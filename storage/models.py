from django.db import models

class Sequence(models.Model):
    """
    DNA sequence that can be added and then requested by name.
    Sequence can have only "ACTGactg" letters, maximum 20000. Name is up to 100 chars.
    Both fields are mandatory.
    """
    name = models.CharField(max_length=100, blank=False)
    sequence = models.TextField(max_length=20000, blank=False)
    def __str__(self):
        return self.name

    objects = models.Manager()

