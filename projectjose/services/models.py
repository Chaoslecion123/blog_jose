from django.db import models
from django.core.exceptions import ValidationError


class Service(models.Model):
    title = models.CharField(max_length=80)
    icon = models.FileField(upload_to='iconos',null=True,blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='services',null=True,blank=True)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        ordering = ['created']

    def __str__(self):
        return self.title

class AttributeService(models.Model):
    service = models.ForeignKey(
        Service,
        related_name='attributes',
        related_query_name='attribute',
        on_delete=models.CASCADE
    )
    name  = models.CharField(max_length=100)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "Atributo"
        verbose_name_plural = "Atributos"
        ordering = ['created']


    def __str__(self):
        return self.name
