from project import app
from flask import render_template,request,session,redirect,url_for
from project.com.vo.FeedbackVO import FeedbackVO
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.dao.BloodbankDAO import BloodbankDAO
import datetime


@app.route('/userLoadFeedback')
def userLoadFeedback():
    bloodbankDAO = BloodbankDAO()
    bloodbankDict = bloodbankDAO.adminViewBloodbank()
    return render_template('user/addFeedback.html',bloodbankDict=bloodbankDict)


@app.route('/userAddFeedback',methods=['POST'])
def userAddFeedback():

    feedbackRating = request.form['feedbackRating']
    feedbackDescription = request.form['feedbackDescription']

    feedbackVO = FeedbackVO()
    feedbackDAO = FeedbackDAO()

    feedbackFrom_LoginId = session['loginId']
    print(feedbackFrom_LoginId)

    bloodbankId = request.form['bloodbankId']
    feedbackTo_LoginId = feedbackDAO.getFeedbackTo_LoginId(bloodbankId)
    print(feedbackTo_LoginId[0]['bloodbank_LoginId'])

    currentDT = datetime.datetime.now()

    feedbackDate = currentDT.strftime("%Y/%m/%d")
    feedbackTime = currentDT.strftime("%H:%M:%S")

    feedbackVO.feedbackRating = feedbackRating
    feedbackVO.feedbackDescription = feedbackDescription
    feedbackVO.feedbackFrom_LoginId = feedbackFrom_LoginId
    feedbackVO.feedbackTo_LoginId = feedbackTo_LoginId[0]['bloodbank_LoginId']
    feedbackVO.feedbackDate = feedbackDate
    feedbackVO.feedbackTime = feedbackTime

    feedbackDAO = FeedbackDAO()

    feedbackDAO.userAddFeedback(feedbackVO)
    return redirect(url_for('loadUser'))


@app.route('/userViewUserFeedback')
def userViewUserFeedback():
    if 'loginId' in session and session['loginRole'] == "user":

        loginId = session['loginId']

        print("loginId=", loginId)

        feedbackVO = FeedbackVO()

        feedbackVO.feedbackFrom_LoginId = loginId

        print(feedbackVO.feedbackFrom_LoginId)

        feedbackDAO = FeedbackDAO()

        feedback_LoginDict, feedbackDict = feedbackDAO.userViewUserFeedback(feedbackVO)

        print(feedback_LoginDict, feedbackDict)

        for i in feedback_LoginDict:

            for j in feedbackDict:

                if i['loginId'] == j['feedbackTo_LoginId']:
                    j['loginToEmail'] = i['loginEmail']

        print("complainDict=", feedbackDict)

        return render_template('user/viewFeedback.html', feedbackDict=feedbackDict)

    else:

        return redirect(url_for('loadUser'))


@app.route('/bloodbankViewUserFeedback')
def bloodbankViewUserFeedback():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        feedbackVO = FeedbackVO()

        feedbackVO.feedbackTo_LoginId = loginId

        feedbackDAO = FeedbackDAO()

        feedbackFrom_LoginId = feedbackDAO.getFeedbackFrom_LoginId(feedbackVO)

        ls1=[]

        for i in feedbackFrom_LoginId:
            feedbackVO.feedbackFrom_LoginId = i['feedbackFrom_LoginId']
            feedback_LoginDict= feedbackDAO.getLoginEmail(feedbackVO)
            ls1.append(feedback_LoginDict[0])

        feedbackDict  = feedbackDAO.bloodbankViewUserFeedback(feedbackVO)
        print(ls1)
        print(feedbackDict)

        for i in ls1:
            for j in feedbackDict:
                if i['feedbackFrom_LoginId'] == j['feedbackFrom_LoginId']:
                    j['loginFromEmail'] = i['loginEmail']
        print(feedbackDict)

        return render_template('bloodbank/viewUserFeedback.html',feedbackDict=feedbackDict)

    else:

        return redirect(url_for('loadBloodbank'))


