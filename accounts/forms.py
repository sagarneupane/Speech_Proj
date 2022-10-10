from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm,SetPasswordForm
from accounts.models import MyUser


class DateWidget(forms.DateInput):
    input_type = 'date' 

class CustomUserCreationForm(UserCreationForm):
    
    first_name = forms.CharField(
    required=True, max_length=255,
    widget=forms.TextInput(attrs={"id":"firstname","class":"form-control form-control-lg"})
    )

    last_name = forms.CharField(required=True, max_length=255,
    widget=forms.TextInput(attrs={"id":"lastname","class":"form-control form-control-lg"})
    )

    class Meta:
        model = MyUser
        fields = ["first_name","middle_name","last_name","age","date_of_birth","email",
        "phone_number","username"]
        widgets = {
            "date_of_birth":DateWidget(attrs={
                "id":"date",
                "class":"form-control form-control-lg"
                }),
            "middle_name":forms.TextInput(attrs={
                "id":"middlename",
                "class":"form-control form-control-lg"
                }),
            "age":forms.NumberInput(attrs={
                "id":"age",
                "class":"form-control form-control-lg"
                }),
            "email":forms.EmailInput(attrs={
                "id":"email",
                "class":"form-control form-control-lg"
            }),
            "phone_number":forms.TextInput(attrs={
                "id":"phonenumber",
                "class":"form-control form-control-lg"
            }),
            "username":forms.TextInput(attrs={
                "id":"username",
                "class":"form-control form-control-lg",
            }),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            "id":"password1",
            "class":"form-control form-control-lg"
            })
        self.fields['password2'].widget.attrs.update({
            "id":"password2",
            "class":"form-control form-control-lg",
        })


class CustomAuthenticationForm(AuthenticationForm):

    class Meta:
        model = MyUser
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "id":"username",
            "class":"form-control form-control-lg",
        })
        self.fields["password"].widget.attrs.update({
            "id":"password",
            "class":"form-control form-control-lg",
        })


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            "id":"email",
            "class":"form-control form-control-lg",
        })


class CustomSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["new_password1"].widget.attrs.update({
            "id":"password1",
            "class":"form-control form-control-lg",
        })
        self.fields["new_password2"].widget.attrs.update({
            "id":"password2",
            "class":"form-control form-control-lg",
        })