from project.com.dao import conn_db


class BloodbankDAO:

    def userViewBloodbank(self,userPincode):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor1.execute("Select * from BloodbankMaster where bloodbankPincode='"+userPincode+"'")
        dict1 = cursor1.fetchall()
        print(dict1)
        cursor2 = connection.cursor()
        cursor2.execute("select areaId,areaName from BloodbankMaster B inner join AreaMaster A where B.bloodbank_AreaId = A.areaId and B.bloodbankPincode='"+userPincode+"' ")
        dict2 = cursor2.fetchall()
        print(dict2)
        connection.commit()
        cursor1.close()
        cursor2.close()
        connection.close()
        return dict1,dict2

    def insertBloodbank(self, bloodbankVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()

        cursor1.execute("Select max(loginId) as loginId from LoginMaster")
        dict1 = cursor1.fetchone()
        print(dict1)
        bloodbankVO.bloodbank_LoginId = str(dict1['loginId'])

        cursor2.execute("select areaId from AreaMaster where areaId = '" + bloodbankVO.bloodbank_AreaId + "' ")
        dict2 = cursor2.fetchone()
        print(dict2)
        bloodbankVO.areaId = str(dict2['areaId'])

        cursor2.execute(
            "insert into BloodbankMaster(bloodbank_AreaId,bloodbankName,bloodbankAddress,bloodbankPincode,bloodbankDescription,bloodbankContactNumber,bloodbankRegistrationDate,bloodbank_LoginId,bloodbankStatus) values ('" + bloodbankVO.bloodbank_AreaId + "','" + bloodbankVO.bloodbankName + "','" + bloodbankVO.bloodbankAddress + "','" + bloodbankVO.bloodbankPinCode + "','" + bloodbankVO.bloodbankDescription + "','" + bloodbankVO.bloodbankContactNumber + "','" + bloodbankVO.bloodbankRegistrationDate + "','" + bloodbankVO.bloodbank_LoginId + "','" +bloodbankVO.bloodbankStatus+ "')")
        connection.commit()
        cursor1.close()
        cursor2.close()
        connection.close()

    def bloodbankDeleteBloodbank(self,bloodbankVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute(
            "Select * from BloodbankMaster where bloodbank_LoginId = '" + str(bloodbankVO.loginId) + "'")
        dict1=cursor.fetchall()
        print(dict1)
        cursor.execute("update BloodbankMaster set bloodbankStatus='deactive' where bloodbank_LoginId = '"+str(dict1[0]['bloodbank_LoginId'])+"'")
        connection.commit()
        cursor.close()
        connection.close()


    def bloodbankEditBloodbank(self, bloodbankVO):
        connection = conn_db()
        cursor1 = connection.cursor()

        cursor1.execute(
                    "Select * from BloodbankMaster where bloodbank_LoginId = '"+str(bloodbankVO.loginId)+"'")

        dict1 = cursor1.fetchall()

        cursor1.close()
        connection.close()

        return dict1


    def bloodbankUpdateBloodbank(self, bloodbankVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update BloodbankMaster set bloodbankName ='{}',bloodbankAddress = '{}',bloodbankPincode = '{}', bloodbankDescription = '{}',bloodbankContactNumber = '{}',bloodbankRegistrationDate = '{}' where bloodbankId = '{}'".format(
                bloodbankVO.bloodbankName, bloodbankVO.bloodbankAddress,
                bloodbankVO.bloodbankPinCode, bloodbankVO.bloodbankDescription, bloodbankVO.bloodbankContactNumber,
                bloodbankVO.bloodbankRegistrationDate,bloodbankVO.bloodbankId))
        connection.commit()
        cursor.close()
        connection.close()


    def adminViewBloodbank(self):
        connection = conn_db()

        dict1 = ()
        cursor = connection.cursor()

        cursor.execute("Select * from BloodbankMaster B inner join LoginMaster L where L.loginId = B.bloodbank_LoginId and bloodbankStatus = 'active'")

        dict1 = cursor.fetchall()

        cursor.close()
        connection.close()

        return dict1

    def adminDeleteBloodbank(self, bloodbankVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("update BloodbankMaster set bloodbankStatus = 'deactive' where bloodbankId = '{}'".format(bloodbankVO.bloodbankId))
        connection.commit()
        cursor.close()
        connection.close()

    def adminEditBloodbank(self, bloodbankVO):
        connection = conn_db()
        cursor1 = connection.cursor()

        cursor1.execute("Select * from BloodbankMaster where bloodbankId = '{}'".format(bloodbankVO.bloodbankId))
        dict1 = cursor1.fetchall()

        cursor1.close()
        connection.close()

        return dict1

    def adminUpdateBloodbank(self, bloodbankVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update BloodbankMaster set bloodbankName ='{}',bloodbankAddress = '{}',bloodbankPincode = '{}', bloodbankDescription = '{}',bloodbankContactNumber = '{}',bloodbankRegistrationDate = '{}' where bloodbankId = '{}'".format(
                bloodbankVO.bloodbankName, bloodbankVO.bloodbankAddress,
                bloodbankVO.bloodbankPinCode, bloodbankVO.bloodbankDescription, bloodbankVO.bloodbankContactNumber,
                bloodbankVO.bloodbankRegistrationDate,bloodbankVO.bloodbankId))
        connection.commit()
        cursor.close()
        connection.close()


    def getUserCount(self):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("select ")
