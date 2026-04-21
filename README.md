 User Login Authentication
 Developer Dashboard
 Project Management
 Task Assignment
 Task Status Update (Pending / In Progress / Completed)
 View All Database Tasks
 Stylish UI (Login + Dashboard)
 Technologies Used
Python
Django
HTML
CSS
SQLite (Default Database)
Project Structure
project/
│
├── hello/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   ├── urls.py
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│
├── static/
│   └── (CSS / Images)
│
├── manage.py
⚙️ Installation
# Clone the repository
git clone https://github.com/your-username/your-repo-name.git

# Go to project folder
cd your-repo-name

# Create virtual environment
python -m venv env

# Activate environment
env\Scripts\activate   # Windows

# Install dependencies
pip install django

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (Admin)
python manage.py createsuperuser

# Run server
python manage.py runserver
🔑 Login Details
👑 Admin
Access: /admin/
Can create:
Developers
Projects
Tasks
👨‍💻 Developer
Login via homepage
Can:
View assigned tasks
Update task status
