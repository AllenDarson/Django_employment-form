Employee Management System — Django Web Application
This is a simple yet functional Employee Management System built using Django and Bootstrap 5. The application allows users to add, update, view, search, and delete employee records in a structured and user-friendly interface.

✅ Features
🔐 Add new employee details

🔎 Search employee by name

📋 View all employee records in a table

✏️ Edit employee information

❌ Delete employee with confirmation prompt

🎨 Clean Bootstrap-based UI

🔄 Form validation and redirection

🛠️ Tech Stack
Backend: Django (Python)

Frontend: HTML, CSS, Bootstrap 5 ,Javascript

Database: SQLite (default Django DB)

📂 Project Structure
templates/ – HTML templates (form.html, show_data.html, updateform.html, delete_data.html)

models.py – Employee model with fields like name, DOB, contact, department, etc.

views.py – Contains all views for handling data and rendering templates

urls.py – URL patterns for navigation

static/ – Bootstrap via CDN (no local CSS/JS dependencies)

🧑‍💻 How to Run
Clone the repository

git clone https://github.com/your-username/employee-management-django.git
cd employee-management-django
Set up virtual environment (optional but recommended)


python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
Install Django

pip install django
Run the server

python manage.py runserver
Visit http://127.0.0.1:8000/form to start using the app.
