from django.db import models
from time import time


def get_upload_file_name(instance, filename):
    """
    Converts filename from database into correctly formatted
    filename.

    # Models call functions by default with an instance. (?)
    # The instance is an instance of the calling model. (?)

    :param instance:
    :param filename:
    :return:string
    """
    return "uploaded_files/%s_%s" % (str(time()).replace('.', '_'), filename)


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    likes = models.IntegerField(default=0)
    # It seems that Django makemigrations requires a default or null=True
    thumbnail = models.FileField(upload_to=get_upload_file_name, null=True, blank=True)

    def __str__(self):
        return self.title
