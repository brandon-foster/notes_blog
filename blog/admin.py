from django.contrib import admin
from django.forms import ModelForm

from redactor.widgets import RedactorEditor

from blog.models import Post

class PostAdminForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': RedactorEditor(),
        }

class PostAdmin(admin.ModelAdmin):
    # fields display on change list
    list_display = ['title', 'description', 'course_name']
    
    # fields to filter the change list with
    list_filter = ['published', 'created', 'course_name']
    
    # fields to search in change list
    search_fields = ['title', 'description', 'content', 'course_name']

    # enable the date drill down on change list
    date_hierarchy = 'created'
    
    # enable the save buttons on top of change form
    save_on_top = True
    
    # prepopulate the slug from the title - big timesaver!
    prepopulated_fields = {"slug": ("title",)}
    
    # redactor
    form = PostAdminForm

admin.site.register(Post, PostAdmin)
