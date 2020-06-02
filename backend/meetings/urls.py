from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('meetings.meeting.urls', namespace='meeting')),
                  path('login/', obtain_auth_token),
              ] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))
