from django.urls import path, include
from . import views
from django.contrib.auth import views as v
from trone.views import *

urlpatterns = (
    path('', main_list, name='main_list'),
    path('past/', past_list, name='past_list'),

    path('reg/squads/', squads_reg, name='squads_reg'),
    path('reg/praks/', reg_praks, name='reg_praks'),
    path('reg/duo/', duo_reg, name='duo_reg'),

    path('faq/', how_works, name='how_works'),
    path('faq/praks/', info_praks, name='info_praks'),

    path('success/', success, name='success'),
    path('success/praks/', success_praks, name='success_praks'),
)
