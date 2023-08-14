from project import app
from flask import render_template, request, session, redirect, url_for
from project.com.vo.UserVO import UserVO
from project.com.dao.UserDAO import UserDAO
from project.com.vo.LoginVO import LoginVO
from project.com.dao.LoginDAO import LoginDAO
import string
import random
import smtplib
from project.com.dao.AreaDAO import AreaDAO
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# @app.route('/userViewBloodbank')
# def userViewBloodbank():
#
#     return render_template('')

@app.route('/userLoadLogin')
def userLoadLogin():
    return render_template('user/login.html')


@app.route('/userLoadRegister')
def userLoadRegister():

    areaDAO= AreaDAO()

    areaDict = areaDAO.adminViewArea()

    return render_template('user/register.html',areaDict=areaDict)


@app.route('/userLoadContactUs')
def userLoadContactUs():
    return render_template('user/ContactUs.html')


@app.route('/userLoadAboutUs')
def userLoadAboutUs():
    return render_template('user/AboutUs.html')


@app.route('/userLoadLoginContactUs')
def userLoadLoginContactUs():
    return render_template('user/loginContactUs.html')


@app.route('/userLoadLoginAboutUs')
def userLoadLoginAboutUs():
    return render_template('user/loginAboutUs.html')


@app.route('/userInsertUser', methods=['POST'])
def userInsertUser():
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    userVO = UserVO()
    userDAO = UserDAO()

    userFirstName = request.form['userFirstName']
    userLastName = request.form['userLastName']
    loginEmail = request.form['loginEmail']
    userAddress = request.form['userAddress']
    userGender = request.form['userGender']
    userDateOfBirth = request.form['userDateOfBirth']
    userContactNumber = request.form['userContactNumber']
    userBloodGroup = request.form['userBloodGroup']
    # user_LoginId = session['loginId']

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
    loginVO.loginRole = "user"

    loginDAO.insertLogin(loginVO)

    userVO.userFirstName = userFirstName
    userVO.userLastName = userLastName
    userVO.userAddress = userAddress
    userVO.userGender = userGender
    userVO.userDateOfBirth = userDateOfBirth
    userVO.userContactNumber = userContactNumber
    userVO.userBloodGroup = userBloodGroup
    userVO.userStatus = "active"


    userDAO.insertUser(userVO)

    server.quit()

    return render_template('user/login.html')


@app.route('/userDeleteUser',methods=['GET'])
def userDeleteUser():
    if 'loginId' in session and session['loginRole'] == "user":

        loginId = session['loginId']

        print("loginId=", loginId)

        userVO = UserVO()

        userVO.loginId = loginId

        userDAO = UserDAO()

        userDAO.userDeleteUser(userVO)

        return render_template('user/login.html')

    else:

        return redirect(url_for('loadUser'))


@app.route('/userEditUser',methods=['GET'])
def userEditUser():
    if 'loginId' in session and session['loginRole'] == "user":

        loginId = session['loginId']

        print("loginId=", loginId)

        userVO = UserVO()

        userVO.loginId = loginId

        userDAO = UserDAO()

        userDict = userDAO.userEditUser(userVO)

        return render_template('user/editUser.html', userDict=userDict)
    else:

        return render_template('user/login.html')


@app.route('/userUpdateUser', methods=['POST'])
def userUpdateUser():
    userId = request.form['userId']
    userFirstName = request.form['userFirstName']
    userLastName = request.form['userLastName']
    userAddress = request.form['userAddress']
    userGender = request.form['userGender']
    userDateOfBirth = request.form['userDateOfBirth']
    userContactNumber = request.form['userContactNumber']
    userBloodGroup = request.form['userBloodGroup']

    userVO = UserVO()

    userVO.userId = userId
    userVO.userFirstName = userFirstName
    userVO.userLastName = userLastName
    userVO.userAddress = userAddress
    userVO.userGender = userGender
    userVO.userDateOfBirth = userDateOfBirth
    userVO.userContactNumber = userContactNumber
    userVO.userBloodGroup = userBloodGroup

    userDAO = UserDAO()

    userDAO.userUpdateUser(userVO)

    return redirect(url_for('loadUser'))



