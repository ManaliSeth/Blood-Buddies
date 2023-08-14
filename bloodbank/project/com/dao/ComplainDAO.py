from project.com.dao import *


class ComplainDAO:

    def userAddComplain(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "insert into ComplainMaster(complainSubject,complainDescription,datasetname,datasetpath,complainFrom_LoginId,complainTo_LoginId,complainDate,complainTime,complainStatus) values ('" + complainVO.complainSubject + "','" + complainVO.complainDescription + "','" + complainVO.datasetname + "','" + complainVO.datasetpath + "','" + str(complainVO.complainFrom_LoginId) + "','" + str(complainVO.complainTo_LoginId) + "','" + complainVO.complainDate + "','" + complainVO.complainTime + "','" + complainVO.complainStatus + "')")
        connection.commit()
        cursor.close()
        connection.close()

    def getComplainTo_LoginId(self,bloodbankId):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("select bloodbank_LoginId from BloodbankMaster where bloodbankId = '"+bloodbankId+"'  ")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def userViewUserComplain(self,complainVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor1.execute("select loginId,loginEmail from LoginMaster L inner join ComplainMaster C where L.loginId = C.complainTo_LoginId and C.complainFrom_LoginId ='"+str(complainVO.complainFrom_LoginId)+"' ")
        dict1 = cursor1.fetchall()
        cursor2.execute("Select * from ComplainMaster C inner join LoginMaster L where L.loginId = C.complainFrom_LoginId and C.complainFrom_LoginId ='"+str(complainVO.complainFrom_LoginId)+"'  ")
        dict2 = cursor2.fetchall()
        cursor1.close()
        cursor2.close()
        connection.close()
        return dict1,dict2

    def getComplainFrom_LoginId(self,complainVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor1.execute("select complainFrom_LoginId from ComplainMaster  where complainTo_LoginId = '"+str(complainVO.complainTo_LoginId)+"' ")
        dict1 = cursor1.fetchall()
        connection.close()
        return dict1


    def getLoginEmail(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("select DISTINCT(loginEmail),complainFrom_LoginId from   ComplainMaster C inner join LoginMaster L where C.complainFrom_LoginId = L.loginID and C.complainFrom_LoginId = '"+str(complainVO.complainFrom_LoginId)+"'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def bloodbankViewUserComplain(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("Select * from ComplainMaster where complainTo_LoginId ='"+str(complainVO.complainTo_LoginId)+"' and complainStatus='pending'")
        dict1 = cursor.fetchall()
        cursor.close()
        connection.close()
        return dict1

    # def adminViewUserComplain(self):
    #     connection = conn_db()
    #     dict1 = ()
    #     cursor = connection.cursor()
    #     cursor.execute("Select * from ComplainMaster C inner join LoginMaster L where L.loginId = C.complainFrom_LoginId and L.loginRole = 'user'")
    #     dict1 = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return dict1

    def bloodbankAddComplain(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute(
            "insert into ComplainMaster(complainSubject,complainDescription,datasetname,datasetpath,complainFrom_LoginId,complainTo_LoginId,complainDate,complainTime,complainStatus) values ('" + complainVO.complainSubject + "','" + complainVO.complainDescription + "','" + complainVO.datasetname + "','" + complainVO.datasetpath + "','" + str(complainVO.complainFrom_LoginId) + "','" + str(complainVO.complainTo_LoginId) + "','" + complainVO.complainDate + "','" + complainVO.complainTime + "','" + complainVO.complainStatus + "')")
        connection.commit()
        cursor.close()
        connection.close()

    def bloodbankViewBloodbankComplain(self,complainVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor1.execute("select loginId,loginEmail from LoginMaster L inner join ComplainMaster C where L.loginId = C.complainTo_LoginId and C.complainFrom_LoginId ='"+str(complainVO.complainTo_LoginId)+"' ")
        dict1 = cursor1.fetchall()
        cursor2.execute("Select * from ComplainMaster C inner join LoginMaster L where L.loginId = C.complainFrom_LoginId and C.complainFrom_LoginId ='"+str(complainVO.complainFrom_LoginId)+"'  ")
        dict2 = cursor2.fetchall()
        connection.commit()
        cursor1.close()
        cursor2.close()
        connection.close()
        return dict1,dict2

    def adminViewBloodbankComplain(self):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("Select * from ComplainMaster C inner join LoginMaster L where L.loginId = C.complainFrom_LoginId and L.loginRole = 'bloodbank' and C.complainStatus='pending'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def getBloodbankComplaintDetails(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("select * from ComplainMaster where complainId = '"+str(complainVO.complainId)+"'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1


    def adminReplyBloodbankComplain(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("update ComplainMaster set complainStatus = '"+complainVO.complainStatus+"', replyDescription ='"+complainVO.replyDescription+"' ,replyDate = '"+complainVO.replyDate+"',replyTime = '"+complainVO.replyTime+"' where complainId = '"+str(complainVO.complainId)+"' ")
        connection.commit()
        cursor.close()
        connection.close()

    def getUserComplaintDetails(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("select * from ComplainMaster where complainId = '"+str(complainVO.complainId)+"'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def bloodbankReplyUserComplain(self,complainVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("update ComplainMaster set complainStatus = '"+complainVO.complainStatus+"', replyDescription ='"+complainVO.replyDescription+"' ,replyDate = '"+complainVO.replyDate+"',replyTime = '"+complainVO.replyTime+"' where complainId = '"+str(complainVO.complainFrom_LoginId)+"' ")
        connection.commit()
        cursor.close()
        connection.close()

