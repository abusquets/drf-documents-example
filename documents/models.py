import os

from django.db import models
from django.dispatch import receiver


class Document(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False,
                             blank=False)
    project_file = models.FileField(upload_to='upload', null=False,
                                    blank=False)

    def __str__(self):
        return '%s' % self.title

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


@receiver(models.signals.post_delete, sender=Document)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Delete the project file if the service is deleted
    """
    if instance.project_file:
        if os.path.isfile(instance.project_file.path):
            os.remove(instance.project_file.path)


@receiver(models.signals.pre_save, sender=Document)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Delete the project file only when it changes
    """
    if not instance.pk:
        return False
    old_file = None
    try:
        old_file = (Document.objects.get(pk=instance.pk)).project_file
    except Document.DoesNotExist:
        return False

    new_file = instance.project_file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
