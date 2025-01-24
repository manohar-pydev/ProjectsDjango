from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.login_page,name='login_page'),
    path('logout/',views.logout_page,name='logout_page'),
    path('delete-transaction/<uuid>/',views.deleteTransaction,name='deleteTransaction')
]