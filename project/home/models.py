from django.db import models

# Create your models here.

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=50)
    contact_email = models.CharField(max_length=50)
    contact_message = models.TextField()
    contact_time = models.DateTimeField(auto_now_add=True, blank="true")

    def __str__(self):
        return 'Message by: '+self.contact_name+'- '+str(self.contact_time)
    



    