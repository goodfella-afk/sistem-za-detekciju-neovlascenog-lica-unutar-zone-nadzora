from django.db import models
    

class Sistem(models.Model):
    ids = models.IntegerField(db_column='IDs', primary_key=True)  # Field name made lowercase.
    aktivnost = models.CharField(max_length=25)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sistem'


#For better admin visibility of models

def __str__(self):
    return self.status
