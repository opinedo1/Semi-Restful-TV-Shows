from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if postData['description'] != '' and len(postData['description']) < 10:
            errors["description"] = "Show description should be at least 10 characters"
        if postData['release_date'] == '':
            errors['release_date'] = 'Release Date field should be not be empty'
        else:
            if datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.now():
                errors['release_date'] = 'Release Date should be in the past'
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
