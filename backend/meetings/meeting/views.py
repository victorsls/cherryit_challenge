from rest_framework.response import Response
from rest_framework.views import APIView

from meetings.meeting.models import Meeting
from meetings.meeting.serializers import MeetingSerializer


class MeetingList(APIView):
    def get(self, request):
        queryset = Meeting.objects.filter(employees=request.user)
        serializer = MeetingSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
