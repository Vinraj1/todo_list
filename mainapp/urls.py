from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.signup, name='signup'),

    path('login/', views.loginn, name='login'),

    path('todopage/', views.todo, name='todopage'),

    path('edit_todo/<int:srno>', views.edit_todo, name='edit_todo'),

    path('delete_todo/<int:srno>', views.delete_todo, name='delete_todo'),

    path('signout/', views.signout, name="signout"),

    # ===============================
    # PASSWORD RESET FLOW (ADD THIS)
    # ===============================

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='registration/password_reset_form.html'
         ),
         name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]