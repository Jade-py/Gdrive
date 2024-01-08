from django.db import models


# Create your models here.
class Storage_Folder(models.Model):
    folder = models.TextField()


class Storage_File(models.Model):
    file = models.FileField()
    folder = models.ForeignKey(Storage_Folder, on_delete=models.CASCADE)