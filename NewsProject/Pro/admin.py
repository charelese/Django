from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


from .models import Human, Profession

class HumanAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Human
        fields = '__all__'

class HumanAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession', 'name', 'surname', 'birthday', 'age', 'height', 'weight')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'surname')
    list_filter = ('name', 'id')
    list_editable = ['birthday', 'profession']
    fields = ('name', 'surname', 'birthday', 'age', 'height', 'weight')
    readonly_fields = ()
    form = HumanAdminForm

class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


admin.site.register(Human, HumanAdmin)
admin.site.register(Profession, ProfessionAdmin)

admin.site.site_title = 'Страница администратора'
admin.site.site_header = 'Страница администратора'
