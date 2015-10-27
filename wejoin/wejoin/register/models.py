from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class UserBase(models.Model):
    email = models.EmailField(max_length=254, blank=True, default='')
    password = models.CharField(max_length=30, blank=True, default='')
    def __unicode__(self):
        return 'email: ' + self.email
    
    
class Register(models.Model):
    userbase = models.OneToOneField('UserBase', primary_key=True)
    fname = models.CharField(max_length=30, blank=True, default='')
    lname = models.CharField(max_length=30, blank=True, default='')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')
    profile = models.TextField(max_length=512, blank=True, default='')
    register_date = models.DateTimeField(auto_now_add=True)
    tel = models.CharField(max_length=16, blank=True, default='')
    zipcode = models.CharField(max_length=10, blank=True, default='')
    def __unicode__(self):
        return 'email: ' + self.userbase.email
    
    

    
    
    
    
