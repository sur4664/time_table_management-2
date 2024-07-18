from flask import Flask, request, jsonify,render_template,redirect,url_for,session
import mysql.connector
from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import json

# Import Flask

# Continue with the rest of your Flask app setup...

app = Flask(__name__)

# Generate a secret key
import os
import binascii

secret_key = binascii.hexlify(os.urandom(24)).decode()
print("Secret Key:", secret_key)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'default_secret_key')

# You can then manually set this as an environment variable or use it directly in your app
connection = get_sql_connection()

@app.route('/')
def home():
    return render_template('index.html')

# Teacher Page
@app.route('/teacher')
def teacher():
    
    return render_template('teacher2.html')

# Student Page
@app.route('/student')
def student():
    return render_template('student2.html')

# Database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="newschema",
        port="3305"
    )
    return connection

@app.route('/api/student-events', methods=['POST','GET'])
def get_student_events():
  if request.method == 'POST':
    data = request.json
    sem=data['sem']
    section=data['section']
 

    connection = get_db_connection()
    print("connected")
    cursor = connection.cursor(dictionary=True)
    print("cursor")
    query = ("SELECT * FROM tt WHERE sem_no = %s AND section = %s")
    print("query")
    cursor.execute(query,( sem, section))
    print("executed")
    events = cursor.fetchall()
    print("fetched")
    # for row in events:
    #     print(row)
    #print('events',events)
    cursor.close()
    connection.close()
    from collections import defaultdict

    timetable = defaultdict(lambda: defaultdict(list))

    for event in events:
        timetable[event['day']][event['time']].append(event)

    days_order = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6}
    time_order = {
    '9:00': 1, '10:00': 2, '11:15':3 , '12:15':4 ,'1:00': 5, '2:00': 6, '3:00': 7, '4:00':8
   
}
    # Sort days according to the custom order
    sorted_days = sorted(timetable.keys(), key=lambda day: days_order[day])

    # Sort times as before
    sorted_times = sorted(set(time for day in timetable.values() for time in day),key=lambda time:time_order[time])

    # Continue with the rest of your code
    session['timetable'] = timetable
    session['sorted_days'] = sorted_days
    session['sorted_times'] = sorted_times
    return redirect(url_for('display'))
  return render_template('student3.html', timetable=timetable, sorted_days=sorted_days, sorted_times=sorted_times)

