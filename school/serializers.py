from rest_framework import serializers
from .models import Teacher, ClassRoom, Student, Result, Subject

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"

class ClassRoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = "__all__"

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ResultSerializers(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = "__all__"

class SubjectSerialilzers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"