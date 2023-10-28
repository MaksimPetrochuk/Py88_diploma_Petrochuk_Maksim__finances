from django.shortcuts import render


def sign_in(request):
    return render(request, 'consumer/sign_in.html')


def sign_up(request):
    return render(request, 'consumer/sign_up.html')


def profile(request):
    return render(request, 'consumer/profile.html')


def create_cost_group(request):
    return render(request, 'consumer/create_cost_group.html')


def create_cost_record(request):
    return render(request, 'consumer/create_cost_record.html')