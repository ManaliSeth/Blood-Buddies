from wtforms import *

class ComplainVO:
    complainId = IntegerField
    complainSubject = StringField
    complainDescription = StringField
    datasetname = StringField
    datasetpath = StringField
    complainFrom_LoginId = IntegerField
    complainTo_LoginId = IntegerField
    complainDate = StringField
    complainTime = StringField
    replyDate = StringField
    replyTime = StringField
    complainStatus = StringField
