from project import app
from flask import render_template, request, session, redirect, url_for
from project.com.vo.BloodbankVO import BloodbankVO
from project.com.dao.BloodbankDAO import BloodbankDAO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
import string
import random
import smtplib
from project.com.dao.AreaDAO import AreaDAO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@app.route('/NearMe')
def NearMe():
    bloodbankDAO = BloodbankDAO()
    bloodbankDict = bloodbankDAO.adminViewBloodbank()
    return render_template('user/nearMe.html', bloodbankDict=bloodbankDict)


@app.route('/bloodbankNearMe', methods=['POST'])
def bloodbankNearMe():
    userPincode = request.form['userPincode']

    bloodbankDAO = BloodbankDAO()

    bloodbankDict,areaDict = bloodbankDAO.userViewBloodbank(userPincode)

    for i in areaDict:
        for j in bloodbankDict:
            if i['areaId'] == j['bloodbank_AreaId']:
                j['areaName'] = i['areaName']

    print("bloodbankDict=",bloodbankDict)

    return render_template('user/bloodbankNearMe.html',bloodbankDict=bloodbankDict,msg="Sorry! No bloodbanks available nearby.")

@app.route('/bloodbankLoadRegister', methods=['GET'])
def bloodbankLoadRegister():
    areaDAO = AreaDAO()

    areaDict = areaDAO.adminViewArea()

    return render_template('bloodbank/register.html', areaDict=areaDict)


