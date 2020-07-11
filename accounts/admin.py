from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django import forms

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('nickname','image')}),)
    list_display = ['username', 'email', 'nickname','image']

# Register your models here.
admin.site.register(User, CustomUserAdmin)

class UserCreationForm(forms.ModelForm):
       class Meta:
           model = User
           fields = ('email',)

       def save(self, commit=True):
           # Save the provided password in hashed format
           user = super(UserCreationForm, self).save(commit=False)
           user.set_password(self.cleaned_data["password"])
           if commit:
               user.save()
           return user