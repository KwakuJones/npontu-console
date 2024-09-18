import os
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/delUser',methods=['POST','GET'])
def create():
    name = request.form['username']
    username = 'username: ' + name
    f=open("/home/jerryjones/myProject/npontu-console/samplevars.yml","w")
    f.write(username)
    f.close()
    os.system("ansible-playbook delUser.yml")
    print("Success!")



if __name__ == '__main__':
    app.run()

