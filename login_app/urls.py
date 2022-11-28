from django.urls import path
from django.urls import re_path as url
from login_app.views import index, register, login_page, user_login, user_logout
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'login_app'

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_page, name='login'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
