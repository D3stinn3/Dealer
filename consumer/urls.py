from django.urls import path, include
from consumer import views

urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('auth/', views.auth_view, name="auth"),
    path('index/', views.index_page, name="index"),
    path('logout/', views.logout_page, name="logout"),
    path('register/', views.register, name="register"),
    path('registration/', views.registration, name="registration"),
    path('search/', views.search, name="search"),
    path('searchresult/', views.searchResult, name="searchresult"),
    path('rent/', views.bookVehicle, name="bookvehicle"),
    path('confirmed/', views.confirmBooking, name="confirm"),
    path('manage/', views.manage, name="manage"),
    path('update/', views.update_order, name="updateorder"),
    path('delete/', views.delete_order, name="deleteorder"),
]
