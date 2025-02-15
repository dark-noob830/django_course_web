from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VideoSerializer,CourseSerializer,SectionSerializer
from .models import Course

class HomeView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)