from django.urls import path
from . import views

urlpatterns = [
    path('<int:question_ID>/', views.game, name='Game-page'),
    path('<int:question_ID>/variant-<int:variant>', views.result, name='Result-page'),
    path('<int:next_id>/propose', views.propose, name='Propose-page'),
]