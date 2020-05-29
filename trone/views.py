from django.shortcuts import render, redirect
from trone.forms import EasyForm, EasyForm2, PayForm


def main_list(request):
    return render(request, 'relevant_info.html')


def past_list(request):
    return render(request, 'past.html')


def how_works(request):
    return render(request, 'how_works.html')


def success(request):
    return render(request, 'success.html')


def success_pay(request):
    return render(request, 'success_pay.html')


def easy_reg(request):
    if request.method == "POST":
        form = EasyForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('success')
    else:
        form = EasyForm()
    return render(request, 'easy_reg.html', {'form': form})


def easy_reg2(request):
    if request.method == "POST":
        form = EasyForm2(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('success')
    else:
        form = EasyForm2()
    return render(request, 'easy_reg2.html', {'form': form})


def pay(request):
    if request.method == "POST":
        form = PayForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('success_pay')
    else:
        form = PayForm()
    return render(request, 'payment.html', {'form': form})
