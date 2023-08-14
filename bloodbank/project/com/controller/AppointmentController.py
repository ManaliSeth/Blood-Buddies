from project import app
from flask import render_template,request,session,redirect,url_for
from project.com.vo.BloodbankVO import BloodbankVO
from project.com.dao.BloodbankDAO import BloodbankDAO
from project.com.vo.AppointmentVO import AppointmentVO
from project.com.dao.AppointmentDAO import AppointmentDAO
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


@app.route('/userLoadRequestAppointment',methods=['GET'])
def userLoadRequestAppointment():
    bloodbankDAO = BloodbankDAO()
    bloodbankDict = bloodbankDAO.adminViewBloodbank()
    print(bloodbankDict)
    return render_template('user/requestAppointment.html',bloodbankDict=bloodbankDict)


@app.route('/userInsertAppointmentDetails',methods=['POST'])
def userInsertAppointmentDetails():
    if 'loginId' in session and session['loginRole']== 'user':

        appointmentType = request.form['appointmentType']
        appointmentDate = request.form['appointmentDate']
        appointmentTime = request.form['appointmentTime']
        lastDonationDate = request.form['lastDonationDate']
        bloodGroupType = request.form['bloodGroupType']
        bloodbankId = request.form['bloodbankId']
        messageDescription = request.form['messageDescription']

        appointment_LoginId  = session['loginId']

        appointmentVO = AppointmentVO()
        appointmentDAO = AppointmentDAO()

        appointmentVO.appointment_LoginId = appointment_LoginId
        appointmentVO.appointment_BloodbankId = bloodbankId

        appointment_AreaId = appointmentDAO.getAreaId(appointmentVO)
        print(appointment_AreaId)
        appointmentVO.appointment_AreaId  = appointment_AreaId[0]['bloodbank_AreaId']

        appointmentVO.appointmentType = appointmentType
        appointmentVO.appointmentDate = appointmentDate
        appointmentVO.appointmentTime = appointmentTime
        appointmentVO.lastDonationDate = lastDonationDate
        appointmentVO.bloodGroupType = bloodGroupType
        appointmentVO.messageDescription = messageDescription
        appointmentVO.appointmentStatus = "pending"

        appointmentDAO.userInsertAppointmentDetails(appointmentVO)

        return render_template('user/index.html')

    else:
        return render_template('user/requestAppointment.html')


@app.route('/userViewUserAppointment')
def userViewUserAppointment():
    if 'loginId' in session and session['loginRole'] == 'user':

        loginId = session['loginId']

        print("loginId = ",loginId)

        appointmentVO = AppointmentVO()

        appointmentVO.appointment_LoginId = loginId

        appointmentDAO = AppointmentDAO()

        appointmentTo_LoginId = appointmentDAO.getAppointmentTo_LoginId(appointmentVO)

        print("appointmentTo_LoginId=",appointmentTo_LoginId)

        appointmentVO.appointment_BloodbankId = appointmentTo_LoginId[0]['appointment_BloodbankId']

        ls1=[]
        for i in appointmentTo_LoginId:
            appointmentVO.appointmentTo_LoginId = i['appointment_BloodbankId']
            appointment_BloodbankDict = appointmentDAO.getBloodbankName(appointmentVO)
            ls1.append(appointment_BloodbankDict[0])

        print(ls1)

        appointmentDict = appointmentDAO.userViewUserAppointment(appointmentVO)

        print(appointmentDict)

        for i in ls1:

            for j in appointmentDict:

                if i['bloodbank_LoginId'] == j['appointment_BloodbankId']:
                    j['appointmentToBloodbankName'] = i['bloodbankName']

        print("appointmentDict=", appointmentDict)

        return render_template('user/viewUserAppointment.html', appointmentDict=appointmentDict)

    else:

        return  redirect(url_for('loadUser'))


@app.route('/bloodbankViewUserAppointment')
def bloodbankViewUserAppointment():
    if 'loginId' in session and session['loginRole'] == "bloodbank":

        loginId = session['loginId']

        print("loginId=", loginId)

        bloodbankVO = BloodbankVO()

        bloodbankVO.bloodbank_LoginId=loginId

        appointmentDAO = AppointmentDAO()

        appointmentDict = appointmentDAO.bloodbankViewUserAppointment(bloodbankVO)

        ls1 = []
        for i in appointmentDict:
            ls1.append(i['appointment_LoginId'])
        print(ls1)

        ls2=[]
        for i in ls1:
            appointment_LoginDict = appointmentDAO.getLoginEmail(i)
            ls2.append(appointment_LoginDict[0])
        print(ls2)

        for i in ls2:
            for j in appointmentDict:
                if i['loginId'] == j['appointment_LoginId']:
                    j['loginFromEmail'] = i['loginEmail']
        print(appointmentDict)

        return render_template('bloodbank/viewUserAppointment.html', appointmentDict=appointmentDict)

    else:

        return redirect(url_for('loadBloodbank'))


@app.route('/requestApproved')
def requestApproved():

    appointmentId = request.args.get('appointmentId')

    loginEmail = request.args.get('loginEmail')

    appointmentStatus = "Approved"

    appointmentVO = AppointmentVO()

    appointmentVO.appointmentId = appointmentId

    appointmentVO.appointmentStatus = appointmentStatus

    print(appointmentStatus)

    appointmentDAO = AppointmentDAO()

    sender = "pythondemodonotreply@gmail.com"

    receiver = loginEmail

    msg = MIMEMultipart()

    msg['FROM'] = sender

    msg['TO'] = receiver

    msg['Subject'] = "APPOINTMENT STATUS"

    msg.attach(MIMEText(appointmentStatus, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender, "qazwsxedcrfvtgb1234567890!")

    text = msg.as_string()

    server.sendmail(sender, receiver, text)

    appointmentDAO.updateUserAppointment(appointmentVO)

    return redirect(url_for('bloodbankViewUserAppointment'))


@app.route('/requestRejected')
def requestRejected():
    appointmentId = request.args.get('appointmentId')

    loginEmail = request.args.get('loginEmail')

    appointmentVO = AppointmentVO()

    appointmentVO.appointmentId = appointmentId

    appointmentStatus = "Rejected"

    appointmentDAO = AppointmentDAO()

    sender = "pythondemodonotreply@gmail.com"

    receiver = loginEmail

    msg = MIMEMultipart()

    msg['FROM'] = sender

    msg['TO'] = receiver

    msg['Subject'] = "APPOINTMENT STATUS"

    msg.attach(MIMEText(appointmentStatus, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender, "qazwsxedcrfvtgb1234567890!")

    text = msg.as_string()

    server.sendmail(sender, receiver, text)

    appointmentVO.appointmentStatus = appointmentStatus

    appointmentDAO.updateUserAppointment(appointmentVO)

    return redirect(url_for('bloodbankViewUserAppointment'))






