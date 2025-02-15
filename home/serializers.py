from rest_framework import serializers
from .models import Course,Section,Video
import datetime
import  zoneinfo
class CourseSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='name', read_only=True)
    sections = serializers.SerializerMethodField()
    Time = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = '__all__'

    def get_sections(self, obj):
        result = obj.sections.all()
        return SectionSerializer(result, many=True,partial=True).data

    def get_Time(self, obj):
        results = obj.sections.all()
        all_time_videos = []
        for result in results:
            rs = result.videos.all()
            for video in rs:
                all_time_videos.append(int(video.duration.total_seconds()))

        time_delta = datetime.datetime.fromtimestamp(0,zoneinfo.ZoneInfo('UTC')) + datetime.timedelta(seconds=sum(all_time_videos))
        return  time_delta.strftime('%H:%M:%S')


    def to_representation(self, instance):
        data = super().to_representation(instance)
        sections = data.pop('sections')
        data['sections'] = sections
        return data




class SectionSerializer(serializers.ModelSerializer):
    vidoes = serializers.SerializerMethodField()
    class Meta:
        model = Section
        fields = '__all__'

    def get_vidoes(self, obj):
        result = obj.videos.all()
        return VideoSerializer(result, many=True).data

    def to_representation(self, instance):
        data = super().to_representation(instance)
        video = data.pop('vidoes')
        data['videos'] = video
        return data


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

