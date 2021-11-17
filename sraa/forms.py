from django import forms

class UploadFileForm(forms.From):
    tiltle = form.CharField(max_length=500)
    file = forms.FileField()
