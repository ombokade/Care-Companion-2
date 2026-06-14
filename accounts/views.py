from django.contrib import messages
from django.shortcuts import render, redirect
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
            return redirect('home')
    else:
        form = PatientForm()

    patients = Patient.objects.all()
    return render(request, 'home.html', {'form': form, 'patients': patients})


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('home')

def edit_patient(request, id):
    patient = Patient.objects.get(id=id)

    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']

        patient.save()

        return redirect('home')

    return render(request, 'edit.html', {'patient': patient})
    

