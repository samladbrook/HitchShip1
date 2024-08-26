# jobs/models.py
from django.db import models
from django.conf import settings

class Job(models.Model):
    STATUS_CHOICES = [
        ('unassigned', 'Unassigned'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ]
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    description = models.TextField()
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    date_added = models.DateField(auto_now_add=True)
    total_weight = models.DecimalField(max_digits=10, decimal_places=1, default=0.0)
    SKU = models.IntegerField(blank=True, null=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE, related_name='jobs_added')
    accepted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name='jobs_accepted')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='unassigned'
    )

    def __str__(self):
        return f"{self.item_name} ({self.status})"