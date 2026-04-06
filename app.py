from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# ---------- AUTO CREATE TABLE ----------
def init_db():
    conn = sqlite3.connect("registrations.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registrations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        department TEXT NOT NULL,
        batch TEXT NOT NULL,
        ku_id TEXT NOT NULL,
        enrollment_number TEXT NOT NULL,
        event_name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

# Run DB setup when app starts
init_db()

# ---------- HOME / REGISTRATION FORM ----------
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        full_name = request.form["full_name"]
        department = request.form["department"]
        batch = request.form["batch"]
        ku_id = request.form["ku_id"]
        enrollment_number = request.form["enrollment_number"]
        event_name = request.form["event_name"]

        conn = sqlite3.connect("registrations.db")
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO registrations
            (full_name, department, batch, ku_id, enrollment_number, event_name)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (full_name, department, batch, ku_id, enrollment_number, event_name))

        conn.commit()
        conn.close()

        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Registration Successful</title>
            <style>
                * {
                    box-sizing: border-box;
                }
                body {
                    font-family: 'Segoe UI', Arial, sans-serif;
                    background: linear-gradient(135deg, #1e1b4b, #4c1d95, #be185d, #f59e0b);
                    background-size: 400% 400%;
                    animation: gradientMove 12s ease infinite;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                }
                @keyframes gradientMove {
                    0% { background-position: 0% 50%; }
                    50% { background-position: 100% 50%; }
                    100% { background-position: 0% 50%; }
                }
                .success-box {
                    background: rgba(255, 255, 255, 0.18);
                    backdrop-filter: blur(18px);
                    -webkit-backdrop-filter: blur(18px);
                    border: 1px solid rgba(255, 255, 255, 0.25);
                    padding: 40px;
                    border-radius: 24px;
                    box-shadow: 0 12px 35px rgba(0,0,0,0.25);
                    text-align: center;
                    width: 90%;
                    max-width: 550px;
                    color: white;
                }
                h1 {
                    margin-bottom: 15px;
                    font-size: 32px;
                }
                p {
                    font-size: 18px;
                    margin-bottom: 28px;
                    line-height: 1.6;
                }
                a {
                    display: inline-block;
                    margin: 8px;
                    text-decoration: none;
                    background: linear-gradient(90deg, #8b5cf6, #ec4899);
                    color: white;
                    padding: 13px 24px;
                    border-radius: 14px;
                    font-weight: bold;
                    transition: 0.3s ease;
                    box-shadow: 0 6px 18px rgba(0,0,0,0.2);
                }
                a:hover {
                    transform: translateY(-2px) scale(1.03);
                    opacity: 0.95;
                }
            </style>
        </head>
        <body>
            <div class="success-box">
                <h1>🎉 Registration Successful</h1>
                <p>Thank you, <strong>{{ full_name }}</strong>!<br>Your registration for <strong>{{ event_name }}</strong> has been saved successfully.</p>
                <a href="/">Register Another Student</a>
                <a href="/view">View Registrations</a>
            </div>
        </body>
        </html>
        """, full_name=full_name, event_name=event_name)

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>College Event Registration</title>
        <style>
            * {
                box-sizing: border-box;
            }
            body {
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #1e1b4b, #4c1d95, #be185d, #f59e0b);
                background-size: 400% 400%;
                animation: gradientMove 12s ease infinite;
                margin: 0;
                padding: 30px 15px;
                min-height: 100vh;
            }
            @keyframes gradientMove {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            .container {
                width: 95%;
                max-width: 720px;
                margin: 20px auto;
                background: rgba(255, 255, 255, 0.18);
                backdrop-filter: blur(18px);
                -webkit-backdrop-filter: blur(18px);
                border: 1px solid rgba(255, 255, 255, 0.25);
                padding: 35px;
                border-radius: 28px;
                box-shadow: 0 12px 35px rgba(0,0,0,0.25);
                color: white;
            }
            h1 {
                text-align: center;
                margin-bottom: 10px;
                font-size: 34px;
            }
            .subtitle {
                text-align: center;
                margin-bottom: 28px;
                color: #fdf4ff;
                font-size: 16px;
            }
            label {
                display: block;
                margin-top: 16px;
                margin-bottom: 7px;
                font-weight: 600;
                font-size: 15px;
            }
            input, select {
                width: 100%;
                padding: 13px 14px;
                border: none;
                border-radius: 14px;
                font-size: 15px;
                background: rgba(255, 255, 255, 0.9);
                color: #111827;
                outline: none;
            }
            input:focus, select:focus {
                box-shadow: 0 0 0 4px rgba(255,255,255,0.25);
            }
            button {
                width: 100%;
                margin-top: 28px;
                background: linear-gradient(90deg, #8b5cf6, #ec4899);
                color: white;
                border: none;
                padding: 15px;
                font-size: 17px;
                border-radius: 16px;
                cursor: pointer;
                font-weight: bold;
                transition: 0.3s ease;
                box-shadow: 0 8px 22px rgba(0,0,0,0.2);
            }
            button:hover {
                transform: translateY(-2px) scale(1.01);
                opacity: 0.95;
            }
            .view-link {
                display: block;
                text-align: center;
                margin-top: 22px;
                text-decoration: none;
                color: white;
                font-weight: bold;
                font-size: 16px;
            }
            .view-link:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>✨ College Event Registration</h1>
            <p class="subtitle">Register students for exciting college events with style 🎓</p>

            <form method="POST">
                <label>Full Name</label>
                <input type="text" name="full_name" required>

                <label>Department</label>
                <input type="text" name="department" placeholder="e.g. B.Tech CSE" required>

                <label>Batch</label>
                <input type="text" name="batch" placeholder="e.g. 2023-2027" required>

                <label>KU ID</label>
                <input type="text" name="ku_id" required>

                <label>Enrollment Number</label>
                <input type="text" name="enrollment_number" required>

                <label>Select Event</label>
                <select name="event_name" required>
                    <option value="">-- Select an Event --</option>
                    <option value="Cyber Forensic Seminar">Cyber Forensic Seminar</option>
                    <option value="Lok Sabha">Lok Sabha</option>
                    <option value="ARVR">ARVR</option>
                    <option value="Treasure Hunt">Treasure Hunt</option>
                    <option value="Cooking Contest">Cooking Contest</option>
                    <option value="Coding Competition">Coding Competition</option>
                    <option value="Hackathon">Hackathon</option>
                    <option value="Debate Competition">Debate Competition</option>
                    <option value="Poster Presentation">Poster Presentation</option>
                    <option value="Robotics Workshop">Robotics Workshop</option>
                </select>

                <button type="submit">Submit Registration</button>
            </form>

            <a class="view-link" href="/view">📋 View All Registrations</a>
        </div>
    </body>
    </html>
    """)

# ---------- VIEW REGISTRATIONS ----------
@app.route("/view")
def view_registrations():
    conn = sqlite3.connect("registrations.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, full_name, department, batch, ku_id, enrollment_number, event_name
        FROM registrations
        ORDER BY id DESC
    """)
    rows = cursor.fetchall()

    conn.close()

    table_rows = ""
    for row in rows:
        table_rows += f"""
        <tr>
            <td>{row[0]}</td>
            <td>{row[1]}</td>
            <td>{row[2]}</td>
            <td>{row[3]}</td>
            <td>{row[4]}</td>
            <td>{row[5]}</td>
            <td>{row[6]}</td>
        </tr>
        """

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>View Registrations</title>
        <style>
            * {{
                box-sizing: border-box;
            }}
            body {{
                font-family: 'Segoe UI', Arial, sans-serif;
                background: linear-gradient(135deg, #1e1b4b, #4c1d95, #be185d, #f59e0b);
                background-size: 400% 400%;
                animation: gradientMove 12s ease infinite;
                margin: 0;
                padding: 25px 12px;
                min-height: 100vh;
            }}
            @keyframes gradientMove {{
                0% {{ background-position: 0% 50%; }}
                50% {{ background-position: 100% 50%; }}
                100% {{ background-position: 0% 50%; }}
            }}
            .container {{
                width: 97%;
                max-width: 1250px;
                margin: auto;
                background: rgba(255, 255, 255, 0.18);
                backdrop-filter: blur(18px);
                -webkit-backdrop-filter: blur(18px);
                border: 1px solid rgba(255, 255, 255, 0.25);
                padding: 30px;
                border-radius: 26px;
                box-shadow: 0 12px 35px rgba(0,0,0,0.25);
                color: white;
            }}
            h1 {{
                text-align: center;
                margin-bottom: 22px;
                font-size: 32px;
            }}
            .table-wrap {{
                overflow-x: auto;
            }}
            table {{
                width: 100%;
                border-collapse: collapse;
                margin-top: 10px;
                background: rgba(255,255,255,0.08);
                border-radius: 14px;
                overflow: hidden;
            }}
            th, td {{
                padding: 12px;
                text-align: center;
                border-bottom: 1px solid rgba(255,255,255,0.15);
                font-size: 14px;
            }}
            th {{
                background: rgba(255,255,255,0.18);
                color: #ffffff;
                font-weight: 700;
            }}
            tr:hover {{
                background: rgba(255,255,255,0.08);
            }}
            .back-link {{
                display: inline-block;
                margin-top: 24px;
                text-decoration: none;
                background: linear-gradient(90deg, #8b5cf6, #ec4899);
                color: white;
                padding: 12px 22px;
                border-radius: 14px;
                font-weight: bold;
                transition: 0.3s ease;
            }}
            .back-link:hover {{
                transform: translateY(-2px);
            }}
            .empty-note {{
                text-align: center;
                margin-top: 20px;
                font-size: 16px;
                color: #fdf4ff;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📋 All Student Registrations</h1>
            <div class="table-wrap">
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Full Name</th>
                        <th>Department</th>
                        <th>Batch</th>
                        <th>KU ID</th>
                        <th>Enrollment Number</th>
                        <th>Event Name</th>
                    </tr>
                    {table_rows}
                </table>
            </div>
            <a class="back-link" href="/">⬅ Back to Registration Form</a>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
