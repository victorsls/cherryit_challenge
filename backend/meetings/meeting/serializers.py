from rest_framework import serializers

from meetings.meeting.models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = ('title', 'image', 'date')
