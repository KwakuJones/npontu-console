import os
from flask import Flask,request,render_template
app = Flask(__name__)

@app.route('/expire',methods=['POST','GET'])
def create():
    name = request.form['username']
    period = request.form['days']
    username = 'username: ' + name 
    days = 'days: ' + period
    f=open("/home/ubuntu/npontu-console/samplevars.yml","w")
    f.write(username)
    f.write("\n")
    f.write(days)
    f.close()
    os.system("ansible-playbook expire.yml")
    print("Success!")



if __name__ == '__main__':
    app.run()

