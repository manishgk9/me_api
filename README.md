# Me API with React UI

This project is a **full-stack application** built with **Django REST Framework (DRF)** for the backend and **React** for the frontend UI.

- **Backend**: Django + DRF
- **Frontend**: React (served by Django in production)
- **Deployment**: [PythonAnywhere](https://www.pythonanywhere.com/)

### 🔗 Live Links

- **Frontend (UI)** → [https://manizh.pythonanywhere.com/](https://manizh.pythonanywhere.com/)
- **API Base URL** → [https://manizh.pythonanywhere.com/api/](https://manizh.pythonanywhere.com/api/)
- **API Health Check URL** → [https://manizh.pythonanywhere.com/api/health/](https://manizh.pythonanywhere.com/api/health/)
- **Search user** → [https://manizh.pythonanywhere.com/api/profiles/?search=manish](https://manizh.pythonanywhere.com/api/profiles/?search=manish)
- **Search skill** → [https://manizh.pythonanywhere.com/api/projects/?search=django](https://manizh.pythonanywhere.com/api/projects/?search=django)

---

## 📂 Features

- User Authentication (Register & Login with Token)
- Manage **Profiles**, **Projects**, **Skills**, and **Work Experiences**
- Public search interface for finding users & projects
- Health check endpoint
- Register user
- Token Bassed Auth + Delete , Update , Post
- Pegination implemented

---

## 📌 API Endpoints

All endpoints are prefixed with:

```
https://manizh.pythonanywhere.com/api/
```

### 1️⃣ Health Check

**Endpoint**: `/health/`
**Method**: `GET`

📬 **Postman Example**

```http
GET https://manizh.pythonanywhere.com/api/health/
```

✅ **Response**

```json
{
  "status": "ok"
}
```

---

### 2️⃣ User Authentication

#### Register

**Endpoint**: `/auth/register/`
**Method**: `POST`

📬 **Postman Example**

```http
POST https://manizh.pythonanywhere.com/api/auth/register/

Body (JSON):
{
  "username": "testuser",
  "email": "testuser@gmail.com",
  "password": "testuser@123"
}
```

✅ **Response**

```json
{
  "id": 5,
  "username": "testuser",
  "email": "testuser@gmail.com"
}
```

---

#### Login (Get Token)

**Endpoint**: `/auth/token/`
**Method**: `POST`

📬 **Postman Example**

```http
POST https://manizh.pythonanywhere.com/api/auth/token/

Body (JSON):
{
  "username": "testuser",
  "password": "testuser@123"
}
```

✅ **Response**

```json
{
  "token": "user-auth-token-here"
}
```

---

### 3️⃣ Profiles

**Endpoint**: `/profiles/`

#### List Profiles

```http
GET https://manizh.pythonanywhere.com/api/profiles/
```

#### Create Profile (Requires Auth)

```http
POST https://manizh.pythonanywhere.com/api/profiles/

Headers:
Authorization: Token user-auth-token-here

Body (JSON):
{
  "full_name": "Test User",
  "email": "testuser@gmail.com",
  "education": "B.Tech in Computer Science",
  "bio": "This is a test user profile.",
  "github": "https://github.com/testuser",
  "linkedin": "https://linkedin.com/in/testuser",
  "portfolio": "https://testuser.github.io",
  "skills": [
    "python",
    "django",
   "rest api",
    "reactjs",
    "flutter",
    "drf",
    "celery"
  ]
}

```

---

### DELETE Profile

```
DELETE https://manizh.pythonanywhere.com/api/profiles/2/
```

---

### 4️⃣ Projects

**Endpoint**: `/projects/`

#### List Projects

```http
GET https://manizh.pythonanywhere.com/api/projects/
```

#### Create Project (Requires Auth)

```http
POST https://manizh.pythonanywhere.com/api/projects/

Headers:
Authorization: Token user-auth-token-here

Body (JSON):

{
    "title": "Testing api upload project",
    "description": "Flutter app for demonstration.",
    "link": "https://github.com/manishgk9/chatbotgimini",
    "skills": [
        "flutter",
        "bloc",
        "hive",
        "gemini"
    ]
}
```

---

### DELETE Project

```
DELETE https://manizh.pythonanywhere.com/api/projects/2/
```

---

### 5️⃣ Skills

**Endpoint**: `/skills/`

#### List Skills

```http
GET https://manizh.pythonanywhere.com/api/skills/
```

---

### 6️⃣ Work Experience

**Endpoint**: `/work-experience/`

#### List Work Experiences

```http
GET https://manizh.pythonanywhere.com/api/work-experience/
```

#### Create Work Experience

```http
POST https://manizh.pythonanywhere.com/api/work-experience/

Headers:
Authorization: Token user-auth-token-here

Body (JSON):
{
  "company": "Google.com",
  "role": "Backend Developer",
  "start_date": "2023-02-02",
  "end_date": "2024-02-02",
  "description": "Worked on AI Models"
}
```

---

### DELETE Exeperience

```
DELETE https://manizh.pythonanywhere.com/api/work-experience/2/
```

---

## 🔧 Running Locally

```bash
# Clone repo
git clone https://github.com/manishgk9/me_api.git
cd me_api

# Backend setup
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

# Frontend setup (React)
cd frontend
npm install
npm run build
```

---

## 🧪 Test User for API

You can test APIs using the following credentials:

```
username: testuser
password: testuser@123
```

Login first (`/auth/token/`) to get a token, then use it in **Authorization Header**:

```
Authorization: Token <your-token>
```

---

## About the Developer

Hi, I’m **Manish Yadav** – a passionate Full-Stack Developer and Machine Learning enthusiastic and know **Django, React, Flutter,Fastapi and API development**.
I enjoy building scalable applications, crafting APIs, and working on cross-platform solutions.

- 📄 **Resume:** [View Here](https://drive.google.com/file/d/1VUT944U_ZwEAhBiiX6uwYUahOF3JXQbs/view)
- 🔗 **Portfolio:** [https://portfolio](https://manishgk9.github.io/site/)
- 💼 **LinkedIn:** [linkedin.com/in/manishgk9](https://linkedin.com/in/manishgk9)
- 🐙 **GitHub:** [github.com/manishgk9](https://github.com/manishgk9)

---
