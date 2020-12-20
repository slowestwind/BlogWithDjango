from django.db import models

# Create your models here.

class BlogPost(models.Model):
    blog_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=100)
    blog_content = models.TextField()
    blog_slug = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=50)
    blog_time = models.DateField(blank=True)
    blog_category = models.CharField(max_length=50)
    blog_thumbnail = models.ImageField(upload_to='images/blog-post/')

    def __str__(self):
        # BlogPost table, field that will be showing in the admin panel
        return self.blog_title+" by "+self.blog_author
    