from django.db import models


class Image(models.Model):

    file = models.FileField()
    caption = models.TextField()
    location = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.caption} - {self.location}'
