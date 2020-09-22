from django.shortcuts import render, redirect
from .forms import SeasonForm, CurrentSeasonForm
from django.contrib import messages
from .functions import InitializeOtherSeasonValues
from StudentManager.models import Seasons, Students, CurrentSeason
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def createSeason(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            Season = str(form.cleaned_data['SeasonName'])
            if Seasons.objects.filter(SeasonName=Season).exists():
                message = "Operation Failed!: Season Name already exists. Try using another name."
            else:
                form.save()
                message = InitializeOtherSeasonValues(Season)
                message = "Season Creation " + message
                if "Failed" in message:
                    messages.error(request, message)
                else:
                    messages.success(request, message)
            form = SeasonForm()
            return render(request, 'createSeason.html', {'form': form})
    else:
        form = SeasonForm()
        print(form)
    return render(request, 'createSeason.html', {'form': form})

@login_required(login_url='login')
def changeCurrentSeason(request):
    message=""
    currentseason = CurrentSeason.objects.get(pk=1)
    form = CurrentSeasonForm(instance=currentseason)
    if request.method == 'POST':
        form = CurrentSeasonForm(request.POST or None, request.FILES or None, instance=currentseason)
        if form.is_valid():
            form.save()
            seasonName = str(form.cleaned_data['Season'])
            message = InitializeOtherSeasonValues(seasonName)
            if "Failed" in message:
                messages.error(request, message)
            else:
                messages.success(request, message)
            return redirect("Manager-changeCurrentSeason")
    else:
        form = CurrentSeasonForm(instance=currentseason)
    return render(request, 'changeCurrentSeason.html', {'form': form})

def viewSettings(request):
    currentSeason = CurrentSeason.objects.get(pk=1)
    season = currentSeason.Season
    return render(request, 'viewSettings.html', {'season': season})