@app.route('/bloodbankInsertBloodbank', methods=['POST'])
def bloodbankInsertBloodbank():
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    bloodbankVO = BloodbankVO()
    bloodbankDAO = BloodbankDAO()

    bloodbankName = request.form['bloodbankName']
    bloodbankAddress = request.form['bloodbankAddress']
    bloodbank_AreaId = request.form['bloodbank_AreaId']
    bloodbankPincode = request.form['bloodbankPincode']
    bloodbankDescription = request.form['bloodbankDescription']
    bloodbankContactNumber = request.form['bloodbankContactNumber']
    loginEmail = request.form['loginEmail']
    bloodbankRegistrationDate = request.form['bloodbankRegistrationDate']

    loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))

    print("loginPassword=" + loginPassword)

    sender = "pythondemodonotreply@gmail.com"

    receiver = loginEmail

    msg = MIMEMultipart()

    msg['FROM'] = sender

    msg['TO'] = receiver

    msg['Subject'] = "PYTHON PASSWORD"

    msg.attach(MIMEText(loginPassword, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender, "qazwsxedcrfvtgb1234567890!")

    text = msg.as_string()

    server.sendmail(sender, receiver, text)

    loginVO.loginEmail = loginEmail
    loginVO.loginPassword = loginPassword
    loginVO.loginRole = "bloodbank"

    loginDAO.insertLogin(loginVO)

    bloodbankVO.bloodbankName = bloodbankName
    bloodbankVO.bloodbankAddress = bloodbankAddress
    bloodbankVO.bloodbank_AreaId = bloodbank_AreaId
    bloodbankVO.bloodbankPinCode = bloodbankPincode
    bloodbankVO.bloodbankDescription = bloodbankDescription
    bloodbankVO.bloodbankContactNumber = bloodbankContactNumber
    bloodbankVO.bloodbankRegistrationDate = bloodbankRegistrationDate
    bloodbankVO.bloodbankStatus = "active"

    bloodbankDAO.insertBloodbank(bloodbankVO)

    server.quit()

    return render_template('bloodbank/login.html')


@app.route('/bloodbankDeleteBloodbank',methods=['GET'])
def bloodbankDeleteBloodbank():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        bloodbankVO = BloodbankVO()

        bloodbankVO.loginId = loginId

        bloodbankDAO = BloodbankDAO()

        bloodbankDAO.bloodbankDeleteBloodbank(bloodbankVO)

        return render_template('user/login.html')

    else:

        return redirect(url_for('loadBloodbank'))


@app.route('/bloodbankEditBloodbank',methods=['GET'])
def bloodbankEditBloodbank():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        bloodbankVO = BloodbankVO()

        bloodbankVO.loginId = loginId

        bloodbankDAO = BloodbankDAO()

        bloodbankDict = bloodbankDAO.bloodbankEditBloodbank(bloodbankVO)

        return render_template('bloodbank/editBloodbank.html', bloodbankDict=bloodbankDict)
    else:

        return render_template('user/login.html')


@app.route('/bloodbankUpdateBloodbank', methods=['POST'])
def bloodbankUpdateBloodbank():
    bloodbankId = request.form['bloodbankId']
    bloodbankName = request.form['bloodbankName']
    bloodbankAddress = request.form['bloodbankAddress']
    bloodbankPincode = request.form['bloodbankPincode']
    bloodbankDescription = request.form['bloodbankDescription']
    bloodbankContactNumber = request.form['bloodbankContactNumber']
    bloodbankRegistrationDate = request.form['bloodbankRegistrationDate']

    bloodbankVO = BloodbankVO()

    bloodbankVO.bloodbankId = bloodbankId
    bloodbankVO.bloodbankName = bloodbankName
    bloodbankVO.bloodbankAddress = bloodbankAddress
    bloodbankVO.bloodbankPinCode = bloodbankPincode
    bloodbankVO.bloodbankDescription = bloodbankDescription
    bloodbankVO.bloodbankContactNumber = bloodbankContactNumber
    bloodbankVO.bloodbankRegistrationDate = bloodbankRegistrationDate

    bloodbankDAO = BloodbankDAO()

    bloodbankDAO.bloodbankUpdateBloodbank(bloodbankVO)

    return redirect(url_for('loadBloodbank'))



@app.route('/adminViewBloodbank')
def adminViewBloodbank():
    if 'loginId' in session and session['loginRole']=="admin":

        loginId = session['loginId']

        print("loginId=", loginId)

        bloodbankVO = BloodbankVO()

        bloodbankVO.loginId = loginId

        bloodbankDAO = BloodbankDAO()

        bloodbankDict = bloodbankDAO.adminViewBloodbank()

        print(bloodbankDict)

        return render_template('admin/viewBloodbank.html', bloodbankDict=bloodbankDict)

    else:

        return render_template('bloodbank/login.html')


@app.route('/adminDeleteBloodbank',methods=['GET'])
def adminDeleteBloodbank():

    bloodbankId = request.args.get('bloodbankId')

    bloodbankVO = BloodbankVO()

    bloodbankVO.bloodbankId = bloodbankId

    bloodbankDAO = BloodbankDAO()

    bloodbankDAO.adminDeleteBloodbank(bloodbankVO)

    return redirect(url_for('adminViewBloodbank'))


@app.route('/adminEditBloodbank',methods=['GET'])
def adminEditBloodbank():

    bloodbankId = request.args.get('bloodbankId')

    bloodbankVO = BloodbankVO()

    bloodbankVO.bloodbankId = bloodbankId

    bloodbankDAO = BloodbankDAO()

    bloodbankDict = bloodbankDAO.adminEditBloodbank(bloodbankVO)

    return render_template('admin/editBloodbank.html', bloodbankDict=bloodbankDict)


@app.route('/adminUpdateBloodbank',methods=['POST'])
def adminUpdateBloodbank():

    bloodbankId = request.form['bloodbankId']
    bloodbankName = request.form['bloodbankName']
    bloodbankAddress = request.form['bloodbankAddress']
    bloodbankPincode = request.form['bloodbankPincode']
    bloodbankDescription = request.form['bloodbankDescription']
    bloodbankContactNumber = request.form['bloodbankContactNumber']
    bloodbankRegistrationDate = request.form['bloodbankRegistrationDate']

    bloodbankVO = BloodbankVO()

    bloodbankVO.bloodbankId = bloodbankId
    bloodbankVO.bloodbankName = bloodbankName
    bloodbankVO.bloodbankAddress = bloodbankAddress
    bloodbankVO.bloodbankPinCode = bloodbankPincode
    bloodbankVO.bloodbankDescription = bloodbankDescription
    bloodbankVO.bloodbankContactNumber = bloodbankContactNumber
    bloodbankVO.bloodbankRegistrationDate = bloodbankRegistrationDate

    bloodbankDAO = BloodbankDAO()

    bloodbankDAO.adminUpdateBloodbank(bloodbankVO)

    return redirect(url_for('adminViewBloodbank'))


@app.route('/bloodbankCountUser')
def bloodbankCountUser():

    bloodbankDAO = BloodbankDAO()

    bloodbankDAO.getUserCount()




