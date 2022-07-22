from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('update-user/', views.updateUser, name='update-user'),
    path('', views.home, name='home'),
    path('job/<str:pk>', views.job, name='job'),
    path('companies/', views.companiesPage, name='companies'),
    path('saved/', views.savedPage, name='saved'),
    #path('create-job/', views.createJob, name='create-job'),
    path('profile/', views.userProfile, name='user-profile'),
    path('create-company/', views.createCompany, name='create-company'),
    path('update-company/<str:pk>', views.updateCompany, name='update-company'),
    path('delete-company/<str:pk>', views.deleteCompany, name='delete-company'),
    path('delete-job/<str:pk>', views.deleteJob, name='delete-job'),
    path('delete-saved/<str:pk>', views.deleteSaved, name='delete-saved'),

]