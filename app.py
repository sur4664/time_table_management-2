from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Landing Page
@app.route('/')
def home():
    return render_template('index.html')

# Teacher Page
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')

# Student Page
@app.route('/student')
def student():
    return render_template('student.html')

# Sample route for student events (dynamic content for FullCalendar)
@app.route('/api/student-events')
def student_events():
    sem = request.args.get('sem')
    section = request.args.get('section')
    # For simplicity, returning a static list of events. Replace with actual data fetching logic.
    events = [
        {
            "title": "Math Class",
            "start": "2024-07-03T10:00:00",
            "end": "2024-07-03T11:00:00"
        },
        {
            "title": "Science Class",
            "start": "2024-07-04T12:00:00",
            "end": "2024-07-04T13:00:00"
        }
    ]
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
