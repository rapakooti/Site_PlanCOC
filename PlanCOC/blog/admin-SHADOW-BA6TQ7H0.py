from django.contrib import admin
from .models import PostPlan , Category, comment


# Register your models here.
# admin.site.register(PostPlan)



@admin.register(PostPlan)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'Niveau', 'status', 'author', 'created')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title','usage')
    ordering = ('title', 'author','created')
    list_filter = ('status', 'author','category')

admin.site.register(Category)


@admin.register(comment )
class commentsAdmin(admin.ModelAdmin):
    list_display= ['username','email','created']