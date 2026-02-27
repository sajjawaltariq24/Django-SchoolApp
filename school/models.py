from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    name = models.CharField(max_length=50)
    teacher =models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    name = models.CharField(max_length=20)
    section = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_no =models.IntegerField(unique=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="student")

    def __str__(self):
        return self.name
    

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}"