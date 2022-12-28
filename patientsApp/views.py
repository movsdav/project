from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView, DeleteView, UpdateView
from django.views import View

from .models import Patient
from .forms import PatientForm, PatientUUIDForm


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patients/create_patient.html'

    def form_valid(self, form):
        instance = form.save()
        self.request.user.doctor.patients.add(instance)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('display_patient', kwargs={'uuid': self.object.uuid})


class PatientUUIDView(View):
    form_class = PatientUUIDForm
    template_name = 'patients/get_patient_uuid.html'
    context = {
    }

    def get(self, req, *args, **kwargs):
        form = self.form_class(req.POST or None)
        self.context['form'] = form
        self.context['patient_not_found'] = False
        return render(req, self.template_name, self.context)

    def post(self, req, *args, **kwargs):
        form = self.form_class(req.POST or None)
        patient_uuid = None

        if form.is_valid():
            patient_uuid = form.cleaned_data.get('uuid')

        if Patient.objects.filter(uuid=patient_uuid).exists():
            return redirect('display_patient', uuid=patient_uuid)
        else:
            self.context['patient_not_found'] = True
            return render(req, self.template_name, self.context)


class PatientDetailView(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'patients/display_patient.html'

    def get_object(self, queryset=None):
        return Patient.objects.get(uuid=self.kwargs.get('uuid'))


class PatientListView(ListView):
    template_name = 'patients/patients_list.html'
    model = Patient
    context_object_name = 'patients'

    def get_queryset(self):
        return self.request.user.doctor.patients.all()


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient_list')

    def get_object(self, queryset=None):
        return Patient.objects.get(uuid=self.kwargs.get('uuid'))


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    success_url = reverse_lazy('patient_list')
    template_name = 'patients/update_patient.html'

    def get_object(self, queryset=None):
        return Patient.objects.get(uuid=self.kwargs.get('uuid'))
