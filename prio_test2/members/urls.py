from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    
]

urlpatterns += staticfiles_urlpatterns()