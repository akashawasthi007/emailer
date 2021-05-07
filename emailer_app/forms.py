from django import forms

class FormName(forms.Form):
    receiver_email=forms.CharField(label="Receiver's Email")
    subject=forms.CharField(label="Subject")
    text=forms.CharField(widget=forms.Textarea)
    file=forms.FileField(required=False)
