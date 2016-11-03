from django.shortcuts import render
from django.forms import inlineformset_factory

from .forms import SpecificationForm, SetupForm
from .models import Setup, Specification


def handle_setup(request):

    if request.method == 'POST':
        form = SetupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = SetupForm()


    return render(request, 'index.html', {'form': form, 'setups': Setup.objects.all()})


def handle_specification(request, setup_id):
    setup = Setup.objects.get(pk=setup_id)
    SpecificationFormset = inlineformset_factory(Setup, Specification, SpecificationForm, exclude=['setup'], extra=3)

    if request.method == 'POST':
        formset = SpecificationFormset(request.POST, request.FILES, instance=setup)
        if formset.is_valid():
            formset.save()
    else:
        formset = SpecificationFormset(instance=setup)


    return render(request, 'setup.html', {'formset': formset, 'specifications': setup.target_specs.all(), 'setup': setup})
