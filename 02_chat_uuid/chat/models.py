from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    uuid = models.UUIDField(default=uuid4, editable=False)
    members = models.ManyToManyField(User)

    def add_user(self, user):
        """Agrega un usuario al grupo."""
        self.members.add(user)
        self.save()

    def remove_user(self, user):
        """Elimina un usuario del grupo."""
        self.members.remove(user)
        self.save()


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
