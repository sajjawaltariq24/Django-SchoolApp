from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import  (TeacherViewSet, SubjectViewSet, StudentViewSet,
ResultViewSet, classRoomViewSet)

router = DefaultRouter()
router.register('teacher', TeacherViewSet)
router.register('subjects',SubjectViewSet)
router.register('sudents', StudentViewSet)
router.register('results', ResultViewSet)
router.register('classrooms', classRoomViewSet)

urlpatterns = router.urls
