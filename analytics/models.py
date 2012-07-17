from django.db import models

# Create your models here.

class Hit(models.Model):
    source_ip = models.CharField(max_length=512)
    timestamp = models.DateTimeField()
    method = models.CharField(max_length=10)
    url = models.CharField(max_length=4096)
    status_code = models.IntegerField()
    response_size = models.IntegerField(blank=True,null=True)
    referer_url = models.CharField(max_length=4096, blank=True, null=True)
    user_agent = models.CharField(max_length=512)

