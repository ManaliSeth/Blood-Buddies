from project.com.dao import conn_db


class UserDAO:

    def insertUser(self, userVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("Select max(loginId) as loginId from LoginMaster")
        dict1 = cursor.fetchone()
        print(dict1)
        userVO.user_LoginId = str(dict1['loginId'])
        cursor.execute(
            "insert into UserMaster(userFirstName,userLastName,userAddress,userGender,userDateOfBirth,userContactNumber,userBloodGroup,user_LoginId,userStatus) values ('" + userVO.userFirstName + "','" + userVO.userLastName + "','" + userVO.userAddress + "','" + userVO.userGender + "','" + userVO.userDateOfBirth + "','" + userVO.userContactNumber + "','" + userVO.userBloodGroup + "','" + userVO.user_LoginId + "','" + userVO.userStatus + "')")
        connection.commit()
        cursor.close()
        connection.close()


    def userDeleteUser(self,userVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute(
            "Select * from UserMaster where user_LoginId = '" + str(userVO.loginId) + "'")
        dict1=cursor.fetchall()
        print(dict1)
        cursor.execute("update UserMaster set userStatus='deactive' where user_LoginId = '"+str(dict1[0]['user_LoginId'])+"'")
        connection.commit()
        cursor.close()
        connection.close()


    def userEditUser(self, userVO):
        connection = conn_db()
        cursor1 = connection.cursor()

        cursor1.execute(
                    "Select * from UserMaster where user_LoginId = '"+str(userVO.loginId)+"'")

        dict1 = cursor1.fetchall()

        cursor1.close()
        connection.close()

        return dict1


    def userUpdateUser(self, userVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update UserMaster set userFirstName ='{}',userLastName = '{}',userAddress = '{}', userGender = '{}',userDateOfBirth = '{}',userContactNumber = '{}',userBloodGroup = '{}' where userId = '{}'".format(
                userVO.userFirstName, userVO.userLastName,userVO.userAddress,
                userVO.userGender, userVO.userDateOfBirth, userVO.userContactNumber,
                userVO.userBloodGroup,userVO.userId))
        connection.commit()
        cursor.close()
        connection.close()



    def adminViewUser(self):
        connection = conn_db()

        dict1 = ()
        cursor = connection.cursor()
        cursor.execute("Select * from UserMaster U inner join LoginMaster L where L.loginId = U.user_LoginId and userStatus = 'active' ")
        dict1 = cursor.fetchall()

        cursor.close()
        connection.close()

        return dict1


    def adminDeleteUser(self, userVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("update UserMaster set userStatus='deactive' where userId = '{}'".format(userVO.userId))
        connection.commit()
        cursor.close()
        connection.close()


    def adminEditUser(self, userVO):
        connection = conn_db()
        cursor1 = connection.cursor()

        cursor1.execute("Select * from UserMaster where userId = '{}'".format(userVO.userId))
        dict1 = cursor1.fetchall()

        cursor1.close()
        connection.close()

        return dict1


    def adminUpdateUser(self, userVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update UserMaster set userFirstName ='{}',userLastName = '{}',userAddress = '{}', userGender = '{}',userDateOfBirth = '{}',userContactNumber = '{}',userBloodGroup = '{}' where userId = '{}'".format(
                userVO.userFirstName, userVO.userLastName,userVO.userAddress,
                userVO.userGender, userVO.userDateOfBirth, userVO.userContactNumber,
                userVO.userBloodGroup,userVO.userId))
        connection.commit()
        cursor.close()
        connection.close()



    def bloodbankViewUser(self):
        connection = conn_db()
        dict1 = ()
        cursor = connection.cursor()
        cursor.execute("Select * from UserMaster U inner join LoginMaster L where L.loginId = U.user_LoginId and userStatus = 'active'")
        dict1 = cursor.fetchall()

        cursor.close()
        connection.close()

        return dict1


    def bloodbankDeleteUser(self, userVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("update UserMaster set userStatus='deactive' where userId = '{}'".format(userVO.userId))
        connection.commit()
        cursor.close()
        connection.close()


    def bloodbankEditUser(self, userVO):
        connection = conn_db()
        cursor1 = connection.cursor()

        cursor1.execute("Select * from UserMaster where userId = '{}'".format(userVO.userId))
        dict1 = cursor1.fetchall()

        cursor1.close()
        connection.close()

        return dict1


    def bloodbankUpdateUser(self, userVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "update UserMaster set userFirstName ='{}',userLastName = '{}',userAddress = '{}', userGender = '{}',userDateOfBirth = '{}',userContactNumber = '{}',userBloodGroup = '{}' where userId = '{}'".format(
                userVO.userFirstName, userVO.userLastName,userVO.userAddress,
                userVO.userGender, userVO.userDateOfBirth, userVO.userContactNumber,
                userVO.userBloodGroup,userVO.userId))
        connection.commit()
        cursor.close()
        connection.close()


