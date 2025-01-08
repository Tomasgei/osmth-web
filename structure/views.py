from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Area, Commandery
from .forms import AreaForm, CommanderyForm
from django.contrib import messages

# Kontrola, zda uživatel je K9
def is_k9(user):
    return user.profile.rank == 'knight' and user.profile.user.is_superuser

# Kontrola, zda uživatel je Komtur
def is_komtur(user):
    return user.profile.rank == 'knight'

@login_required
@user_passes_test(is_k9)
def area_list(request):
    areas = Area.objects.all()
    return render(request, 'structure/area_list.html', {'areas': areas})

@login_required
@user_passes_test(is_k9)
def add_area(request):
    if request.method == 'POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oblast byla úspěšně přidána.')
            return redirect('area_list')
    else:
        form = AreaForm()
    return render(request, 'structure/area_form.html', {'form': form})

@login_required
@user_passes_test(is_k9)
def edit_area(request, area_id):
    area = get_object_or_404(Area, id=area_id)
    if request.method == 'POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            messages.success(request, 'Oblast byla úspěšně aktualizována.')
            return redirect('area_list')
    else:
        form = AreaForm(instance=area)
    return render(request, 'structure/area_form.html', {'form': form, 'area': area})

@login_required
@user_passes_test(is_komtur)
def commandery_detail(request):
    commandery = get_object_or_404(Commandery, komtur=request.user)
    return render(request, 'structure/commandery_detail.html', {'commandery': commandery})
