from django.db import models


class CommunicationService(models.Model):
    """Model for table communication_services."""
    subject = models.CharField(
        max_length=255,
        verbose_name='Subject',
    )
    email = models.EmailField(
        verbose_name='Email',
    )
    message = models.TextField(
        verbose_name='Message',
        max_length=1000,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Active',
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at',
    )

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Communication Service'
        verbose_name_plural = 'Communication Services'
        ordering = ['-created_at']
        db_table = 'communication_service'

