from django.db import models
from django.urls import reverse
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)


class Tag(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Post(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=70)
    body = models.TextField()
    create_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'id':self.pk})

    class Meta:
        ordering = ['-create_time','title']