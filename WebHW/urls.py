from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('tagQuestion/<str:tag>', views.tagQuestion, name='tagQuestion'),
    path('question/<int:question_id>', views.question, name='question'),
    path('ask', views.ask, name='ask'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('settings', views.settings, name='settings'),
]
