from django.contrib import admin
from .models import Course , Section,Video

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    exclude = ['slug']

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    exclude = ['slug']


