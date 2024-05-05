from django.db import models


class Service(models.Model):
    """Model for table service"""

    name = models.CharField(
        max_length=120,
        verbose_name="Name",
    )
    description = models.TextField(
        verbose_name="Description",
        blank=True,
        null=True,
        max_length=1500
    )
    post = models.ForeignKey(
        'blog.Post',
        on_delete=models.CASCADE,
        verbose_name="Post",
        related_name='services',
        blank=True,
        null=True,
    )
    image = models.ImageField(
        verbose_name="Image",
        blank=True,
        null=True,
        upload_to='service/',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        ordering = ['-post']
        db_table = 'service'


