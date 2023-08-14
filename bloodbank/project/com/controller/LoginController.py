from project.com.dao import *
from project import app
from flask import render_template,request,session,redirect,url_for
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
import string
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

connection = conn_db()
cursor = connection.cursor()


@app.route('/forgotPassword')
def forgotPassword():
    return render_template('user/forgotPassword.html')


@app.route('/checkLoginEmail',methods=['POST'])
def checkLoginEmail():
    loginEmail = request.form['loginEmail']

    loginVO = LoginVO()
    loginVO.loginEmail = loginEmail
    print(loginVO.loginEmail)

    session['loginEmail'] = loginEmail
    print(session['loginEmail'])

    loginDAO = LoginDAO()
    loginDict = loginDAO.checkLoginEmail(loginVO)

    print("loginDict=",loginDict)

    if len(loginDict)==0:
        return render_template('user/forgotPassword.html',msg="Incorrect EmailID")

    else:
        otp = ''.join((random.choice(string.digits)) for x in range(4))

        session['otp'] = otp

        print("otp=" +otp)

        sender = "pythondemodonotreply@gmail.com"

        receiver = loginEmail

        msg = MIMEMultipart()

        msg['FROM'] = sender

        msg['TO'] = receiver

        msg['Subject'] = "OTP"

        msg.attach(MIMEText(otp, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()

        server.login(sender, "qazwsxedcrfvtgb1234567890!")

        text = msg.as_string()

        server.sendmail(sender, receiver, text)

        server.quit()

        return render_template('user/enterOTP.html')


@app.route('/checkOTP',methods=['POST'])
def checkOTP():
    otp = request.form['otp']

    if otp == session['otp']:

            loginEmail = session['loginEmail']

            loginVO = LoginVO()

            loginVO.loginEmail = loginEmail

            loginPassword = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))

            session['loginPassword'] = loginPassword

            print("loginPassword=" + loginPassword)

            sender = "pythondemodonotreply@gmail.com"

            receiver = loginEmail

            msg = MIMEMultipart()

            msg['FROM'] = sender

            msg['TO'] = receiver

            msg['Subject'] = "NEW PASSWORD"

            msg.attach(MIMEText(loginPassword, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)

            server.starttls()

            server.login(sender, "qazwsxedcrfvtgb1234567890!")

            text = msg.as_string()

            server.sendmail(sender, receiver, text)

            server.quit()

            loginVO.loginPassword = loginPassword

            loginDAO = LoginDAO()

            loginDAO.updatePassword(loginVO)

            return render_template('user/login.html')

    else:

        return render_template('user/enterOTP.html',msg="Incorrect OTP")


@app.route('/login', methods=['POST'])
def login():

    loginVO = LoginVO()
    loginDAO = LoginDAO()

    loginVO.loginEmail = request.form['loginEmail']
    loginVO.loginPassword = request.form['loginPassword']

    loginDict = loginDAO.searchLogin(loginVO)
    print(loginDict)

    if len(loginDict) == 0:

        return render_template('user/login.html', errorMsg1='Username is Incorrect !')

    elif loginVO.loginPassword != loginDict[0]['loginPassword']:

        return render_template('user/login.html', errorMsg2='Password is Incorrect !')

    elif loginDict[0]['loginRole'] == 'admin':

        session['loginRole'] = loginDict[0]['loginRole']

        session['loginId'] = loginDict[0]['loginId']

        return redirect(url_for('loadAdmin'))

    elif loginDict[0]['loginRole'] == 'bloodbank':

        session['loginRole'] = loginDict[0]['loginRole']

        session['loginId'] = loginDict[0]['loginId']

        return redirect(url_for('loadBloodbank'))

    elif loginDict[0]['loginRole'] == 'user':

        session['loginRole'] = loginDict[0]['loginRole']

        session['loginId'] = loginDict[0]['loginId']

        return redirect((url_for('loadUser')))


@app.route('/logout')
def logout():
    session.clear()
    return render_template('user/login.html')


@app.route('/userChangePassword')
def userChangePassword():
    return render_template('user/changePassword.html')


@app.route('/bloodbankChangePassword')
def bloodbankChangePassword():
    return render_template('bloodbank/changePassword.html')


@app.route('/changePassword',methods=['POST'])
def changePassword():

    oldPassword = request.form['oldPassword']
    newPassword = request.form['newPassword']
    confirmPassword = request.form['confirmPassword']

    loginVO = LoginVO()

    loginVO.oldPassword = oldPassword
    loginVO.newPassword = newPassword
    loginVO.confirmPassword = confirmPassword

    loginDAO = LoginDAO()

    if 'loginId' in session and session['loginRole'] == 'user':

        loginId = session['loginId']

        loginVO.loginId = loginId

        Password_LoginDict = loginDAO.getCurrentPassword(loginVO)

        if len(Password_LoginDict) == 0:
            return render_template("user/changePassword.html", msg1="Old password is incorrect")

        else:
            if loginVO.newPassword == loginVO.confirmPassword:
                loginDAO.setNewPassword(loginVO)
                return redirect(url_for('loadUser'))
            else:
                return render_template('user/changePassword.html',msg2="Incorrect Password")


    elif 'loginId' in session and session['loginRole'] == 'bloodbank':

        loginId = session['loginId']

        loginVO.loginId = loginId

        Password_LoginDict = loginDAO.getCurrentPassword(loginVO)

        print("PasswordLoginDict=",Password_LoginDict)

        if len(Password_LoginDict) == 0:
            return render_template("bloodbank/changePassword.html", msg1="Old password is incorrect")

        else:
            if loginVO.newPassword == loginVO.confirmPassword:
                loginDAO.setNewPassword(loginVO)
                return redirect(url_for('loadBloodbank'))
            else:
                return render_template('bloodbank/changePassword.html',msg2="Incorrect Password")














