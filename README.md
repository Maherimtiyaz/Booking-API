# 🏋️ Fitness Studio Booking API

## 📌 Overview

This project is a backend API built using **FastAPI** for managing bookings in a fictional fitness studio.

Users can:
- Sign up and log in
- Create fitness classes (Admin only)
- View upcoming classes
- Book classes
- View their bookings

Authentication is handled using **JWT tokens**.

---

## 🛠 Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- Passlib (bcrypt)
- Pydantic

---

## 📂 Project Structure

app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── dependencies.py
├── config.py
├── routers/
│ ├── users.py
│ ├── classes.py
│ └── bookings.py
└── utils/
└── timezone.py


---

## 🚀 Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd fitness-booking-api

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ .env

DATABASE_URL=postgresql+psycopg2://fitness_user:password@localhost:5432/fitness_booking_db
SECRET_KEY=your_secret_key
---

## 🚀 Running

uvicorn main:app --reload

http://127.0.0.1:8000/docs

## Postman Collection

You can import the full Postman collection for testing the API:

1. Open Postman → File → Import
2. Select `docs/postman/fitness_booking_api.postman_collection.json`
3. Run requests in order:

   - Auth → Signup/Login
   - Classes → Create/Get
   - Bookings → Book/Get
   - Edge Cases → Unauthorized requests

## Screenshots

### Signup User
![Signup](docs/postman/screenshots/signup.png)

### Login User
![Login](docs/postman/screenshots/UserLogin.png)

### Create Class (Admin)
![Create Class](docs/postman/screenshots/Booking_classes.png)

### Booking Successful
![Booking Success](docs/postman/screenshots/Get_User_booking.png)

### Duplicate Booking
![Duplicate Booking](docs/postman/screenshots/duplicate_booking.png)

### Overbooking Test
![Overbooking](docs/postman/screenshots/overbooking.png)
