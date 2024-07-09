from django.db import models

class Trophy(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    
    # Returns the primary key of the trophy
    def __int__(self):
        return self.pk
    
    # Returns a string representation of the trophy
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Troféus"  # Plural name for the model in admin interface
        verbose_name = "Troféu"  # Singular name for the model in admin interface
        ordering = ['name']  # Orders trophies by name
