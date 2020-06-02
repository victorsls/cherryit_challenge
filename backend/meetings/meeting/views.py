from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from meetings.meeting.models import Meeting
from meetings.meeting.serializers import MeetingSerializer


# class MeetingViewSet(viewsets.ModelViewSet):
#     serializer_class = MeetingSerializer
#     http_method_names = ['get']
#
#     def get_queryset(self):
#         return Meeting.objects.filter(employees=self.request.user)


class MeetingList(APIView):
    def get(self, request):
        serializer = MeetingSerializer(Meeting.objects.filter(employees=request.user), many=True,
                                       context={'request': request})
        return Response(serializer.data)
