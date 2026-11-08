from django.contrib import admin
from .models import Course, Module, Topic, Subtopic, StudyMaterial

# Inline allows you to add Subtopics directly inside a Topic
class SubtopicInline(admin.StackedInline):
    model = Subtopic
    extra = 1 

# Inline allows you to add Topics directly inside a Module
class TopicInline(admin.StackedInline):
    model = Topic
    extra = 1
    show_change_link = True

# Inline allows you to add Modules directly inside a Course
class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1
    show_change_link = True

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Added 'image' here so you can see if a photo is uploaded
    list_display = ('title', 'level', 'duration', 'image')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter = ('course',)
    inlines = [TopicInline]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'module')
    list_filter = ('module__course',)
    inlines = [SubtopicInline]

@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic')
    list_filter = ('topic__module__course',)

# Register the materials model (if you added it to models.py)
@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category', 'uploaded_at')