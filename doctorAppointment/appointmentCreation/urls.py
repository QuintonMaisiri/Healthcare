from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("doctor",views.doctors, name="doctors"),
    path("doctor/<str:id>",views.doctor,name="doctor"),
    path("patient",views.patients, name="patients"),
    path("patient/<str:id>",views.patient,name="patient"),
    path("record",views.records, name="records"),
    path("record-patient/<str:patient_id>",views.record_patient,name="record_patient"),
    path("record-doctor/<str:doctor_id>",views.record_doctor,name="record_doctor"),
    path("record/<str:id>",views.record,name="record"),
    path("account/<str:id>",views.account,name="account"),
    path("review",views.reviews, name="reviews"),
    path("review/<str:id>",views.review, name="review"),
     path("review-doctor/<str:doctor_id>",views.review_doctor,name="review_doctor"),
]