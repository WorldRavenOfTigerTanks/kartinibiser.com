from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}




class ProductAdminForm(forms.ModelForm):
    dopolnitelnie_xapakteristiki = forms.CharField(widget=CKEditorWidget())
    polnoe_opisanie = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Product
        fields = '__all__'

class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm



class PagesAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    fotertitle = forms.CharField(widget=CKEditorWidget())
    fotercontent = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Pages
        fields = '__all__'

class PagesAdmin(admin.ModelAdmin):
    form = PagesAdminForm




class SliderAdminForm(forms.ModelForm):
    title = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Slider
        fields = '__all__'

class SliderAdmin(admin.ModelAdmin):
    form = SliderAdminForm



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Pages , PagesAdmin)
admin.site.register(Slider , SliderAdmin)
admin.site.register(Photos)
