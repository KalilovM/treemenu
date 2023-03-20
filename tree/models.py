from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
