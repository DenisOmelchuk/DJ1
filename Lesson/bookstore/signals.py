from django.db.models.signals import post_save
from django.dispatch import receiver
from bookstore.models import Book


@receiver(post_save, sender=Book)
def update_example_field(sender, instance, created, **kwargs):
    if created:
        instance.example = f'{instance.name}/{instance.year}/id:{instance.id}'
        instance.save()

