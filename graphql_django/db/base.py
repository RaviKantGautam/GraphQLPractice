from django.db import models


class ModelAbstractBase(models.Model):
    """
    Abstract base model.
    """
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="Date and time when this entry was "
                                             "created in the system")
    updated = models.DateTimeField(auto_now=True,
                                   help_text="Date and time when the table data was "
                                             "last updated in the system")
    status = models.BooleanField(
        default=True,
        help_text="Toggle the status.",
        verbose_name='active'
        )

    # ---------------------------------------------------------------------------
    # Meta
    # ---------------------------------------------------------------------------
    class Meta:
        abstract = True

