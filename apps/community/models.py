from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
# My models:

class User(AbstractUser):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('LGBT', 'LGBT'),
    )
    gender = models.CharField(
        max_length = 6,
        choices = gender_choices,
    )
    profile_picture = models.ImageField(upload_to = 'apps/community/static/files/profile_pictures/', blank = True)
    about_me = models.TextField()
    singed_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return '%s %s' % (self.username, self.email)

    def get_user_id(self):
        return self.id
    
    def get_profile_picture(self):
        keyword = str(self.profile_picture)
        key = keyword[22:]
        return key

class Issue(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    image = models.ImageField(upload_to = 'apps/community/static/files/issue_pictures/', blank = True)
    file = models.FileField(upload_to = 'apps/community/static/files/issue_documents/', blank = True)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.title, self.text)

    def get_issue_image(self):
        keyword = str(self.image)
        key = keyword[22:]
        return key

class Comment(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to = 'apps/community/static/files/comment_pictures/', blank = True)
    file = models.FileField(upload_to = 'apps/community/static/files/comment_documents/', blank = True)
    user_id = models.ForeignKey('User', on_delete = models.CASCADE)
    issue_id = models.ForeignKey('Issue', on_delete = models.CASCADE)

    def __str__(self):
        return '%s' % (self.text)

    def get_comment_image(self):
        keyword = str(self.image)
        key = keyword[22:]
        return key