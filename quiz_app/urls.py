from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:pk>/', get_questions, name='category'),


    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register_user, name='register'),
    path('profile/<int:pk>/', profile_view, name='profile'),
    path('edit_account/', edit_account_view, name='edit_account'),
    path('edit_profile/', edit_profile_view, name='edit_profile'),


    path('quiz_results/', quiz_results, name='quiz_results'),

    path('about_us/', about_us, name='about_us'),
    path('search_bar/', search_bar, name='search_bar'),
    path('word/', word, name='word'),

]




