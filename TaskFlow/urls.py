from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, DeleteView

urlpatterns=[
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('FAQ/', views.freqask, name='freqask'),
    path('contact/', views.contact, name='contact'),

    path('login/', views.log, name='log'),
    path('sign_up/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html', email_template_name='password_reset_email.html', ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('tasks/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task-delete'),
]
