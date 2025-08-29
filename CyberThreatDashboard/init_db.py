# init_db.py
from app import app, db, User
from werkzeug.security import generate_password_hash
import pyotp

# Use app context
with app.app_context():
    # Create tables
    db.create_all()

    # Check if admin already exists
    if not User.query.filter_by(username="admin").first():
        admin_user = User(
            username="admin",
            pw_hash=generate_password_hash("yourpassword123"),  # replace with a strong password
            email="youremail@example.com",
            role="admin",
            otp_secret=pyotp.random_base32()  # generates a 2FA secret
        )
        db.session.add(admin_user)
        db.session.commit()
        print("Admin user created successfully!")
        print(f"Username: {admin_user.username}")
        print(f"Password: yourpassword123")
        print(f"2FA Secret: {admin_user.otp_secret}")
    else:
        print("Admin user already exists.")
