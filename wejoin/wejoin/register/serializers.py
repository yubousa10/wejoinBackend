from .models import Register
from .models import UserBase

from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = (
            'pk',
            'userbase',
            'fname',
            'lname',
            'gender',
            'profile',
            'register_date',
            'tel',
            'zipcode',
        )
        
        def __unicode__(self):
            return u"%i" % self.pk
        
        class Meta:
            verbose_name_plural = "Register"
            
class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBase
        fields = (
            'pk',
            'email',
            'password'
        )
        
        def __unicode__(self):
            return u"%i" % self.pk
        
        class Meta:
            verbose_name_plural = "UserBase"
            