from django.db import models
from django.contrib.auth.models import User

# 👨‍💻 Developer
class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# 📁 Project
class Project(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# ✅ Task
class Task(models.Model):
    title = models.CharField(max_length=200)

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.title