@app.route('/view_tt', methods=['GET', 'POST'])
def get_teacher_events():
  if request.method == 'POST':

    connection = get_db_connection()
    print("connected")
    cursor = connection.cursor(dictionary=True)
    print("cursor")
    tname=login_db['name']
    query = ("SELECT * FROM tt WHERE teacher_name=%s")
    print("query")
    cursor.execute(query,( tname,))
    print("executed")
    events = cursor.fetchall()
    print("fetched")
    for row in events:
        print(row)
    #print('events',events)
    cursor.close()
    connection.close()
    from collections import defaultdict

    timetable = defaultdict(lambda: defaultdict(list))

    for event in events:
        timetable[event['day']][event['time']].append(event)

    days_order = {'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6}
    time_order = {
    '9:00': 1, '10:00': 2, '11:15':3 , '12:15':4 ,'1:00': 5, '2:00': 6, '3:00': 7, '4:00':8
   
}
    # Sort days according to the custom order
    sorted_days = sorted(timetable.keys(), key=lambda day: days_order[day])

    # Sort times as before
    sorted_times = sorted(set(time for day in timetable.values() for time in day),key=lambda time:time_order[time])

    # Continue with the rest of your code
    session['timetable'] = timetable
    session['sorted_days'] = sorted_days
    session['sorted_times'] = sorted_times
    return redirect(url_for('displayt'))
  
  return render_template('teacher3.html', timetable=timetable, sorted_days=sorted_days, sorted_times=sorted_times)


@app.route('/displayt', methods=['GET'])
def displayt():
    timetable = session.get('timetable', {})
    sorted_days = session.get('sorted_days', [])
    sorted_times = session.get('sorted_times', [])
  
    print(timetable)
    print(sorted_days)
    print('hiii')
    return render_template('teacher3.html', timetable=timetable, sorted_days=sorted_days, sorted_times=sorted_times)



@app.route('/display', methods=['GET'])
def display():
    
    timetable = session.get('timetable', {})
    sorted_days = session.get('sorted_days', [])
    sorted_times = session.get('sorted_times', [])
  
    print(timetable)
    print(sorted_days)
    print('hiii')
    return render_template('student3.html', timetable=timetable, sorted_days=sorted_days, sorted_times=sorted_times)


@app.route('/api/schedule', methods=['POST'])
def schedule_class():
    data = request.json
    sem = data['sem']
    section = data['section']
    subject = data['subject']
    time = data['time']
    day = data['day']
    #tid=data['teacherId']
    tname=login_db['name']
    conn = get_db_connection()
    cursor = conn.cursor()


#     cursor.execute('''
#         INSERT INTO tt (sem_no, section, sub, time, day, teacher_name, teacher_id)
# SELECT %s, %s, %s, %s, %s, %s, %s
# WHERE NOT EXISTS (
#     SELECT 1 FROM tt
#     WHERE sem_no = %s AND section = %s AND day = %s AND time = %s
# )''', (sem, section, subject, time, day, tname, tid, sem, section, day, time))
#     conn.commit()
    cursor.execute('''
    INSERT INTO tt (sem_no, section, sub, time, day, teacher_name)
SELECT %s, %s, %s, %s, %s, %s
WHERE NOT EXISTS (
    SELECT 1 FROM tt
    WHERE (sem_no = %s AND section = %s AND day = %s AND time = %s)
    OR (teacher_name = %s AND day = %s AND time = %s)
)''', (sem, section, subject, time, day, tname, sem, section, day, time,tname, day, time))
    conn.commit()
    if cursor.rowcount > 0:
        print("Class scheduled successfully.")
        response_message = {'message': 'Class scheduled successfully'}
        status_code = 201
    else:
        connection=get_db_connection()
        cursor2 = connection.cursor()
        cursor2.execute('''
    SELECT 1 FROM tt
    WHERE sem_no = %s AND section = %s AND day = %s AND time = %s
    ''', (sem, section, day, time))
        conn.commit()
        
        rows=cursor2.fetchall()
        if not rows:
            print("Class not scheduled. A class already exists for the specified sem_no, section, day, and time.")
            response_message = {'message': 'Class not scheduled. A class already exists for the specified sem_no, section, day, and time.'}
            status_code = 500
        else:
            print("{tname} is already scheduled for another class at the same time.")
            response_message = {'message': 'Class not scheduled. Teacher is already scheduled for another class at the same time.'}
            status_code = 409  # 409 Conflict

    cursor.close()
    conn.close()

    return jsonify(response_message),status_code

from flask import Flask, render_template, request, redirect, url_for, flash
# Example content of authentication.py

# This is a placeholder for actual authentication logic
# In a real application, you would check against a database or an authentication service
# def authenticate_teacher(email, password):
#     # Placeholder for authentication logic
#     # For demonstration, let's assume these are the valid credentials
#     valid_email = "teacher@example.com"
#     valid_password = "securepassword"
    
#     if email == valid_email and password == valid_password:
#         return True
#     else:
#         return False


# @app.route('/teacher_login', methods=['GET', 'POST'])
# def teacher_login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']
#         # Authenticate teacher
#         if authenticate_teacher(email, password):
#             # Redirect to teacher dashboard or another page
#             print("Teacher authenticated")
#             return redirect(url_for('teacher_dashboard'))
#         else:
#             flash('Invalid email or password', 'danger')
#             return redirect(url_for('teacher_login'))
#     return render_template('login.html')

users_db = {}
login_db = {}

@app.route('/teacher_signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash('Passwords do not match! Please try again.', 'danger')
            return redirect(url_for('signup'))

       
        connection = get_db_connection()
        print("connected")
        cursor = connection.cursor(dictionary=True)

        # Check if email already exists
        cursor.execute("SELECT emaill FROM teachers WHERE emaill = %s", (email,))
        if cursor.fetchone():
            flash('Email already exists! Please login.', 'danger')
            cursor.close()
            
            return redirect(url_for('login'))

        # Insert new teacher into the database
        insert_query = "INSERT INTO teachers (teacher_name, emaill, password) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, email, password))
        connection.commit()

        flash('Signup successful! Please login.', 'success')
        cursor.close()
        connection.close()
        return redirect(url_for('login'))

    return render_template('login_signup.html')

@app.route('/teacher_login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

         # Connect to the database
        cnx = get_db_connection()
        cursor = cnx.cursor()

        # Execute SELECT query
        query = "SELECT * FROM teachers WHERE emaill = %s AND password = %s"
        cursor.execute(query, (email, password))
        result = cursor.fetchone()

        cursor.close()
        cnx.close()

        if result:
            # Redirect to a protected page or dashboard here
            login_db['name'] = result[1]
            print(login_db)
            return redirect(url_for('teacher_dashboard'))
        else:
            flash('Invalid email or password', 'danger')
            return redirect(url_for('signup'))
    return render_template('login.html')


@app.route('/teacher_dashboard')
def teacher_dashboard():
    return render_template('teacher_dashboard.html')



@app.route('/delete_class', methods=['POST'])
def delete_class():
    return render_template('delete_class.html')

@app.route('/api/delete', methods=['POST'])
def delete():
    data = request.json
    sem = data['sem']
    section = data['section']
    time = data['time']
    day = data['day']
    print(data)

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tt WHERE sem_no = %s AND section = %s AND day = %s AND time = %s;', ( sem, section, day, time))
    conn.commit()
 

    cursor.close()
    conn.close()

    return jsonify({'message': 'Class deleted successfully'}), 201


@app.route('/add_subject', methods=['POST','GET'])
def add_subject():
    return render_template('add_subject.html')

@app.route('/api/add_sub',methods=['POST'])
def add_sub():
    data=request.json
    sem=data['sem']
    sub=data['subject']
    credits=data['credits']

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("UPDATE sems SET no_of_subs = no_of_subs+1 WHERE sem_no = %s", (sem,))

    if cursor.rowcount == 0:
    # Step 3: Insert because update was unsuccessful
        cursor.execute("INSERT INTO sems (sem_no, no_of_subs) VALUES (%s, %s)", (sem, 1))

    cursor.execute('''
        INSERT INTO subjs (sem_no, credits, sub) VALUES (%s, %s, %s)''', (sem,credits, sub))
    conn.commit()
 
    cursor.close()
    conn.close()

    return jsonify({'message': 'sub added succesfully'}), 201




@app.route('/getSubjects')
def get_subjects():
    sem = request.args.get('sem', type=int)
    subjects = query_subjects(sem)
    return jsonify(subjects)

def query_subjects(sem):
    # Assuming you have a SQLite database for simplicity
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT sub FROM subjs WHERE sem_no = %s", (sem,))
    subjects = [ row[0] for row in cursor.fetchall()]
    print(subjects)
    conn.close()
    return subjects

 
if __name__ == '__main__':
    app.debug = True
    app.run(debug=True)
