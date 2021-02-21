from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(
        label='', widget=forms.TextInput(attrs={"placeholder": "Yoda"}))
    email       = forms.EmailField()
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                            attrs={
                                "class": "new class",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "cols": 120
                            }
                            )
                    )
    price       = forms.DecimalField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self. cleaned_data.get("title")
        if not "Waldi" in title:
            raise forms.ValidationError("This is not a valid title")
        if not "news" in title:
            raise forms.ValidationError("Well what the heck")
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email.")
        return title

class RawProductForm(forms.Form):
    title       = forms.CharField(
        label='', widget=forms.TextInput(attrs={"placeholder": "Yoda"}))
    description = forms.CharField(
                    required=False, 
                    widget=forms.Textarea(
                            attrs={
                                "class": "new class",
                                "id": "my-id-for-textarea",
                                "rows": 20,
                                "cols": 120
                            }
                            )
                    )
    price       = forms.DecimalField(initial=199.99)