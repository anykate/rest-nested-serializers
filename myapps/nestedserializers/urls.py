from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'nestedserializers'


router = routers.DefaultRouter()
router.register('marks', views.MarksViewset)
router.register('students', views.StudentsViewset)


urlpatterns = [
    path('', views.savemarks, name='save_marks_data'),
    path('api/', include(router.urls)),
]
