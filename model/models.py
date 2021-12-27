from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ModelObjEnvinterface(models.Model):
    interfaceid = models.BigAutoField(primary_key=True)
    carLicenseno = models.CharField(db_column='carLicenseno', max_length=20, blank=True, null=True)  # Field name made lowercase.
    readtime = models.DateTimeField(blank=True, null=True)
    baidulongitude = models.CharField(max_length=20, blank=True, null=True)
    baidulatitude = models.CharField(max_length=20, blank=True, null=True)
    gpslongitude = models.CharField(max_length=20, blank=True, null=True)
    gpslatitude = models.CharField(max_length=20, blank=True, null=True)
    recordspeed = models.IntegerField(blank=True, null=True)
    cardirection = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    loadweight = models.IntegerField(blank=True, null=True)
    garabtype = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'model_obj_envinterface'

