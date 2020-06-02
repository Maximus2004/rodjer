from django.shortcuts import render, redirect
from trone.forms import DuoForm, PraksForm, SquadsForm


def main_list(request):
    return render(request, 'relevant_info.html')


def past_list(request):
    return render(request, 'past.html')


# как работает оплата турнирв
def how_works(request):
    return render(request, 'how_works.html')


# информация по пракам
def info_praks(request):
    return render(request, 'praks.html')


# успешное прохождение регистрации на праки
def success_praks(request):
    return render(request, 'success_praks.html')


# успешное прохождение регистрации на бесплатный турик
def success(request):
    return render(request, 'success.html')


# регистрация сквада на праки
def reg_praks(request):
    if request.method == "POST":
        form = PraksForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('success_praks')
    else:
        form = PraksForm()
    return render(request, 'praks_reg.html', {'form': form})


# регистрация сквадов на бесплатный турнир
def squads_reg(request):
    if request.method == "POST":
        form = SquadsForm(request.POST)
        if form.is_valid():
            squad = form.save(commit=False)
            squad.save()
            return redirect('success')
    else:
        form = SquadsForm()
    return render(request, 'reg_squads.html', {'form': form})


def duo_reg(request):
    if request.method == "POST":
        form = DuoForm(request.POST)
        if form.is_valid():
            duo = form.save(commit=False)
            duo.save()
            return redirect('success')
    else:
        form = DuoForm()
    return render(request, 'reg_duo.html', {'form': form})
