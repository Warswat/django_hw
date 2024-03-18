from django.contrib import admin

from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main'):
                i += 1
            print(form.cleaned_data.get('is_main'))
        if i == 0:
            raise ValidationError('Укажите основной раздел')
        elif i > 1:
            raise ValidationError('Основным может быть только один раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline,]
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass