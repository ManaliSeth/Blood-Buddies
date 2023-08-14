from project.com.dao import *

class FeedbackDAO:

    def userAddFeedback(self,feedbackVO):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute(
            "insert into FeedbackMaster(feedbackRating,feedbackDescription,feedbackFrom_LoginId,feedbackTo_LoginId,feedbackDate,feedbackTime) values ('" + feedbackVO.feedbackRating + "','" + feedbackVO.feedbackDescription + "','" + str(feedbackVO.feedbackFrom_LoginId) + "','" + str(feedbackVO.feedbackTo_LoginId) + "','" + feedbackVO.feedbackDate + "','" + feedbackVO.feedbackTime + "')")
        connection.commit()
        cursor.close()
        connection.close()

    def getFeedbackTo_LoginId(self,bloodbankId):
        connection = conn_db()
        cursor = connection.cursor()

        cursor.execute("select bloodbank_LoginId from BloodbankMaster where bloodbankId = '"+bloodbankId+"'  ")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def getFeedbackFrom_LoginId(self,feedbackVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor1.execute("select feedbackFrom_LoginId from FeedbackMaster  where feedbackTo_LoginId = '"+str(feedbackVO.feedbackTo_LoginId)+"' ")
        dict1 = cursor1.fetchall()
        connection.close()
        return dict1


    def getLoginEmail(self,feedbackVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("select DISTINCT(loginEmail),feedbackFrom_LoginId from FeedbackMaster F inner join LoginMaster L where F.feedbackFrom_LoginId = L.loginID and F.feedbackFrom_LoginId = '"+str(feedbackVO.feedbackFrom_LoginId)+"'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1


    def userViewUserFeedback(self,feedbackVO):
        connection = conn_db()
        cursor1 = connection.cursor()
        cursor2 = connection.cursor()
        cursor1.execute("select loginId,loginEmail from LoginMaster L inner join FeedbackMaster F where L.loginId = F.feedbackTo_LoginId and F.feedbackFrom_LoginId ='"+str(feedbackVO.feedbackFrom_LoginId)+"' ")
        dict1 = cursor1.fetchall()
        cursor2.execute("Select * from FeedbackMaster F inner join LoginMaster L where L.loginId = F.feedbackFrom_LoginId and F.feedbackFrom_LoginId ='"+str(feedbackVO.feedbackFrom_LoginId)+"'  ")
        dict2 = cursor2.fetchall()
        cursor1.close()
        cursor2.close()
        connection.close()
        return dict1,dict2

    def bloodbankViewUserFeedback(self,feedbackVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute(
            "select * from FeedbackMaster where feedbackTo_LoginId = '" + str(feedbackVO.feedbackTo_LoginId) + "'")
        dict1 = cursor.fetchall()
        connection.commit()
        cursor.close()
        return dict1

    # def adminViewUserFeedback(self):
    #     connection = conn_db()
    #     dict1 = ()
    #     cursor = connection.cursor()
    #     cursor.execute("Select * from FeedbackMaster F inner join LoginMaster L where L.loginId = F.feedbackFrom_LoginId and L.loginRole = 'user'")
    #     dict1 = cursor.fetchall()
    #     cursor.close()
    #     connection.close()
    #     return dict1

    def bloodbankAddFeedback(self,feedbackVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute(
            "insert into FeedbackMaster(feedbackRating,feedbackDescription,feedbackFrom_LoginId,feedbackTo_LoginId,feedbackDate,feedbackTime) values ('" + feedbackVO.feedbackRating + "','" + feedbackVO.feedbackDescription + "','" + str(feedbackVO.feedbackFrom_LoginId) + "','" + str(feedbackVO.feedbackTo_LoginId) + "','" + feedbackVO.feedbackDate + "','" + feedbackVO.feedbackTime + "')")
        connection.commit()
        cursor.close()
        connection.close()

    def bloodbankViewBloodbankFeedback(self,feedbackVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("select * from FeedbackMaster where feedbackFrom_LoginId = '"+str(feedbackVO.feedbackFrom_LoginId)+"'")
        dict1= cursor.fetchall()
        connection.commit()
        cursor.close()
        connection.close()
        return dict1

    def adminViewBloodbankFeedback(self,feedbackVO):
        connection = conn_db()
        cursor = connection.cursor()
        cursor.execute("Select * from FeedbackMaster where feedbackTo_LoginId ='"+str(feedbackVO.feedbackTo_LoginId)+"'")
        dict1 = cursor.fetchall()
        cursor.close()
        connection.close()
        return dict1