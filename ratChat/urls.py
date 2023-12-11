from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name ='login'),
    path('logout', auth_views.LogoutView.as_view(), name= 'logout'),

    #Salas
    path('rooms', views.rooms, name='rooms'),
    path('<slug:slug>', views.room, name='room'),
]

#Permite que se vean las imagenes de la BD:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
