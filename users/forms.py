from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from design.models import Comment
from users.models import UserComment
# Create your models here.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields =['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        for fieldname in ['username','password1','password2']:
            self.fields[fieldname].help_text = None
        
class UserCommentForm(UserCreationForm):
    comment = forms.Textarea()
    class Meta:
        model = UserComment
        fields = ['author','comment']
