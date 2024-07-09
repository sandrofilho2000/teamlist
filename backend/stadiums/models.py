from django.db import models

class Stadium(models.Model):
    # Basic stadium information
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)  # Slug for URL
    link = models.CharField(max_length=255)  # Link to external resource

    # Stadium characteristics
    seats = models.IntegerField(default=0)  # Number of seats
    build_year = models.CharField(max_length=255)  # Year of construction
    grass_heat = models.CharField(max_length=255)  # Heat tolerance of grass
    grass_type = models.CharField(max_length=255)  # Type of grass
    grass_size = models.CharField(max_length=255)  # Size of grass area

    # Stadium images
    imgs = models.CharField(max_length=255)  # Comma-separated URLs of images

    # Additional stadium features
    staterooms = models.IntegerField(default=0)  # Number of staterooms
    build_value = models.CharField(max_length=255)  # Estimated value of construction
    oficial_site = models.CharField(max_length=255)  # Official website URL
    phone = models.CharField(max_length=255)  # Contact phone number

    # Stadium capacity
    crowd_capacity = models.IntegerField(default=0)  # Maximum capacity
    team_name = models.CharField(max_length=255)  # Associated team name

    def __str__(self):
        return self.name  # String representation of the stadium object
