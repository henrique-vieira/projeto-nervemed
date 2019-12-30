from django.contrib import admin

from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'start_date', 'created_at','image')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug' :('name',)}

    def foto(self, obj):
        return u'<img src="%s">' % (obj.image.url)


admin.site.register(Course, CourseAdmin)
