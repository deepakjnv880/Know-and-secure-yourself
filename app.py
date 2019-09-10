from flask import Flask, render_template, request, flash, redirect
from flask import send_file, url_for, after_this_request
from flask_session import Session
import requests
import sqlite3 as sql
import connection as cn
import healthline
import check
import simplejson as json
# from config import Config
import os
from flask_mysqldb import MySQL
# import urllib
from dotenv import load_dotenv
# from songs import oauth, ext_down
# from anime import anime_download
from flask_socketio import SocketIO



load_dotenv()

DATABASE = cn.DATABASE
cn.get_db()

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__),"templates")
STATIC_DIR = os.path.join(os.path.dirname(__file__),"static")

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)
# app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
# app.config.from_object(Config)
# session = Session()
# session.init_app(app)


@app.route('/', methods=['POST', 'GET'])
def index():
	return render_template('index.html')

# @app.route('/redirecting1',methods=['POST','GET'])
# def different_platform1():
#    symptom=request.form['symptom']
#    # symptom = request.form['symptom']
#    return redirect(url_for('find',symptom=symptom))
#
# @app.route('/<symptom>',methods=['POST','GET'])
# def find(symptom):
#
#
# 	   massage,check1=healthline.healthline_web_scraping(symptom)
# 	   # print(check1[0])
# 	   return render_template('index.html',msg=symptom,msg1=check1[0],msg2=check1[1],msg3=check1[2])
# 	   # print(massage)

@app.route('/redirecting',methods=['POST','GET'])
def different_platform():
   print("=========================================================================")
   medicine=request.form['medicine']
   symptom = request.form['symptom']
   print(medicine)
   print(symptom)
   if (symptom=="akhil"):
	   # print("rinvrinvirnvirctvusbhnjmkcjbhgfc")
	   return redirect(url_for('checkmedicine',medicine=medicine))
   else:
	   if (medicine=="akhil"):
		   # print(" ia m here aldos")
		   return redirect(url_for('find',symptom=symptom))

   # return redirect(url_for('findw',medicine=medicine))

@app.route('/sysmptom/<symptom>',methods=['POST','GET'])
def find(symptom):
	# print("i am n=in syoion")
	massage,check1=healthline.healthline_web_scraping(symptom)
	   # print(check1[0])
	return render_template('index.html',msg="For your given symtom "+symptom+" these are top three result:-",msg1=check1[0],msg2=check1[1],msg3=check1[2])
	 # print(massage)

@app.route('/medicine/<medicine>',methods=['POST','GET'])
def checkmedicine(medicine):
	   print("i am n=in medicine====================================================================")
	   # print("i amgejgei")
	   massag,checkingm=check.checkmedicine(medicine)
	   print(checkingm)
	   return render_template('index.html',msg4="Your medicine "+medicine+" do following thing:-",msg5=checkingm)
	   # print(massage)


@app.route('/chatwithdoctor', methods=['POST', 'GET'])
def move_forward():
	print("Moving Forward...")
	return render_template('session.html')

if __name__ == '__main__':
   app.run(debug = True)


@app.route('/doctor/nisndi/bvdvnd/vnvdjvn', methods=['POST', 'GET'])
def sign():
	print("Moving Forward...")
	return render_template('signup.html')

mysql = MySQL()
con=mysql.connection
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = "******"
app.config['MYSQL_DB'] = "hac"
# cur = mysql.connection.cursor()
# cur.execute('CREATE DATABASE IF NOT EXISTS DBName;')
# app.config['MYSQL_DB'] = "DBName"
# mysql.init_app(app)
# cur = mysql.connection.cursor()
# # cur.config[.cursor()
# cur.execute('CREATE TABLE IF NOT EXISTS deepak(hi int);')
# app.config['MYSQL_DATABASE_DB'] = 'EmpData'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

# @app.route('/',methods=['POST','GET'])
# def index():
#     print('hihihih'+url_for('index'))
#     return render_template('signup.html')

    # return 'arhul, World!'


