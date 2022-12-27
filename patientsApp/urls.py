from django.urls import path

from .views import PatientCreateView, PatientDetailView, PatientUUIDView

urlpatterns = [
    path('add_patient/', PatientCreateView.as_view(), name='add_patient'),
    path('display_patient/<uuid:uuid>', PatientDetailView.as_view(), name='display_patient'),
    path('find_patient/', PatientUUIDView.as_view(), name ='find_patient'),
]
