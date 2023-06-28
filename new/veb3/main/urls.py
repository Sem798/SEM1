from django.urls import path
from. import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('create',views.create, name='create'),
    path('DZ_1',views.DZ_1, name='DZ_1'),

]
