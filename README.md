# 👤 User Management API with FastAPI + PostgreSQL

Welcome to your 🔐 **User Authentication & Management API**, built with **FastAPI**, **PostgreSQL**, **JWT tokens**, and **bcrypt** for secure password hashing. This project is a RESTful backend — no frontend required — and includes full documentation via Swagger UI.

---

## 📌 Project Features

- 🔐 **Register/Login** system using email & password
- 🧾 **JWT token authentication**
- 🗃️ **PostgreSQL database integration**
- 🔒 **Password hashing** with `bcrypt`
- 🚧 **Profile viewing/updating**, secured via token
- 📚 **Auto-generated Swagger UI documentation**
- 🧪 Test everything using Swagger or Postman

---

# Project Structure

The structure of the FastAPI project is as follows:

```plaintext
user_api_project/
│
├── app/                        # Application folder
│   ├── __init__.py             # Initialize the app package
│   ├── main.py                 # FastAPI entry point
│   ├── models.py               # SQLAlchemy models
│   ├── schemas.py              # Pydantic models (input/output)
│   ├── database.py             # DB engine & session setup
│   ├── crud.py                 # DB logic (Create, Read, Update, Delete operations)
│   ├── auth.py                 # JWT & password logic (authentication)
│   └── requirements.txt        # Project dependencies
│
└── README.md                   # Documentation file

```

---

## 🧰 Technologies Used

| Tool            | Description                              |
|-----------------|------------------------------------------|
| FastAPI         | High-performance Python web framework 🚀|
| PostgreSQL      | Relational database                      |
| SQLAlchemy      | ORM for DB interaction                   |
| Pydantic        | Input validation & schema modeling       |
| JWT (python-jose) | Secure authentication tokens           |
| bcrypt (passlib) | Password hashing                        |

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/user_api_project.git
cd user_api_project

**2️⃣ Create a Virtual Environment**

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

**3️⃣ Install Dependencies**

pip install -r requirements.txt

**4️⃣ Set Up PostgreSQL**

Make sure PostgreSQL is running

Create a database in pgAdmin or via CLI (e.g., CREATE DATABASE user_db)

Update your .env or database.py with correct DB credentials

**5️⃣ Run the API**

uvicorn app.main:app --reload

The server will start on http://127.0.0.1:8000

**🌐 Explore with Swagger UI**

Just go to:
👉 http://127.0.0.1:8000/docs
You’ll see live, interactive API docs with:

📝 /register – Register a new user

🔐 /login – Login and receive JWT token

🙋 /profile/{id} – View user profile (with token)

✏️ /profile/{id} – Update user data (with token)


**🔄 API Workflow Explained**

1. 📝 Register a New User
POST /register
Request:

{
  "name": "Alice",
  "email": "alice@example.com",
  "password": "secure123"
}

Response:

{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}

2. 🔐 Login
POST /login
Request:

{
  "email": "alice@example.com",
  "password": "secure123"
}

Response:

{
  "access_token": "JWT_TOKEN_HERE",
  "token_type": "bearer"
}

3. 👁️ Get Profile (Protected)
GET /profile/1
Headers:

Authorization: Bearer JWT_TOKEN_HERE

Response:

{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com"
}

4. ✏️ Update Profile (Protected)
PUT /profile/1
Headers:

Authorization: Bearer JWT_TOKEN_HERE

Request:

{
  "name": "Alice Updated",
  "email": "alice.updated@example.com"
}


**🧪 How to Test
✅ Use Swagger UI:**

Go to http://127.0.0.1:8000/docs

Click "Try it out" on each route

Paste JWT token into "Authorize" or manually in header as:

Bearer <your_token_here>

🧪 Use Postman:
1. Create requests for /register, /login, /profile/{id}

2. Add token to Authorization header as Bearer token_here

**⚙️ .env Format**

DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/user_db

SECRET_KEY=your_jwt_secret

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30


**📸 Screenshots**

![image](https://github.com/user-attachments/assets/6528bbe8-eeed-4c0e-927e-e9bd28692989)
![image](https://github.com/user-attachments/assets/8553cd40-4c6f-445b-9940-2f99d3d143ee)
![image](https://github.com/user-attachments/assets/5fdeb938-58fc-4cc9-b2bf-24cc72f0433d)
![image](https://github.com/user-attachments/assets/bc53abbe-2ebc-411e-8d6e-ac71e56953f8)
![image](https://github.com/user-attachments/assets/9e6bc948-4239-4a0b-b2e4-83234e0a1d34)

**🗒️ Explain Your Work**

This project is a simple user management system built using FastAPI and PostgreSQL. The goal was to create a RESTful API that handles user registration, login, and profile management with proper security practices like password hashing and JWT-based authentication.

The code begins with main.py, which defines the FastAPI application, sets up middleware, and declares the core routes (/register, /login, /profile/{id}). The PostgreSQL database connection is configured using SQLAlchemy in database.py, which initializes the engine and session maker. Upon starting the server, models.Base.metadata.create_all ensures all required database tables are created if they don't already exist.

Each endpoint works as follows:

POST /register: Takes user details, checks if the email is already registered, hashes the password using bcrypt, and saves the user to the database.

POST /login: Validates user credentials, and if correct, returns a JWT token used for authenticating protected routes.

GET /profile/{id} and PUT /profile/{id}: Both require a valid token. They allow users to view or update their profile data but only if their token matches the user ID being requested.

JWT handling is done in auth.py, which includes token generation and decoding. The password handling uses bcrypt (via passlib) for secure storage.

One challenge I faced was managing JWT authentication with proper error handling and ensuring the Authorization header was correctly used in Swagger UI. However, FastAPI's structure made it manageable and clean to implement.

Overall, this project demonstrates how to build a secure, modular, and database-connected API using modern Python web development practices.


**📣 Contact**
For questions or feedback, feel free to reach out!
