from flask import Flask, render_template, request

app = Flask(__name__)

# HOME ROUTE
@app.route('/')
def home():
    return render_template('index.html')


# FORM SUBMIT ROUTE
@app.route('/submit', methods=['POST'])
def submit():

    # Get data from form
    name = request.form.get('name')
    enrollment = request.form.get('enrollment')
    ku_id = request.form.get('ku_id')
    student_class = request.form.get('class')
    event_type = request.form.get('event_type')

    # MULTIPLE EVENTS (IMPORTANT)
    events = request.form.getlist('event_name')

    # Convert list to string
    events_str = ", ".join(events)

    # Print in terminal (for checking)
    print("----- NEW REGISTRATION -----")
    print("NAME:", name)
    print("ENROLLMENT:", enrollment)
    print("KU ID:", ku_id)
    print("CLASS:", student_class)
    print("EVENT TYPE:", event_type)
    print("EVENTS:", events_str)

    # Return success page
    return f"""
    <html>
    <head>
        <title>SUCCESS</title>
        <style>
            body {{
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                font-family: Arial;
                background: linear-gradient(135deg, #ff9a9e, #a18cd1);
                color: white;
            }}

            .box {{
                padding: 30px;
                border-radius: 15px;
                background: rgba(255,255,255,0.2);
                backdrop-filter: blur(12px);
                text-align: center;
            }}

            button {{
                margin-top: 15px;
                padding: 10px 15px;
                border: none;
                border-radius: 6px;
                background: white;
                cursor: pointer;
            }}
        </style>
    </head>

    <body>
        <div class="box">
            <h2>REGISTRATION SUCCESSFUL</h2>
            <p><b>NAME:</b> {name}</p>
            <p><b>EVENTS:</b> {events_str}</p>

            <button onclick="window.location.href='/'">
                GO BACK
            </button>
        </div>
    </body>
    </html>
    """


# ✅ CORRECT MAIN LINE (IMPORTANT FIX)
if __name__ == '__main__':
    app.run(debug=True)