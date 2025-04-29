Blog API
This is a RESTful API for a blogging platform built with FastAPI. It provides endpoints to manage users and blog posts, with a database backend using SQLAlchemy. The API supports CRUD operations for two main entities: User and Post.
Project Structure

app/: Main application directory
api/: API route definitions
core/: Core configurations (e.g., settings, security)
crud/: CRUD operations for database interactions
db/: Database setup and session management
schemas/: Pydantic models for request/response validation


main.py: Entry point for the FastAPI application
.gitignore: Git ignore file for excluding unnecessary files

Features

Create, read, update, and delete users and blog posts
Database management with SQLAlchemy ORM
Input validation using Pydantic schemas
Modular structure for scalability

Prerequisites

Python 3.8+
MySQL (or another supported database)
pip for installing dependencies

Setup Instructions

Clone the repository:
git clone <repository-url>
cd BlogPro


Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install -r requirements.txt

Note: If requirements.txt is not present, install the core dependencies:
pip install fastapi uvicorn sqlalchemy pymysql pydantic


Set up the database:

Ensure MySQL is running.

Create a database for the project.

Update the database connection string in app/core/config.py (or equivalent file) with your database credentials:
DATABASE_URL = "mysql+pymysql://username:password@localhost:5432/dbname"


Run the application:
python -m app.main

The API will be available at http://127.0.0.1:8080.

Access the API documentation:

Open http://127.0.0.1:8080/docs in your browser to view the interactive Swagger UI.



API Endpoints
Users
Prefix: 'v1/auth/
GET /users/: List all users
POST /users/: Create a new user
GET /users/{id}: Get a user by ID
PUT /users/{id}: Update a user
DELETE /users/{id}: Delete a user

Posts
Prefix: 'v1/post/
GET /posts/: List all posts
POST /posts/: Create a new post
GET /posts/{id}: Get a post by ID
PUT /posts/{id}: Update a post
DELETE /posts/{id}: Delete a post


Contact information: 
- Phone Number: 034871187
- Email: nguyenquangduy12112004@gmail.com
- Facebook: https://www.facebook.com/profile.php?id=100034063569091
