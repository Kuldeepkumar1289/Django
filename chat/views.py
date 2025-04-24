from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Chat, Feedback
from main_app.views import patient_ui, doctor_ui
from main_app.models import patient, doctor


def post_feedback(request):
    if request.method == "POST":

        feedback = request.POST.get('feedback', None)
        if feedback != '':
            f = feedback(sender=request.user, feedback=feedback)
            f.savee()

        try:
            if (request.user.patient.is_patient == True):
                return HttpResponse("Feedback successfully sent.")
        except:
            pass
        if (request.user.doctor.is_doctor == True):
            return HttpResponse("Feedback successfully sent.")

    else:

        return HttpResponse("Feedback field is empty. ")


def get_feedback(request):
    if request.method == "GET":
        obj = Feedback.objects.all()

        return redirect(request, 'consulation/chat_body.html', {"obj": obj})