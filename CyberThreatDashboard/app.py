from flask import Flask, render_template, redirect, url_for, request, flash, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from io import BytesIO
from fpdf import FPDF

app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Dummy users for demonstration
users = {
    "admin": {"password": generate_password_hash("admin123")}
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

# Forms
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")

@app.route("/")
def index():
    return redirect(url_for("dashboard"))

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users and check_password_hash(users[username]["password"], password):
            user = User(username)
            login_user(user)
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid credentials")
    return render_template("login.html", form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/dashboard")
@login_required
def dashboard():
    # Dummy data for display
    incidents = [
        {"ioc": "192.168.1.1", "country": "US", "abuseScore": 85, "time": "2025-08-29 16:00", "severity": "High", "type": "Port Scan", "actions": ["Block IP", "Notify Admin"]},
        {"ioc": "10.0.0.5", "country": "IN", "abuseScore": 60, "time": "2025-08-29 15:50", "severity": "Medium", "type": "Brute Force", "actions": ["Monitor", "Limit Attempts"]}
    ]
    top_actions = ["Block IP", "Notify Admin", "Monitor", "Limit Attempts", "Update Firewall", "Patch System"]
    counts = {"High": 1, "Medium": 1, "Low": 0}
    trend = [{"time": "2025-08-29 15:00", "counts": {"High": 0, "Medium": 1, "Low": 0}},
             {"time": "2025-08-29 16:00", "counts": {"High": 1, "Medium": 1, "Low": 0}}]
    return render_template("dashboard.html", incidents=incidents, top_actions=top_actions, counts=counts, trend=trend)

@app.route("/refresh_feed")
@login_required
def refresh_feed():
    # Dummy feed
    data = [
        {"ioc": "192.168.1.1", "country": "US", "abuseScore": 85, "lastReported": "2025-08-29 16:00"},
        {"ioc": "10.0.0.5", "country": "IN", "abuseScore": 60, "lastReported": "2025-08-29 15:50"}
    ]
    return {"data": data}

# ----------------- Added Routes for Download & Email Report ----------------- #

@app.route("/download_report")
@login_required
def download_report():
    # Create PDF in memory
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Cyber Threat Intelligence Report", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt="This is your downloadable threat report.", ln=True)

    # Save PDF to BytesIO buffer
    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    # Send file to browser
    return send_file(buffer, as_attachment=True, download_name="Threat_Report.pdf", mimetype='application/pdf')

@app.route("/email_report")
@login_required
def email_report():
    return "Email report route is working! Configure SMTP to send emails."

# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    app.run(debug=True)
