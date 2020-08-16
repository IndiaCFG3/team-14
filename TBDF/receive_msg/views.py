from django.shortcuts import render
import requests
import twillio_rec


def button(request):
    twilio_rec.py
    return render(request,'home.html')

def output(request):
    if request.method == 'POST' and 'run_script' in request.POST:

    # import function to run

    # call function
        exec(open("twillio_rec.py").read())

        # return user to required page
        print('done')
    return render(request,'home.html')

