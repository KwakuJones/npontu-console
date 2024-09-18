import os
from flask import Flask,request,render_template,url_for
app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/createForm')
def createForm():
    return render_template('createForm.html')

@app.route('/createUser',methods=['POST','GET'])
def createUser():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        username = 'username: ' + name
        password = 'password: ' + password
        f =open("/home/jerryjones/myProject/npontu-console/samplevars.yml","w")
        f.write(username)
        f.write("\n")
        f.write(password)
        f.close()
        os.system("ansible-playbook multiUser.yml")
        print("Success!")
        return render_template('successCreate.html')


@app.route('/delForm')
def delForm():
    return render_template('deleteUser.html')

@app.route('/delUser',methods=['POST','GET'])
def delUser():
    if request.method == 'POST':
        name = request.form['username']
        username = 'username: ' + name
        f=open("/home/jerryjones/myProject/npontu-console/samplevars.yml","w")
        f.write(username)
        f.close()
        os.system("ansible-playbook delUser.yml")
        print("Success!")
        return render_template('successDel.html')


@app.route('/passForm')
def passForm():
    return render_template('password.html')

@app.route('/expire',methods=['POST','GET'])
def expire():
    if request.method == 'POST':
        name = request.form['username']
        period = request.form['days']
        username = 'username: ' + name 
        days = 'days: ' + period
        f=open("/home/jerryjones/myProject/npontu-console/samplevars.yml","w")
        f.write(username)
        f.write("\n")
        f.write(days)
        f.close()
        os.system("ansible-playbook expire.yml")
        print("Success!")
        return render_template('successExpire.html')

if __name__ == '__main__':
    app.run()
