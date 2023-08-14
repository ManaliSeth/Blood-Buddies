from project import app
from flask import render_template


@app.route('/')
def loadIndex():
    return render_template('user/index2.html')

@app.route('/loadHome')
def loadHome():
    return render_template('user/index2.html')


@app.route('/loadUser')
def loadUser():
    return render_template('user/index.html')


@app.route('/loadAdmin')
def loadAdmin():
    return render_template('admin/index.html')


@app.route('/loadBloodbank')
def loadBloodbank():
    return render_template('bloodbank/index.html')


