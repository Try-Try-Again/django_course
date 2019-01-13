from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
            ('draft', 'Draft'),
            ('published', 'Published'),
    )
    #creates a field for the post title
    #creates a VARCHAR column in the SQL database
    title = models.CharField(max_length=250)
    #a slug is a short label with only letters, numbers, underscores, or hyphens
    #creates a field to be used in URLs
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
                            #^so we can build URLs containing publish date
    #TBC p.16
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS_CHOICES,
                                default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
# Create your models here.
