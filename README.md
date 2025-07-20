
# EdTech Assignment Tracker – Django Project

## Prepared by: Ankit

## Setup Instructions

1. **Clone the project**
   - Extract this zip file to your desired directory

2. **Setup Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install django djangorestframework djangorestframework-simplejwt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

6. **Access the APIs & Frontend**
   - Open `http://127.0.0.1:8000/` in your browser
   - API endpoints are accessible via Postman or frontend

7. **JWT Authentication**
   - Obtain token using `/api/login/` and use it in Authorization Header as `Bearer <token>`

## Project Includes
- ✅ Django with JWT Authentication
- ✅ APIs for Signup/Login, Assignment Creation, Submission
- ✅ Simple HTML Frontend Pages
- ✅ System Design Document (Word file)

---

_This project is for the Pannini Education Ventures Internship Submission._
