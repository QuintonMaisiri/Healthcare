from django.shortcuts import render
from django.http import JsonResponse , HttpResponse , QueryDict
from .models import Account,Doctor,Patient,PatientRecord,Review,Next_of_kin
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return JsonResponse({"msg":"HEllo appointment"})

# Doctor API Start
@csrf_exempt
def doctors(request):
    if (request.method == "POST"):
        account = Account(
            username = request.POST["username"],
            password = request.POST["password"],
            type = "D"
        )
        account.save()

        doctor = Doctor(
            fname = request.POST["fname"],
            lname = request.POST["lname"],
            email = request.POST["email"],
            phone = request.POST["phone"],
            gender = request.POST["gender"],
            username = account
            )
        doctor.save()
        return HttpResponse("Successful")
    elif request.method == "DELETE":
        doctor.objects.all().delete()
        return HttpResponse("Successful")
    else:
        data = Doctor.objects.values()
        return JsonResponse(list(data), safe=False)

@csrf_exempt
def doctor(request,id): 
    data = Doctor.objects.filter(id = id).values()

    if request.method == "GET":
        return JsonResponse(list(data), safe=False)
    elif request.method == "DELETE":
        Doctor.objects.get(id= id).delete()
        return HttpResponse("successful")
    elif request.method == "PUT":
        put = QueryDict(request.body)

        doctor = Doctor.objects.get(id = id)
        list_data = list(data)
        for key in list_data[0].keys():
            if key == "username_id" or key == "id" or key ==  "person_ptr_id":
                pass
            else:
                setattr(doctor,key,put.get(key))
        doctor.save()
        return HttpResponse("Successful")

#Doctor API end

#Patient API start
@csrf_exempt
def patients(request):
    if (request.method == "POST"):
        account = Account(
            username = request.POST["username"],
            password = request.POST["password"],
            type = "P"
        )
        account.save()

        nok = Next_of_kin(
            fname = request.POST["next_of_kin_fname"],
            lname = request.POST["next_of_kin_lname"],
            email = request.POST["next_of_kin_email"],
            phone = request.POST["next_of_kin_phone"],
        )
        nok.save()

        patient = Patient(
            fname = request.POST["fname"],
            lname = request.POST["lname"],
            email = request.POST["email"],
            phone = request.POST["phone"],
            gender = request.POST["gender"],
            username = account,
            address = request.POST["address"],
            next_of_kin = nok
            )
        patient.save()
        return HttpResponse("Successful")
    elif request.method == "DELETE":
        Patient.objects.all().delete()
        return HttpResponse("Successful")
    else:
        data = Patient.objects.values()
        return JsonResponse(list(data), safe=False)
    
@csrf_exempt
def patient(request,id):
    data = Patient.objects.filter(id = id).values()

    if request.method == "GET":
        return JsonResponse(list(data), safe=False)
    elif request.method == "DELETE":
        Patient.objects.get(id= id).delete()
        return HttpResponse("successful")
    elif request.method == "PUT":
        put = QueryDict(request.body)

        patient = Patient.objects.get(id = id)
       
        list_data = list(data)
        for key in list_data[0].keys():
            if key == "username_id" or key == "id" or key == "person_ptr_id" or key == "next_of_kin_id":
                pass
            else:
                setattr(patient,key,put.get(key))
        patient.save()
        
        nok = Next_of_kin.objects.get(id = patient.next_of_kin.id)
        nok_data =  Next_of_kin.objects.filter(id = nok.id).values()
        list_nok_data =list(nok_data)

        for key in list_nok_data[0].keys():
            if key == "id":
                pass
            else:
                setattr(nok,key,put.get(f"next_of_kin_{key}"))
        nok.save()
        
        return HttpResponse("Successful")

#Patient API end

#Patient Records API start
@csrf_exempt
def records(request):
    if (request.method == "POST"):

        patient = Patient.objects.get(id = request.POST["patient_id"])
        doctor = Doctor.objects.get(id = request.POST["doctor_id"])

        record = PatientRecord(
            patient = patient,
            doctor = doctor,
            details = request.POST["details"]
            )
        record.save()
        return HttpResponse("Successful")
    
    elif request.method == "DELETE":
        PatientRecord.objects.all().delete()
        return HttpResponse("Successful")
    else:
        data = PatientRecord.objects.values()
        return JsonResponse(list(data), safe=False)
    
@csrf_exempt
def record_patient(request,patient_id):
    data = PatientRecord.objects.filter(patient_id = patient_id).values()

    if request.method == "GET":
        return JsonResponse(list(data), safe=False)
    elif request.method == "DELETE":
        Patient.objects.all().delete()
        return HttpResponse("successful")
    
@csrf_exempt
def record_doctor(request,doctor_id):
    data = PatientRecord.objects.filter(doctor_id = doctor_id).values()

    if request.method == "GET":
        return JsonResponse(list(data), safe=False)
    elif request.method == "DELETE":
        Patient.objects.all().delete()
        return HttpResponse("successful")
    
@csrf_exempt
def record(request,id):
    data = PatientRecord.objects.filter(id = id).values()

    if request.method == "GET":
        return JsonResponse(list(data), safe=False)
    elif request.method == "DELETE":
        PatientRecord.objects.get(id= id).delete()
        return HttpResponse("successful")
    elif request.method == "PUT":
        put = QueryDict(request.body)

        record = PatientRecord.objects.get(id = id)
       
        list_data = list(data)
        for key in list_data[0].keys():
            if key == "id" or key == "doctor_id" or key == "patient_id":
                pass
            else:
                setattr(record,key,put.get(key))
        record.save()
        return HttpResponse("Successful")


  
#Patient Records API end

#Account API start

@csrf_exempt
def account(request,id):
    if request.method == "PUT":
        account = Account.objects.get(id=id)

        put = QueryDict(request.body)
        account.username = put.get("username")
        account.password = put.get("password")

        account.save()
        return HttpResponse("Successful")  
    


#Account API end

#Doctor Review API start

@csrf_exempt
def reviews(request):
    if (request.method == "POST"):

        patient = Patient.objects.get(id = request.POST["patient_id"])
        doctor = Doctor.objects.get(id = request.POST["doctor_id"])

        review = Review(
            patient = patient,
            doctor = doctor,
            comment = request.POST["comment"],
            rating = request.POST["rating"]
            )
        review.save()
        return HttpResponse("Successful")
    
    elif request.method == "DELETE":
        Review.objects.all().delete()
        return HttpResponse("Successful")
    else:
        data = Review.objects.values()
        return JsonResponse(list(data), safe=False)
    
    
@csrf_exempt
def review_doctor(request,doctor_id):
    data = Review.objects.filter(doctor_id = doctor_id).values()

    if request.method == "GET":
        return JsonResponse(list(data), safe=False)
    elif request.method == "DELETE":
        Review.objects.filter(doctor_id = doctor_id).delete()
        return HttpResponse("successful")
    
@csrf_exempt
def review(request,id):
    data = Review.objects.filter(id = id).values()

    if request.method == "GET":
        return JsonResponse(list(data), safe=False)
    elif request.method == "DELETE":
        Review.objects.get(id= id).delete()
        return HttpResponse("successful")

#Doctor review API end



