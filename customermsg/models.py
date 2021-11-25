from django.db import models

class messages(models.Model):
    client_name = models.CharField(max_length=200)
    client_email = models.EmailField(max_length=200)
    client_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.client_name
        