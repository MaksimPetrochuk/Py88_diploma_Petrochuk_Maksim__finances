from django.shortcuts import render, redirect
from .forms import ConsumerSignUpForm, ConsumerSignInForm

def sign_in(request):
    if request.method == 'POST':
        form = ConsumerSignInForm(request.POST)
        if form.is_valid():
            import os, sys
            sys.path.append('/home/mk/Desktop/Py88_diploma_Petrochuk_Maksim__finances/finances')
            os.environ['DJANGO_SETTINGS_MODULE'] = 'finances.settings'
            import django
            django.setup()

            conn = psycopg2.connect(database="finances", user="finances_admin", password="peklo5gd!", host="localhost")
            cursor = conn.cursor()

            cursor.execute(
                SELECT * FROM
            )

            conn.commit()
            conn.close()
            return redirect('profile')
    else:
        form = ConsumerSignInForm()

    response = {
        'form': form,
    }
    return render(request, 'consumer/sign_in.html', response)


def sign_up(request):
    error = ''
    if request.method == 'POST':
        form = ConsumerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign_in')
    else:
        error = 'Incorrect form'
        form = ConsumerSignUpForm()

    response = {
        'form': form,
        'error': error,
    }

    return render(request, 'consumer/sign_up.html', response)



def profile(request):
    return render(request, 'consumer/profile.html')


def create_cost_group(request):
    return render(request, 'consumer/create_cost_group.html')


def create_cost_record(request):
    return render(request, 'consumer/create_cost_record.html')