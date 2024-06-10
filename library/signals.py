from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_save, sender=Permission)
def create_user_groups(sender, instance, created, **kwargs):
    if created:
        admin_group, created = Group.objects.get_or_create(name='Администратор')
        author_group, created = Group.objects.get_or_create(name='Автор')
        reader_group, created = Group.objects.get_or_create(name='Читатель')

        content_type = ContentType.objects.get_for_model(Book)
        permissions = Permission.objects.filter(content_type=content_type)
        for permission in permissions:
            author_group.permissions.add(permission)

        view_permission = Permission.objects.get(codename='view_book')
        reader_group.permissions.add(view_permission)
