from django.urls import path, include
from rest_framework import routers

# from meetings.meeting.views import MeetingViewSet
from meetings.meeting.views import MeetingList

# router = routers.DefaultRouter()
# router.register(r'meetings', MeetingViewSet, basename='meetings')

app_name = 'meeting'
urlpatterns = [
    # path('', include(router.urls))
    path('meetings/', MeetingList.as_view()),
]
