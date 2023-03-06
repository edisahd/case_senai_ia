from django.db import models

class LogSystem(models.Model):
    id = models.AutoField(primary_key=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
    log = models.TextField()

    class Meta:
        db_table = 'log_system'