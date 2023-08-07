from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

class customProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='userprofile')
    profile = models.ImageField(upload_to='image/', blank=True)

    def __str__(self) :
        return self.user.username

    def save(self, *args, **kwargs):
        super(customProfile, self).save(*args, **kwargs)

        if self.profile:
            img = Image.open(self.profile.path)
            max_size = (80, 80)  # Set the maximum size you want for the image
            img.thumbnail(max_size)
            img.save(self.profile.path)