@app.route('/test2',methods=['POST','GET'])
def signup():
	registration_number=request.form['registration_number']
	name=request.form['name']
	email=request.form['email']
	password1=request.form['password1']
	password2=request.form['password2']
	online="online"
	print(registration_number,name,email,password1,password2,online)
    # print('hihihih2'+url_for('create_account'))
	cur = mysql.connection.cursor()
    # cur.execute('CREATE DATABASE IF NOT EXISTS DBName;')
    # app.config['MYSQL_DB'] = "DBName"
    # mysql.init_app(app)
    # cur = mysql.connection.cursor()
    # cur.config[.cursor()
	if password1!=password2:
		return redirect(url_for('index'))
	else:
		try:
			cur.execute('CREATE TABLE IF NOT EXISTS doctor(registration_number varchar(100),name varchar(100),email varchar(100),password varchar(100),online varchar(100),PRIMARY KEY (registration_number));')
			cur.execute("INSERT INTO doctor VALUES(%s,%s,%s,%s,%s)",(registration_number,name,email,password1,online));
			mysql.connection.commit()
			return redirect(url_for('account',username=registration_number))
		except Exception as e:
			return redirect(url_for('index'))

@app.route('/test3',methods=['POST','GET'])
def signin():
	registration_number=request.form['registration_number']
	password=request.form['password']
	cur = mysql.connection.cursor()
	print(registration_number+"---------------------------------------------------------------------")
	cur.execute("select password from doctor where registration_number= %s",(registration_number,));
	query_string=cur.fetchall()
	print(password+" = =hiehif+  = ================================================= "+(query_string[0][0]))
	# str(query_string)
    # con.commit()
	if  ((str(query_string[0][0]))!=str(password)):
		return redirect(url_for('index'))
	else:
		print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		return redirect(url_for('account',registration_number=registration_number))
    # try:
    #     cur.execute("select password from user where username VALUES(%s)",(username))
    #     return 'succesfull'
    # except Exception as e:
        # return 'not succesfuull'
        # return redirect(url_for('index'))

@app.route('/doctor/<registration_number>',methods=['POST','GET'])
def account(registration_number):
	print("vinvirv******************************************************************************************* = ",registration_number)
	cur = mysql.connection.cursor()
	cur.execute("select name from doctor where registration_number= %s",(registration_number,));
	query_string=cur.fetchall()
	# print()
	# print(str(query_string));
	return render_template('account.html',username=(str(query_string[0][0])))

if __name__ == '__main__':
   app.run(debug = True)

#=====================================================\

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
	print('received my event: ' + str(json))
	socketio.emit('my response', json, callback=messageReceived)

@socketio.on('online_doctor')
def online_doctor():
    print("svybnmo,xposd v bnmodicdomvomeov =-=-=-=-=-")
    # now = datetime.datetime.now()
    # print('- =- =-= -= '+str(data['post'])+' - == -++ '+str(data['author'])+str(now))
    cur = mysql.connection.cursor()
    # cur.execute('CREATE TABLE IF NOT EXISTS blog(author varchar(100),post varchar(100),time varchar(100));')
    cur.execute("select json_object('name',`name`) from doctor where online='online';");
    mysql.connection.commit();
    myresult = cur.fetchall()
    # print("========================================================================================")
    print(myresult)
	# print("========================================================================================")
    # print(myresult)
    # print("========================================================================================")
    s1 = json.dumps(myresult)
    # print(s1)
    # print("========================================================================================")
    m1=json.loads((s1));
    # print(m1)

    # print("========================================================================================")
    # print(m1)
    m1.reverse()
    for x in m1:
        print(x[0])
        p = json.loads(x[0]);
        # print(p["post"])
        socketio.emit('online_doctor', p)

    # socketio.emit('', p)

    # p = json.loads(m1[0][0]);
    # print((p["post"]))
    # for x in myresult:
    #     print(x[0][1])
    # for x in myresult:
    #     # var obj = json.load(x);
    #     print((x[0]["post"]))
    # socketio.emit('update_post', {'data': 42})
