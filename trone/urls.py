from django.urls import path, include
from . import views
from django.contrib.auth import views as v
from trone.views import *

urlpatterns = (
    path('', main_list, name='main_list'),
    path('reg/free/', easy_reg, name='easy_reg'),
    path('tourn/past/', past_list, name='past_list'),
    path('reg/free2/', easy_reg2, name='easy_reg2'),
    path('faq/', how_works, name='how_works'),
    path('reg/pay/', pay, name='pay'),
    path('success/', success, name='success'),
    path('pay/success/', success_pay, name='success_pay'),
)
