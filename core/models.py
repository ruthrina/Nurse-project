from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    level = models.CharField(max_length=50)
    # ADDED: Image field for the course cards
    image = models.ImageField(upload_to='courses/', blank=True, null=True) 
    
    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

# 1. The Main Topic (Title)
class Topic(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200, help_text="E.g., Diseases")
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title} ({self.module.title})"

# 2. The Subtopics (Diseases)
class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subtopics')
    title = models.CharField(max_length=200, help_text="E.g., Malaria")
    description = models.TextField(help_text="The main study notes text for this subtopic.")
    image = models.ImageField(upload_to='subtopics/', blank=True, null=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.topic.title} - {self.title}"

class StudyMaterial(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=[
        ('notes', 'Lecture Notes'),
        ('pdf', 'Revision PDF'),
        ('past_paper', 'Past Paper'),
        ('guideline', 'Clinical Guideline')
    ])
    file = models.FileField(upload_to='materials/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title