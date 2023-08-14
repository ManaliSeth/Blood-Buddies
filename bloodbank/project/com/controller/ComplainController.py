from project import app
from flask import render_template, request, redirect, url_for, session
from project.com.vo.ComplainVO import ComplainVO
from project.com.dao.ComplainDAO import ComplainDAO
from project.com.dao.BloodbankDAO import BloodbankDAO
from werkzeug.utils import secure_filename
import os
import datetime


@app.route('/userLoadComplain')
def userLoadComplain():
    bloodbankDAO = BloodbankDAO()

    bloodbankDict = bloodbankDAO.adminViewBloodbank()

    return render_template('user/addComplain.html',bloodbankDict=bloodbankDict)


@app.route('/userAddComplain',methods=['POST'])
def userAddComplain():

    UPLOAD_FOLDER = 'project/static/adminresources/dataset'

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    complainSubject = request.form['complainSubject']

    complainDescription = request.form['complainDescription']

    file = request.files['file']
    print(file)

    filename = secure_filename(file.filename)
    print(filename)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'])
    print(filepath)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

    complainVO = ComplainVO()
    complainDAO = ComplainDAO()

    complainFrom_LoginId = session['loginId']
    print(complainFrom_LoginId)

    bloodbankId = request.form['bloodbankId']
    complainTo_LoginId = complainDAO.getComplainTo_LoginId(bloodbankId)
    print(complainTo_LoginId[0]['bloodbank_LoginId'])

    currentDT = datetime.datetime.now()

    complainDate = currentDT.strftime("%Y/%m/%d")
    complainTime = currentDT.strftime("%H:%M:%S")


    complainVO.complainSubject = complainSubject
    complainVO.complainDescription = complainDescription
    complainVO.datasetname = filename
    complainVO.datasetpath = filepath
    complainVO.complainFrom_LoginId = complainFrom_LoginId
    complainVO.complainTo_LoginId = complainTo_LoginId[0]['bloodbank_LoginId']
    complainVO.complainDate = complainDate
    complainVO.complainTime = complainTime
    complainVO.complainStatus = "pending"


    complainDAO = ComplainDAO()

    complainDAO.userAddComplain(complainVO)
    return redirect(url_for('loadUser'))

@app.route('/userViewUserComplain')
def userViewUserComplain():
    if 'loginId' in session and session['loginRole'] == "user":

        loginId = session['loginId']

        print("loginId=", loginId)

        complainVO = ComplainVO()

        complainVO.complainFrom_LoginId = loginId

        complainDAO = ComplainDAO()

        complain_LoginDict,complainDict= complainDAO.userViewUserComplain(complainVO)

        print(complain_LoginDict,complainDict)

        for i in complain_LoginDict:

            for j in complainDict:

                if i['loginId']==j['complainTo_LoginId']:

                    j['loginToEmail']=i['loginEmail']

        print("complainDict=",complainDict)

        return render_template('user/viewUserComplain.html',complainDict=complainDict)

    else:

        return redirect(url_for('loadUser'))


@app.route('/bloodbankViewUserComplain')
def bloodbankViewUserComplain():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        complainVO = ComplainVO()

        complainVO.complainTo_LoginId = loginId

        complainDAO = ComplainDAO()

        complainFrom_LoginId = complainDAO.getComplainFrom_LoginId(complainVO)

        ls1 = []

        for i in complainFrom_LoginId:
            complainVO.complainFrom_LoginId = i['complainFrom_LoginId']
            complain_LoginDict = complainDAO.getLoginEmail(complainVO)
            ls1.append(complain_LoginDict[0])

        complainDict = complainDAO.bloodbankViewUserComplain(complainVO)
        print(ls1)
        print(complainDict)

        for i in ls1:
            for j in complainDict:
                if i['complainFrom_LoginId'] == j['complainFrom_LoginId']:
                    j['loginFromEmail'] = i['loginEmail']
        print(complainDict)

        return render_template('bloodbank/viewUserComplain.html', complainDict=complainDict)

    else:

        return redirect(url_for('loadBloodbank'))


# @app.route('/adminViewUserComplain')
# def adminViewUserComplain():
#     if 'loginId' in session and session['loginRole'] == "admin":
#
#         loginId = session['loginId']
#
#         print("loginId=", loginId)
#
#         complainVO = ComplainVO()
#
#         complainVO.complainTo_LoginId = loginId
#
#         complainDAO = ComplainDAO()
#
#         complainDict = complainDAO.adminViewUserComplain()
#
#         print(complainDict)
#
#         return render_template('admin/viewUserComplain.html', complainDict=complainDict)
#
#     else:
#
#         return redirect(url_for('loadAdmin'))


@app.route('/bloodbankLoadComplain')
def bloodbankLoadComplain():
    return render_template('bloodbank/addComplain.html')