@app.route('/adminViewUser')
def adminViewUser():
    if 'loginId' in session and session['loginRole']=="admin":

        loginId = session['loginId']

        print("loginId=", loginId)

        userVO = UserVO()

        userVO.loginId = loginId

        userDAO = UserDAO()

        userDict = userDAO.adminViewUser()

        print(userDict)

        return render_template('admin/viewUser.html', userDict=userDict)

    else:

        return render_template('user/login.html')


@app.route('/adminDeleteUser',methods=['GET'])
def adminDeleteUser():

    userId = request.args.get('userId')

    userVO = UserVO()

    userVO.userId = userId

    userDAO = UserDAO()

    userDAO.adminDeleteUser(userVO)

    return redirect(url_for('adminViewUser'))


@app.route('/adminEditUser',methods=['GET'])
def adminEditUser():

    userId = request.args.get('userId')

    userVO = UserVO()

    userVO.userId = userId

    userDAO = UserDAO()

    userDict = userDAO.adminEditUser(userVO)

    return render_template('admin/editUser.html', userDict=userDict)


@app.route('/adminUpdateUser',methods=['POST'])
def adminUpdateUser():

    userId = request.form['userId']
    userFirstName = request.form['userFirstName']
    userLastName = request.form['userLastName']
    userAddress = request.form['userAddress']
    userGender = request.form['userGender']
    userDateOfBirth = request.form['userDateOfBirth']
    userContactNumber = request.form['userContactNumber']
    userBloodGroup = request.form['userBloodGroup']

    userVO = UserVO()

    userVO.userId = userId
    userVO.userFirstName = userFirstName
    userVO.userLastName = userLastName
    userVO.userAddress = userAddress
    userVO.userGender = userGender
    userVO.userDateOfBirth = userDateOfBirth
    userVO.userContactNumber = userContactNumber
    userVO.userBloodGroup = userBloodGroup

    userDAO = UserDAO()

    userDAO.adminUpdateUser(userVO)

    return redirect(url_for('adminViewUser'))


@app.route('/bloodbankViewUser')
def bloodbankViewUser():
    if 'loginId' in session and session['loginRole']=="bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        userVO = UserVO()

        userVO.loginId = loginId

        userDAO = UserDAO()

        userDict = userDAO.bloodbankViewUser()

        print(userDict)

        return render_template('bloodbank/viewUser.html', userDict=userDict)

    else:

        return render_template('user/login.html')


@app.route('/bloodbankDeleteUser',methods=['GET'])
def bloodbankDeleteUser():

    userId = request.args.get('userId')

    userVO = UserVO()

    userVO.userId = userId

    userDAO = UserDAO()

    userDAO.bloodbankDeleteUser(userVO)

    return redirect(url_for('bloodbankViewUser'))


@app.route('/bloodbankEditUser',methods=['GET'])
def bloodbankEditUser():

    userId = request.args.get('userId')

    userVO = UserVO()

    userVO.userId = userId

    userDAO = UserDAO()

    userDict = userDAO.bloodbankEditUser(userVO)

    return render_template('bloodbank/editUser.html', userDict=userDict)


@app.route('/bloodbankUpdateUser', methods=['POST'])
def bloodbankUpdateUser():
    userId = request.form['userId']
    userFirstName = request.form['userFirstName']
    userLastName = request.form['userLastName']
    userAddress = request.form['userAddress']
    userGender = request.form['userGender']
    userDateOfBirth = request.form['userDateOfBirth']
    userContactNumber = request.form['userContactNumber']
    userBloodGroup = request.form['userBloodGroup']

    userVO = UserVO()

    userVO.userId = userId
    userVO.userFirstName = userFirstName
    userVO.userLastName = userLastName
    userVO.userAddress = userAddress
    userVO.userGender = userGender
    userVO.userDateOfBirth = userDateOfBirth
    userVO.userContactNumber = userContactNumber
    userVO.userBloodGroup = userBloodGroup

    userDAO = UserDAO()

    userDAO.bloodbankUpdateUser(userVO)

    return redirect(url_for('bloodbankViewUser'))











