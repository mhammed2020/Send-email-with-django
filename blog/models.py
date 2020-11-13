from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    class Meta :
        ordering = ('-date_posted',)

class Comment(models.Model):
    
    name = models.CharField(max_length=50 )
    email = models.EmailField()
    body = models.TextField(verbose_name='Comment')

    comment_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    

    def __str__(self):
        return '  {} comments {} '.format(self.name,self.post)

    

    class Meta :
        ordering = ('-comment_date',)
class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content=models.TextField()
    img=models.ImageField(upload_to='post_img/',default='post_img/default.png')
    created = models.DateTimeField(default=timezone.now())
    def __str__(self):
        return  self.title

    
    