from project.com.dao import *

class AppointmentDAO:


    def getAreaId(self,appointmentVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("select bloodbank_AreaId from BloodbankMaster where bloodbank_AreaId = '"+str(appointmentVO.appointment_BloodbankId)+"'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def userInsertAppointmentDetails(self,appointmentVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "insert into AppointmentMaster(appointment_LoginId,appointment_AreaId,appointment_BloodbankId,appointmentType,appointmentDate,appointmentTime,lastDonationDate,bloodGroupType,messageDescription,appointmentStatus) values ('" + str(appointmentVO.appointment_LoginId) + "','" + str(appointmentVO.appointment_AreaId) + "','" + str(appointmentVO.appointment_BloodbankId) + "','" + appointmentVO.appointmentType + "','" + appointmentVO.appointmentDate + "','" + appointmentVO.appointmentTime + "','" + appointmentVO.lastDonationDate + "','" + appointmentVO.bloodGroupType + "','" + appointmentVO.messageDescription + "','" + appointmentVO.appointmentStatus + "')")
        connection.commit()
        cursor.close()
        connection.close()

    def getAppointmentTo_LoginId(self,appointmentVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("select appointment_BloodbankId from AppointmentMaster where appointment_LoginId = '"+str(appointmentVO.appointment_LoginId)+"'  ")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def getBloodbankName(self,appointmentVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("select bloodbankName,bloodbank_LoginId from BloodbankMaster B inner join AppointmentMaster A where A.appointment_BloodbankId = '"+str(appointmentVO.appointment_BloodbankId)+"'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def userViewUserAppointment(self,appointmentVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor1.execute("select * from AppointmentMaster A where appointment_LoginId = '"+str(appointmentVO.appointment_LoginId)+"' ")
        dict1 = cursor1.fetchall()
        connection.commit()
        cursor1.close()
        connection.close()
        return dict1

    def bloodbankViewUserAppointment(self,bloodbankVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("Select bloodbankId from bloodbankmaster where bloodbank_LoginId='"+str(bloodbankVO.bloodbank_LoginId)+"'")
        dict1 = cursor.fetchall()
        print(dict1)
        appointment_BloodbankId=dict1[0]['bloodbankId']
        print("appointment_BloodbankId=",appointment_BloodbankId)


        cursor2 = connection.cursor()
        cursor2.execute("select * from AppointmentMaster where appointment_BloodbankId =  '"+str(appointment_BloodbankId)+"' and  appointmentStatus='pending'")
        dict2 = cursor2.fetchall()
        print(dict2)

        connection.commit()
        cursor.close()
        cursor2.close()
        connection.close()
        return dict2

    def getLoginEmail(self,appointment_LoginId):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("select loginId,loginEmail from LoginMaster where loginId = '"+str(appointment_LoginId)+"'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1


    def updateUserAppointment(self,appointmentVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("Update AppointmentMaster set appointmentStatus ='"+appointmentVO.appointmentStatus+"' where appointmentId ='"+str(appointmentVO.appointmentId)+"'")
        connection.commit()
        cursor.close()
        connection.close()