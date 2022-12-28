from django.urls import path

from .views import PatientCreateView, PatientDetailView, PatientUUIDView, PatientListView, PatientDeleteView, \
    PatientUpdateView

urlpatterns = [
    path('add_patient/', PatientCreateView.as_view(), name='add_patient'),
    path('find_patient/', PatientUUIDView.as_view(), name='find_patient'),
    path('all_patients/', PatientListView.as_view(), name='patient_list'),
    path('display_patient/<uuid:uuid>', PatientDetailView.as_view(), name='display_patient'),
    path('display_patient/<uuid:uuid>/delete', PatientDeleteView.as_view(), name='delete_patient'),
    path('display_patient/<uuid:uuid>/update', PatientUpdateView.as_view(), name='update_patient'),
]



