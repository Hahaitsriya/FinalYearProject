"""
URL configuration for HealthPal_Nepal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication import views
import dashboard.views
import blogs.views
from django.conf import settings
from django.conf.urls.static import static
import appointment.views
from chatbox.views import chatbox


urlpatterns = [
    path('',views.home,name="index"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name='logout'),
    path('signup/',views.signup,name="signup"),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('dashboard/',dashboard.views.dashboard,name="dashboard"),
    path('post_dashboard/',dashboard.views.post_dashboard,name='post_dashboard'),
    path('register_view/<str:pk>/',dashboard.views.register_view,name='register_view'),
    path('session/',appointment.views.session,name='session'),
    path('user_doctor/',dashboard.views.user_doctor, name='user_doctor'),
    path('user_doctor_profile/<int:user_id>/',appointment.views.user_doctor_profile,name="user_doctor_profile"),
    path('accept_appointment/<int:id>',appointment.views.accept_appointment,name='accept_appointment'),
    path('about/',views.about_page, name='about'),
    path('base_home',dashboard.views.base_home,name='base_home'),
    path('admin/', admin.site.urls),
    path('upload_blog/',blogs.views.blog_upload,name='upload_blog'),
    path('blog/',blogs.views.blog,name='blog'),
    path('chatbox/',chatbox,name='chatbox'),
    path('search/', appointment.views.search_results, name='search_results'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 


