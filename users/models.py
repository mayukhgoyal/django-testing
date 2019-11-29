from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:        
        verbose_name ="User"
        verbose_name_plural ="Users"
    username = models.CharField(verbose_name='User Name', max_length=200)
    email = models.EmailField(verbose_name='Email',max_length=200,blank=False,null=False, unique=True)
    is_active = models.BooleanField(verbose_name='Is Active',default=False)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', )
  
    def __str__(self):
        return str(self.username)
    def __unicode__(self):
        return unicode(self.username)