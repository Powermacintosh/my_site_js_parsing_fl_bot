from django import forms
from .models import Fl, Tag
from django.core.exceptions import ValidationError


class FlForm(forms.ModelForm):

    # def clean_url(self):
    #     url = self.cleaned_data['url']

    class Meta:
        model = Fl
        # fields = ['link', 'show', 'price', 'ref_link', 'date_p', 'time_p', 'tags', 'image']
        fields = ['tags']
        # widgets = {
        #     'date_p': forms.TextInput(attrs={'class': 'form-control'}),
        #     'time_p': forms.Textarea(attrs={'class': 'form-control'}),
        #     'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        #     'image': forms.ClearableFileInput(attrs={'multiple': True}),
        #     }
        # widgets = {
        #     'show': forms.TextInput,
        #     'ref_link_2': forms.TextInput,
        # }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['title']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug