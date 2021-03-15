
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('<int:board>',views.topics,name='topics'),
    path('<int:board>/new',views.new_topic,name='new_topic')
]
