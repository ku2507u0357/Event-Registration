from flask import Flask, request, redirect, render_template
import requests

app = Flask(__name__)

# ✅ YOUR FIREBASE DATABASE
FIREBASE_URL = "https://event-registration-ac3a3-default-rtdb.asia-southeast1.firebasedatabase.app/registrations.json"


# HOME PAGE → SHOW FORM
@app.route('/')
def home():
    return render_template('index.html')


# FORM SUBMIT
@app.route('/submit', methods=['POST'])
def submit():

    name = request.form.get('name')
    enrollment = request.form.get('enrollment')
    ku_id = request.form.get('ku_id')
    student_class = request.form.get('class')
    event_type = request.form.get('event_type')

    # MULTIPLE EVENTS
    events = request.form.getlist('event_name')

    # VALIDATION
    if not name or not enrollment or not ku_id or not student_class or not event_type or not events:
        return "❌ Please fill all fields"

    # DATA TO FIREBASE
    data = {
        "name": name,
        "enrollment": enrollment,
        "ku_id": ku_id,
        "class": student_class,
        "event_type": event_type,
        "events": events
    }

    # SEND TO FIREBASE
    response = requests.post(FIREBASE_URL, json=data)

    # ✅ DEBUG (NOW INSIDE FUNCTION)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        return redirect('/')
    else:
        return f"❌ Error: {response.text}"


# RUN APP
if __name__ == '__main__':
    app.run(debug=True)
