from django import forms
from .models import Product

class ProductCreationForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'available_quantity', 'is_prescription_needed', 'product_image']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'available_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'is_prescription_needed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
    
    def save(self, commit=True, user=None):  
        product = super().save(commit=False)
        if user:
            product.pharmacy = user
        if commit:
            product.save()
        return product
    

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'available_quantity', 'is_prescription_needed', 'product_image']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter product name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter product description'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'available_quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'}),
            'is_prescription_needed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        