# @app.route('/adminViewUserFeedback')
# def adminViewUserFeedback():
#     if 'loginId' in session and session['loginRole'] == "admin":
#
#         loginId = session['loginId']
#
#         print("loginId=", loginId)
#
#         feedbackVO = FeedbackVO()
#
#         feedbackVO.feedbackFrom_LoginId = loginId
#
#         feedbackDAO = FeedbackDAO()
#
#         feedbackDict = feedbackDAO.adminViewUserFeedback()
#
#         print(feedbackDict)
#
#         return render_template('admin/viewUserFeedback.html', feedbackDict=feedbackDict)
#
#     else:
#
#         return redirect(url_for('loadAdmin'))


@app.route('/bloodbankLoadFeedback')
def bloodbankLoadFeedback():
    return render_template('bloodbank/addFeedback.html')


@app.route('/bloodbankAddFeedback',methods=['POST'])
def bloodbankAddFeedback():

    feedbackRating = request.form['feedbackRating']
    feedbackDescription = request.form['feedbackDescription']

    feedbackVO = FeedbackVO()

    feedbackFrom_LoginId = session['loginId']
    print(feedbackFrom_LoginId)

    currentDT = datetime.datetime.now()

    feedbackDate = currentDT.strftime("%Y/%m/%d")
    feedbackTime = currentDT.strftime("%H:%M:%S")

    feedbackVO.feedbackRating = feedbackRating
    feedbackVO.feedbackDescription = feedbackDescription
    feedbackVO.feedbackFrom_LoginId = feedbackFrom_LoginId
    feedbackVO.feedbackTo_LoginId = 1
    feedbackVO.feedbackDate = feedbackDate
    feedbackVO.feedbackTime = feedbackTime

    feedbackDAO = FeedbackDAO()

    feedbackDAO.userAddFeedback(feedbackVO)
    return redirect(url_for('loadBloodbank'))


@app.route('/bloodbankViewBloodbankFeedback')
def bloodbankViewBloodbankFeedback():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        feedbackVO = FeedbackVO()

        feedbackVO.feedbackFrom_LoginId = loginId

        print(feedbackVO.feedbackFrom_LoginId)

        feedbackDAO = FeedbackDAO()

        feedbackDict = feedbackDAO.bloodbankViewBloodbankFeedback(feedbackVO)

        print(feedbackDict)

        return render_template('bloodbank/viewFeedback.html', feedbackDict=feedbackDict)

    else:

        return redirect(url_for('loadBloodbank'))



@app.route('/adminViewBloodbankFeedback')
def adminViewBloodbankFeedback():
    if 'loginId' in session and session['loginRole'] == "admin":

        loginId = session['loginId']

        print("loginId=", loginId)

        feedbackVO = FeedbackVO()

        feedbackVO.feedbackTo_LoginId = loginId

        feedbackDAO = FeedbackDAO()

        feedbackFrom_LoginId = feedbackDAO.getFeedbackFrom_LoginId(feedbackVO)

        ls1 = []

        for i in feedbackFrom_LoginId:
            feedbackVO.feedbackFrom_LoginId = i['feedbackFrom_LoginId']
            feedback_LoginDict = feedbackDAO.getLoginEmail(feedbackVO)
            ls1.append(feedback_LoginDict[0])

        feedbackDict = feedbackDAO.adminViewBloodbankFeedback(feedbackVO)
        print(ls1)
        print(feedbackDict)

        for i in ls1:
            for j in feedbackDict:
                if i['feedbackFrom_LoginId'] == j['feedbackFrom_LoginId']:
                    j['loginFromEmail'] = i['loginEmail']
        print(feedbackDict)

        return render_template('admin/viewBloodbankFeedback.html', feedbackDict=feedbackDict)

    else:

        return redirect(url_for('loadAdmin'))
