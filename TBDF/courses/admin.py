from django.contrib import admin

# Register your models here.

from courses.models import Student, QuizSent, QuizReceived, Course

admin.site.register(Student)
admin.site.register(QuizSent)
admin.site.register(QuizReceived)
admin.site.register(Course)


# Register your models here.
class TopicInline(admin.StackedInline):
    model = Student


class CategoryAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


admin.site.site_header = "The Better Design Foundation"
admin.site.site_title = "Teacher Admin"
admin.site.index_title = "Welcome to Better Design Admin Portal"