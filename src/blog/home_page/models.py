from django.db import models

# Create your models here.
class Main(models.Model):
    class Meta:
        abstract = True

    main_info = models.CharField(max_length=100)
    def get_main_info(self):
        return self.main_info

