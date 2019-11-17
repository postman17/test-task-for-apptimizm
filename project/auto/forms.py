from django import forms

from .models import CarNameModel, CarModel


class CarNameForm(forms.ModelForm):
    lang = forms.ChoiceField(choices=CarNameModel.LANGUAGES)

    class Meta():
        model = CarNameModel
        fields = ('lang', 'name')


class CarForm(forms.ModelForm):
    class Meta():
        model = CarModel
        fields = ('year',)
