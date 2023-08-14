from project import app
from flask import render_template,request,session,redirect,url_for
from project.com.vo.AreaVO import AreaVO
from project.com.dao.AreaDAO import AreaDAO


@app.route('/adminLoadArea')
def adminLoadArea():
    return render_template('admin/addArea.html')


@app.route('/adminInsertArea',methods=['POST'])
def adminInsertArea():
    areaName = request.form['areaName']

    areaDescription = request.form['areaDescription']

    areaVO = AreaVO()

    areaVO.areaName = areaName

    areaVO.areaDescription = areaDescription

    areaVO.areaStatus = 'active'

    areaDAO = AreaDAO()

    areaDAO.adminInsertArea(areaVO)

    return render_template('admin/addArea.html')


@app.route('/adminViewArea')
def adminViewArea():

    areaDAO = AreaDAO()

    viewArea = areaDAO.adminViewArea()

    return render_template('admin/viewArea.html',viewArea=viewArea)


@app.route('/adminDeleteArea')
def adminDeleteArea():

    areaId = request.args.get('areaId')

    areaVO = AreaVO()

    areaVO.areaId = areaId

    areaDAO = AreaDAO()

    areaDAO.adminDeleteArea(areaVO)

    viewArea = areaDAO.adminViewArea()

    return render_template('admin/viewArea.html',viewArea=viewArea)


@app.route('/adminEditArea')
def adminEditArea():
    areaId = request.args.get('areaId')

    areaVO = AreaVO()

    areaVO.areaId = areaId

    areaDAO = AreaDAO()

    editArea = areaDAO.adminEditArea(areaVO)

    return render_template('admin/editArea.html', editArea = editArea)


@app.route('/adminUpdateArea',methods=['POST'])
def adminUpdateArea():
    areaId = request.form['areaId']
    areaName = request.form['areaName']
    areaDescription = request.form['areaDescription']

    areaVO = AreaVO()
    areaDAO = AreaDAO()

    areaVO.areaId = areaId
    areaVO.areaName = areaName
    areaVO.areaDescription = areaDescription

    areaDAO.adminUpdateArea(areaVO)

    return redirect(url_for('adminViewArea'))







