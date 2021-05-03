from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
import os
'''
we need a author for each post
author for post = user who created post
user is a seperate table so we need to import user model

from django.contrib.auth.models import User = this is for relationship b/w user model and post model(many  to one) 
 bcz user can have multiple post 
but each post will have unique author
'''


class Post(models.Model):
    title = models.CharField(max_length=100, null=True)
    file = models.FileField(null=True,blank=True,upload_to='Files')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null = True) #if user is dleted delete post also
    content = RichTextUploadingField(blank = True, null = True)
    date_posted = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return self.title

    def extension(self):
        name , extension = os.path.splittest(self.file.name)
        return extension
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})   #for redirect after creating a mew post

    