@app.route('/bloodbankAddComplain',methods=['POST'])
def bloodbankAddComplain():

    UPLOAD_FOLDER = 'project/static/adminresources/dataset'

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    complainSubject = request.form['complainSubject']

    complainDescription = request.form['complainDescription']

    file = request.files['file']
    print(file)

    filename = secure_filename(file.filename)
    print(filename)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'])
    print(filepath)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

    complainFrom_LoginId = session['loginId']

    print(complainFrom_LoginId)

    currentDT = datetime.datetime.now()

    complainDate = currentDT.strftime("%Y/%m/%d")
    complainTime = currentDT.strftime("%H:%M:%S")

    complainVO = ComplainVO()

    complainVO.complainSubject = complainSubject
    complainVO.complainDescription = complainDescription
    complainVO.datasetname = filename
    complainVO.datasetpath = filepath
    complainVO.complainFrom_LoginId = complainFrom_LoginId
    complainVO.complainTo_LoginId = 1
    complainVO.complainDate = complainDate
    complainVO.complainTime = complainTime
    complainVO.complainStatus = "pending"

    complainDAO = ComplainDAO()

    complainDAO.bloodbankAddComplain(complainVO)
    return redirect(url_for('loadBloodbank'))


@app.route('/bloodbankViewBloodbankComplain')
def bloodbankViewBloodbankComplain():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        complainVO = ComplainVO()

        complainVO.complainTo_LoginId = loginId

        complainVO.complainFrom_LoginId = loginId

        complainDAO = ComplainDAO()

        complain_LoginDict,complainDict= complainDAO.bloodbankViewBloodbankComplain(complainVO)

        print(complain_LoginDict,complainDict)

        for i in complain_LoginDict:

            for j in complainDict:

                if i['loginId']==j['complainTo_LoginId']:

                    j['loginToEmail']=i['loginEmail']

        print("complainDict=",complainDict)

        return render_template('bloodbank/viewBloodbankComplain.html',complainDict=complainDict,complain_LoginDict=complain_LoginDict)

    else:

        return redirect(url_for('loadBloodbank'))


@app.route('/adminViewBloodbankComplain')
def adminViewBloodbankComplain():
    if 'loginId' in session and session['loginRole'] == "admin":

        loginId = session['loginId']

        print("loginId=", loginId)

        complainVO = ComplainVO()

        complainVO.complainTo_LoginId = loginId

        complainDAO = ComplainDAO()

        complainDict = complainDAO.adminViewBloodbankComplain()

        print(complainDict)

        return render_template('admin/viewBloodbankComplain.html', complainDict=complainDict)

    else:

        return redirect(url_for('loadAdmin'))


@app.route('/bloodbankLoadReplyUserComplain')
def bloodbankLoadReplyUserComplain():
    complainId = request.args.get('complainId')
    complainVO = ComplainVO()
    complainVO.complainId = complainId
    print(complainId)
    print(complainVO.complainId)
    complainDAO = ComplainDAO()
    complainDict = complainDAO.getUserComplaintDetails(complainVO)
    print(complainDict)
    return render_template('bloodbank/replyUserComplain.html', complainDict=complainDict)


@app.route('/bloodbankReplyUserComplain',methods = ['POST'])
def bloodbankReplyUserComplain():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        complainId = request.form['complainId']
        print("complainId=",complainId)

        replyDescription = request.form['replyDescription']

        currentDT = datetime.datetime.now()

        replyDate = currentDT.strftime("%Y/%m/%d")

        replyTime = currentDT.strftime("%H:%M:%S")

        complainVO = ComplainVO()

        complainVO.complainTo_LoginId = loginId

        complainVO.complainFrom_LoginId = complainId

        complainVO.replyDescription = replyDescription

        complainVO.replyDate = replyDate

        complainVO.replyTime = replyTime

        complainVO.complainStatus = "replied"

        complainDAO = ComplainDAO()

        complainDAO.bloodbankReplyUserComplain(complainVO)

        return redirect(url_for('bloodbankViewUserComplain'))

    else:

        return redirect(url_for('loadBloodbank'))


@app.route('/adminLoadReplyBloodbankComplain')
def adminLoadReplyBloodbankComplain():

    complainId = request.args.get('complainId')
    complainVO = ComplainVO()
    complainVO.complainId = complainId
    print(complainId)
    print(complainVO.complainId)
    complainDAO = ComplainDAO()
    complainDict = complainDAO.getBloodbankComplaintDetails(complainVO)
    print(complainDict)
    return render_template('admin/replyBloodbankComplain.html',complainDict=complainDict)


@app.route('/adminReplyBloodbankComplain',methods = ['POST'])
def adminReplyBloodbankComplain():
    if 'loginId' in session and session['loginRole'] == "admin":

        loginId = session['loginId']

        print("loginId=", loginId)

        complainId = request.form['complainId']
        print("complainId=",complainId)

        replyDescription = request.form['replyDescription']

        currentDT = datetime.datetime.now()

        replyDate = currentDT.strftime("%Y/%m/%d")

        replyTime = currentDT.strftime("%H:%M:%S")

        complainVO = ComplainVO()

        complainVO.complainTo_LoginId = loginId

        complainVO.complainId = complainId

        complainVO.replyDescription = replyDescription

        complainVO.replyDate = replyDate

        complainVO.replyTime = replyTime

        complainVO.complainStatus = "replied"

        complainDAO = ComplainDAO()

        complainDAO.adminReplyBloodbankComplain(complainVO)

        return redirect(url_for('adminViewBloodbankComplain'))

    else:

        return redirect(url_for('loadAdmin'))

