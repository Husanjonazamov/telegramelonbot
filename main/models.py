from django.db import models




class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Notice(models.Model):
    description = models.TextField()
    interval = models.PositiveIntegerField(help_text="Interval in seconds")  

    