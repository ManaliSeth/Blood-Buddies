from project.com.dao import *


class LoginDAO:

    def insertLogin(self,loginVO):

        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("insert into LoginMaster(loginEmail,loginPassword,loginRole) values('"+loginVO.loginEmail+"','"+loginVO.loginPassword+"','"+loginVO.loginRole+"')")
        loginDict = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return loginDict

    def searchLogin(self,loginVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "select * from LoginMaster where loginEmail = '"+loginVO.loginEmail+"' and loginPassword = '"+loginVO.loginPassword+"' ")
        loginDict = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return loginDict


    def checkLoginEmail(self,loginVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "select loginEmail from LoginMaster where loginEmail = '" + loginVO.loginEmail + "' ")
        loginDict = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return loginDict

    def updatePassword(self,loginVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update LoginMaster set loginPassword = '"+loginVO.loginPassword+"' where loginEmail = '" + loginVO.loginEmail + "' ")

        connection.commit()
        cursor.close()
        connection.close()

    def getCurrentPassword(self,loginVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "select * from LoginMaster where loginPassword = '" + str(loginVO.oldPassword) + "' ")

        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def setNewPassword(self,loginVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update LoginMaster set loginPassword = '"+loginVO.newPassword+"' where loginPassword = '" + loginVO.oldPassword + "' ")

        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1


