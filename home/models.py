from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model


class Course(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Video(models.Model):
    name = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/%Y/%m/%d')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='videos')
    is_free = models.BooleanField(default=False, db_index=True)
    description = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
