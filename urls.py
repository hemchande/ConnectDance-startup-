from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('JobPortal.urls'))
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


from django.urls import path
from .views import *

urlpatterns = [
   path('', home, name = 'home'),
   path('login/',loginUser, name = 'login'),
   path('logout/',logoutUser,name = 'logout'),
   path('register/', registerUser, name = 'register'),
   path('apply/', applyPage, name = 'apply')
]

