from wtforms import *

class LoginVO:

    loginId = IntegerField
    loginUsername = StringField
    loginPassword = StringField
    loginRole = StringField