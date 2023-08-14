from wtforms import *

class AppointmentVO:
    appointmentId = IntegerField
    appointment_LoginId = IntegerField
    appointment_AreaId = IntegerField
    appointment_BloodbankId = IntegerField
    appointmentType = StringField
    appointmentDate = StringField
    appointmentTime = StringField
    lastDonationDate = StringField
    bloodGroupType = StringField
    messageDescription = StringField
    appointmentStatus = StringField