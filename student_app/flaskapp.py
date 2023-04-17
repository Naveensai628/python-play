from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import psycopg2

app=Flask(__name__)

conn = psycopg2.connect(
   database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5432'
)

#Student script

@app.route("/student",methods=['GET','POST'])
def student():
   cursor = conn.cursor()
   s="SELECT * FROM students"
   cursor.execute(s)
   # cursor.execute(c) 
   list_std = cursor.fetchall()
   # list_crs = cursor.fetchall()
  #  print(list_std)
  #  return 'check logs for data'
   return render_template('index.html', list_std = list_std)


@app.route("/student/add", methods=["POST","GET"])
def studentadd():
  sel_cur = conn.cursor()
  s="select max(id) from students"
  sel_cur.execute(s)
  max_id=sel_cur.fetchall()

  #to change list to int and get max of string
  for element in max_id:
    max_num=int(element[0])

  try:
    if request.method == 'POST':
      max_num=max_num+1
      # return str(max_num)
      fname = request.form['fname']
      lname = request.form['lname']
      dob = request.form['dateob']
      dateOfBirth = datetime.strptime(dob, '%Y-%m-%d').date()

      creation_date=datetime.now()
      last_update_date =datetime.now()

      ins_cur=conn.cursor()
      print(max_num, fname, lname, type(dateOfBirth), str(creation_date), str(last_update_date))
      ins_cur.execute("INSERT INTO students (id, first_name, last_name,dob, creation_date, last_update_date) values (%s,%s,%s,%s,%s,%s)",
                      (max_num, fname, lname, dateOfBirth, creation_date, last_update_date))
      conn.commit()
      return redirect(url_for('student'))
  except:
    return render_template('insertFailure.html')

@app.route('/student/delete/<string:id>', methods=['POST','GET'])
def studentdel(id):
   del_cur = conn.cursor()
   del_cur.execute("DELETE FROM STUDENTS WHERE id ={0}".format(id))
   conn.commit()
   return redirect(url_for('home'))

@app.route('/student/update/<int:id>/<first>/<last>/<birthdate>', methods=["POST","GET"])
def studentupd(id, first, last, birthdate):
   upd_cur = conn.cursor()
   birth = datetime.strptime(birthdate, '%Y-%m-%d').date()
   last_update_date =datetime.now()
   upd_cur=conn.cursor()
  #  print(max_num, fname, lname, type(dateOfBirth), str(creation_date), str(last_update_date))
   upd_cur.execute("UPDATE STUDENTS SET first_name='{1}',last_name='{2}',dob='{3}',last_update_date='{4}' where id={0}".format(id, first, last, birth, last_update_date))        
   conn.commit()   
   return 'updated'


#Cources script
@app.route("/course",methods=['GET','POST'])
def course():
   cur = conn.cursor()
   c="select * from courses"
   cur.execute(c) 
   list_crs = cur.fetchall()
   # list_crs = cursor.fetchall()
  #  print(list_std)
  #  return 'check logs for data'
   return render_template('index.html', list_crs = list_crs)


@app.route("/course/add", methods=["POST","GET"])
def courceadd():
  sel_cur = conn.cursor()
  s="select max(id) from courses"
  sel_cur.execute(s)
  max_id=sel_cur.fetchall()

#   to change list to int and get max of string
  
  for element in max_id:
    max_num=int(element[0])

  try:
    if request.method == 'POST':
      max_num=max_num+1
      # return str(max_num)
      cname = request.form['cname']
      desc = request.form['desc']
      aflag = request.form['activeflag']
      creation_date=datetime.now()
      last_update_date =datetime.now()

      ins_cur=conn.cursor()
      print(max_num, cname, desc, aflag, str(creation_date), str(last_update_date))
      ins_cur.execute("INSERT INTO courses (id, course_name, description,active_flag, creation_date, last_update_date) values (%s,%s,%s,%s,%s,%s)",
                      (max_num, cname, desc, aflag, creation_date, last_update_date))
      conn.commit()
      return redirect(url_for('course'))
  except:
    return render_template('insertFailure.html')

@app.route('/course/delete/<string:id>', methods=['POST','GET'])
def coursedel(id):
   del_cur = conn.cursor()
   del_cur.execute("DELETE FROM courses WHERE id ={0}".format(id))
   conn.commit()
   return redirect(url_for('course'))

# @app.route('/student/update/<int:id>/<first>/<last>/<birthdate>', methods=["POST","GET"])
# def studentupd(id, first, last, birthdate):
#    upd_cur = conn.cursor()
#    birth = datetime.strptime(birthdate, '%Y-%m-%d').date()
#    last_update_date =datetime.now()
#    upd_cur=conn.cursor()
#   #  print(max_num, fname, lname, type(dateOfBirth), str(creation_date), str(last_update_date))
#    upd_cur.execute("UPDATE STUDENTS SET first_name='{1}',last_name='{2}',dob='{3}',last_update_date='{4}' where id={0}".format(id, first, last, birth, last_update_date))        
#    conn.commit()   
#    return 'updated'
  


  

if __name__ == '__main__':
    app.run(debug= True)