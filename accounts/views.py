from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm
from .models import Patient

def home(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            Patient.objects.create(
                name=form.cleaned_data['name'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender']
            )
            messages.success(request, 'Patient registered successfully.')
            return redirect('home')
    else:
        form = PatientForm()

    query = request.GET.get('q', '').strip()
    patients = Patient.objects.all()
    if query:
        patients = patients.filter(name__icontains=query)

    return render(request, 'home.html', {
        'form': form,
        'patients': patients,
        'query': query,
    })


def delete_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    messages.success(request, 'Patient record deleted successfully.')
    return redirect('home')


def edit_patient(request, id):
    patient = get_object_or_404(Patient, id=id)

    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient.name = form.cleaned_data['name']
            patient.age = form.cleaned_data['age']
            patient.gender = form.cleaned_data['gender']
            patient.save()
            messages.success(request, 'Patient details updated successfully.')
            return redirect('home')
    else:
        form = PatientForm(initial={
            'name': patient.name,
            'age': patient.age,
            'gender': patient.gender,
        })

    return render(request, 'edit.html', {'form': form, 'patient': patient})
    

