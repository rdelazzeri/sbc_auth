from django.db import models
#from django.contrib.auth.models import User
from threading import local
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


class BaseModel(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_created_by', null=True, blank=True,)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='%(class)s_updated_by', null=True, blank=True,)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        abstract=True # Set this model as Abstract

    def save(self, *args, **kwargs):
        # Set the author to the current user before saving
        if not self.pk:  # Check if it's a new instance
            #print('no pk')
            user = kwargs.pop('user', None)
            #print(user)
        else:
            print('pk')
        super().save(*args, **kwargs)