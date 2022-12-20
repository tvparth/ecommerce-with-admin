from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import password_validation
from . models import Customer
from store.models import Product


#Customer Registraion Form
class CustomerRegistraionForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    # That Is Use Of The Password2 Conformation
    password2 = forms.CharField(label = 'Confirm Password(agin)',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    email = forms.CharField(required= True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email' ,'password1','password2']
        lables ={'email':'Email'}
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}), # Form control for fields 
            # 'email':forms.EmailInput(attrs={'class':'form-control'}),
            }


#Login Forms
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password =forms.CharField(label=_("Password"), strip=False,
        widget=forms.TextInput(attrs={'autocomplete':'current-password','class':'form-control'}))


#Change Password Form
class PasswordChangeForm(PasswordChangeForm):
    
    old_password = forms.CharField(label=_("Old Password"), strip=False,
        # widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus': True,'class':'form-control'})),
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'})),
    
    
    new_password1 = forms.CharField(label= _("New Password"), strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
        help_text = password_validation.password_validators_help_text_html())

    
    # That Is Use Of The Password2 Conformation
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))



# PassWord Reset Form
class MyPasswordResetForm(PasswordResetForm):
     email = forms.EmailField(label=_("Email"),max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class':'form-control'}))



# Change Pass Form
class MySetPasswordForm(SetPasswordForm):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )


# Customer Profile Form
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','state','zipcode']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta :
        model = Product
        fields = ['title','selling_price','description','brand']
        # fields = '__all__'
        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control'}),
            'selling_price':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','cols': 5, 'rows': 1}),
            'brand':forms.TextInput(attrs={'class':'form-control'}),
            'file': forms.FileField() 
           
            
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
