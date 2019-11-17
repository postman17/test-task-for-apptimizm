from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('accounts/', include('users.urls')),
    path('cars/', include('auto.urls'))
]
