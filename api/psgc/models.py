from django.db import models
from smart_selects.db_fields import ChainedForeignKey


class Region(models.Model):
    """ Region """
    objects = None
    name = models.CharField("Region", max_length=64, unique=True)
    code = models.CharField("Code", max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Province(models.Model):
    """ Province """
    objects = None
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='province')
    name = models.CharField("Province", max_length=64)
    code = models.CharField("Code", max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class City(models.Model):
    """ City """
    objects = None
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='city')
    province = ChainedForeignKey(
        Province,
        chained_field="region",
        chained_model_field="region",
        show_all=False,
        auto_choose=True,
        sort=True,
    )
    name = models.CharField("City/Municipality", max_length=64)
    code = models.CharField("Code", max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Cities'
        unique_together = ('name', 'code')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"


class Barangay(models.Model):
    """ Barangay """
    objects = None
    region = models.ForeignKey(Region, on_delete=models.PROTECT, related_name='barangay')
    province = ChainedForeignKey(
        Province,
        chained_field="region",
        chained_model_field="region",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    city = ChainedForeignKey(
        City,
        chained_field="province",
        chained_model_field="province",
        show_all=False,
        auto_choose=True,
        sort=True
    )
    name = models.CharField("Barangay", max_length=64)
    code = models.CharField("Code", max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'code')
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"
