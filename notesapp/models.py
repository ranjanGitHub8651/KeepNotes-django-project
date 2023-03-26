from django.db import models

class KeepNote(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    notes = models.CharField(max_length=255, null=False)
    created_on = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.id) + " " + self.title
