from pyexpat import model
from home.models import Contact
from django import forms

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass