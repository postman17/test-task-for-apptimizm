from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .forms import CarNameForm, CarForm
from .models import CarNameModel, CarModel
from users.models import UserCars


User = get_user_model()


class AddCarInSystemView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    template_name = 'add-cat-in-system.html'

    def get_context_data(self, **kwargs):
        context = super(AddCarInSystemView, self).get_context_data(**kwargs)
        context['car_name_form_ru'] = CarNameForm(
            self.request.POST or None, initial={'lang': CarNameModel.RUSSIAN}, prefix='car_name_ru')
        context['car_name_form_en'] = CarNameForm(
            self.request.POST or None, initial={'lang': CarNameModel.ENGLISH}, prefix='car_name_en')
        context['car_form'] = CarForm(self.request.POST or None)
        return context

    def post(self, request):
        car_name_form_ru = CarNameForm(request.POST, prefix='car_name_ru')
        car_name_form_en = CarNameForm(request.POST, prefix='car_name_en')
        car_form = CarForm(request.POST)
        if car_name_form_ru.is_valid() and car_name_form_en.is_valid() and car_form.is_valid():
            car = car_form.save()
            name_ru = car_name_form_ru.save()
            name_en = car_name_form_en.save()
            car.name.add(name_ru)
            car.name.add(name_en)
            car.save()
            return redirect('car-list')
        context = self.get_context_data()
        return self.render_to_response(context)


class CarListView(LoginRequiredMixin, ListView):
    login_url = '/'
    template_name = 'car-list.html'
    model = CarModel

    def get_queryset(self):
        return self.model.objects.filter(usercars_car__isnull=True).all()


class AddCarToUser(LoginRequiredMixin, View):
    login_url = '/'

    def get(self, request, *args, **kwargs):
        user = User.objects.get(email=request.user.email)
        car = CarModel.objects.get(id=kwargs.get('pk'))
        model, created = UserCars.objects.get_or_create(user=user)
        model.car.add(car)
        # send_mail(
        #     'Add car to user',
        #     'Hello. You add car to user',
        #     'from@example.com',
        #     [request.user.email],
        #     fail_silently=False,
        # )
        return redirect('profile')
