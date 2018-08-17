from django.db import models


# Create your models here.



class library(models.Model):
    libraryId = models.AutoField(primary_key=True, db_index=True)
    fun = models.CharField(max_length=50, null=False)
    doubt = models.CharField(max_length=50, null=False)
    doubtDesc = models.CharField(max_length=500, null=False)
    processDoubtWay = models.CharField(max_length=500, null=False)
    difficultyTypeId = models.IntegerField(null=False)
    contributor = models.CharField(max_length=100, null=False)
    contributeDate = models.DateTimeField()
    lastUpdateDate = models.DateTimeField()
    lcv = models.BooleanField()
    class Meta:
        db_table='library'
