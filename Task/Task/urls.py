"""
URL configuration for Task project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from ToDo import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/<str:pk>/', views.ProfileDetailView.as_view(), name='profile'),
    path('login', views.CutomLogin.as_view(), name='login'),
    path('register', views.RegisterPage.as_view(), name='register'),
    path('logout', LogoutView.as_view(next_page = 'login'), name='logout'),
    path('', views.TaskList.as_view(), name='tasks'),
    # path('task/<int:pk>/', views.TaskDetail.as_view(), name='task'),
    path('task-create', views.TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', views.TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', views.TaskDelete.as_view(), name='task-delete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
