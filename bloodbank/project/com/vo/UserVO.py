from wtforms import *


class UserVO:
    userId = IntegerField
    userFirstName = IntegerField
    userLastName = StringField
    userAddress = StringField
    userGender = StringField
    userDateOfBirth = StringField
    userContactNumber = IntegerField
    userBloodGroup = StringField
    user_LoginId = IntegerField
