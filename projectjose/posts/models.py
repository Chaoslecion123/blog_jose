from django.db import models


class Post(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=80)
    subtitle = models.CharField(max_length=80)
    content = models.TextField()
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['created']

    def __str__(self):
        return self.title


class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='images',
        related_query_name='image',
        on_delete=models.CASCADE
    )

    image = models.ImageField(
        upload_to='post',
        blank=False
    )


    alt = models.CharField(
        max_length=128,
        blank=True
    )
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de edición", auto_now=True)

    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        ordering = ['created']

    def __str__(self):
        return self.alt
