from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Team(models.Model):
    """Model for table team"""

    place = models.CharField(
        max_length=120,
        verbose_name="Place"
    )
    full_name = models.CharField(
        max_length=120,
        verbose_name="Full name",
        blank=True,
        null=True
    )
    comment = models.TextField(
        max_length=1000,
        verbose_name="Comment",
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='images/team_photos/',
        blank=True,
        null=True,
        verbose_name="Photo",
    )
    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f"{self.place}"

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"
        ordering = ['place']
        db_table = 'team'


class Feedback(models.Model):
    """Model for table feedback"""

    created_as = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    assessment = models.IntegerField(
        verbose_name="Assessment",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    feedback = models.TextField(
        max_length=1500,
        verbose_name="Feedback",
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Is feedback active"
    )

    def __str__(self):
        return f"{self.assessment}, {self.feedback[:15]}, {self.created_as}"

    class Meta:
        verbose_name = "Feedback"
        verbose_name_plural = "Feedbacks"
        db_table = 'feedback'
        ordering = ['created_as']
