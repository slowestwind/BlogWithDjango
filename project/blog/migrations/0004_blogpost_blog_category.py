# Generated by Django 3.1.4 on 2020-12-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpost_blog_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='blog_category',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
