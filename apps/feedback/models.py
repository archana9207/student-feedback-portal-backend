from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    CATEGORY_CHOICES = [
        ('academic', 'Academic'),
        ('facilities', 'Facilities'),
        ('administration', 'Administration'),
        ('extracurricular', 'Extracurricular'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewed', 'Reviewed'),
        ('resolved', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    subject = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    message = models.TextField()
    rating = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject