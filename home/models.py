from django.db import models


class Film(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    cata_log_name = models.CharField(max_length=255, blank=True, null=True)
    cata_log_id = models.CharField(max_length=255, blank=True, null=True)
    evaluation = models.FloatField()
    image = models.CharField(max_length=255)
    is_use = models.IntegerField()
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    loc_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    on_decade = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_class_name = models.CharField(max_length=255, blank=True, null=True)
    sub_class_id = models.CharField(max_length=255)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    is_vip = models.IntegerField()

    class Meta:
        db_table = 't_film'
