from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # admin path already included in project urls; remove to avoid duplicate namespace warning
    path('',views.signup),
    path('login/',views.loginn),
    path('todopage/',views.todo),
    path('edit_todo/<int:srno>',views.edit_todo,name='edit_todo'),
    path('delete_todo/<int:srno>',views.delete_todo),
    path('signout/',views.signout,name="signout")
]
