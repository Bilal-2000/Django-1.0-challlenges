from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "navbar"),
    path('<int:month>',views.monthly_challenges_a_number),
    path('<str:month>',views.monthly_challenges,name="only-url"),
]