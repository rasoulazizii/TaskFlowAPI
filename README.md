TaskFlow API 📝

TaskFlow is a RESTful API for a task management system built with Django and Django REST Framework. This project was developed as a portfolio piece to demonstrate proficiency in building robust backend services and to specifically learn and implement asynchronous background tasks using Celery and Redis.

The core feature of this API is its ability to automatically send reminder emails to users about tasks that are approaching their due dates, without blocking the main application thread.

✨ Key Features

User Authentication: Secure user registration and login using JSON Web Tokens (JWT).

Protected Routes: Endpoints for viewing and updating user profiles are accessible only to authenticated users.

Complete Task Management: Full CRUD (Create, Read, Update, Delete) functionality for tasks.

Ownership & Permissions: Users can only view and manage their own tasks.

🚀 Asynchronous Reminders: A daily scheduled job, powered by Celery Beat, checks for tasks due within the next 24 hours.

Background Email Delivery: Reminder emails are sent asynchronously by Celery Workers, ensuring the API remains fast and responsive.

🛠️ Tech Stack

Component	Technology
Backend	Django, Django REST Framework
Database	SQLite3 (for development)
Asynchronous Tasks	Celery
Message Broker	Redis
Authentication	djangorestframework-simplejwt

🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

Prerequisites

Python 3.8+

pip package manager

An active Redis server instance.

Installation & Setup

Clone the repository:

git clone https://github.com/your-username/taskflow-api.git
cd taskflow-api

Create and activate a virtual environment:

Create the virtual environment

python -m venv venv

Activate on Windows

.\venv\Scripts\activate

Activate on macOS/Linux

source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt
(Note: You may need to create the requirements.txt file first using pip freeze > requirements.txt)

Apply the database migrations:

python manage.py migrate

Run the application (Requires 4 separate terminals):

Terminal 1: Run the Redis Server
If not already running, start your Redis instance.

redis-server

Terminal 2: Run the Celery Worker
This worker listens for tasks from the Redis queue and executes them.

celery -A config worker -l info

Terminal 3: Run the Celery Beat Scheduler
This service schedules the periodic tasks (like our daily check).

celery -A config beat -l info

Terminal 4: Run the Django Development Server
This serves the API.

python manage.py runserver

The API will be available at http://127.0.0.1:8000.

📚 API Endpoints

To access protected endpoints, include the JWT access token in the Authorization header as follows: Authorization: Bearer <your_access_token>.

Authentication / Users
Method	Endpoint	Description	Access
POST	/api/accounts/register/	Registers a new user.	Public.
POST	/api/accounts/token/	Authenticates a user and returns access and refresh tokens.	Public.
GET, PUT	/api/accounts/me/	Retrieves or updates the profile of the currently authenticated user.	Authenticated.

Request Body for POST /api/accounts/register/:

{
"username": "newuser",
"email": "user@example.com",
"password": "your_strong_password",
"password2": "your_strong_password"
}

Request Body for POST /api/accounts/token/:

{
"username": "newuser",
"password": "your_strong_password"
}

Tasks
Method	Endpoint	Description	Access
GET	/api/tasks/	Returns a list of all tasks belonging to the authenticated user.	Authenticated.
POST	/api/tasks/	Creates a new task for the authenticated user.	Authenticated.
GET, PUT, PATCH, DELETE	/api/tasks/{id}/	Retrieve, fully update, partially update, or delete a specific task by its ID.	Authenticated (user must be the owner of the task).

Request Body for POST /api/tasks/:

{
"title": "My first important task",
"description": "Some details about what needs to be done.",
"due_date": "2025-11-09T10:00:00Z",
"status": "TODO"
}