from django.contrib import admin
from blogs.models import Entry, Tags, Category

# Register your models here.
class EntryAdmin(admin.ModelAdmin):
  list_display = ("blog_title", "description",)



# Register your models here.
class TagAdmin(admin.ModelAdmin):
  list_display = ("tag_name",)
  


# Register your models here.
class CatAdmin(admin.ModelAdmin):
  list_display = ("cat_name",)
  

  
admin.site.register(Tags, TagAdmin)
admin.site.register(Category, CatAdmin)
admin.site.register(Entry, EntryAdmin)
