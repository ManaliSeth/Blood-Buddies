from wtforms import *


class BloodbankVO:
    bloodbankId = IntegerField
    bloodbank_AreaId = IntegerField
    bloodbankName = StringField
    bloodbankAddress = StringField
    bloodbankPinCode = IntegerField
    bloodbankDescription = StringField
    bloodbankContactNumber = StringField
    bloodbankRegistrationDate = StringField
    bloodbank_LoginId = IntegerField
