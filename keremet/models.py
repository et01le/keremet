from uuid import uuid4
from django.db import models
from django.contrib.auth import get_user_model

class Term(models.Model):

    term_id = models.UUIDField(primary_key = True, default = uuid4)
    term = models.TextField(unique = True)
    translation = models.TextField()
    created_by = models.ForeignKey(get_user_model(), on_delete = models.DO_NOTHING)
    created_when = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.term
