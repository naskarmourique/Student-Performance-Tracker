# Student Performance Tracker

A web-based application built with Flask to help teachers track and manage student performance.

## Features

*   **Teacher Authentication:** Secure login system for teachers.
*   **Student Management:** Add, edit, and delete student records.
*   **Grade Management:** Record, update, and delete grades for various subjects.
*   **Detailed Student View:** See a comprehensive overview of each student's grades and average performance.
*   **Subject Statistics:** Analyze subject-wise performance, including identifying the topper and class average.
*   **Data Backup:** Export all student data and grades to a text file.

## Technologies Used

*   **Backend:** Flask, Flask-SQLAlchemy, Flask-Login
*   **Database:** PostgreSQL (with a fallback to SQLite)
*   **Frontend:** HTML, CSS, JavaScript
*   **Deployment:** Gunicorn

## Getting Started

### Prerequisites

*   Python 3
*   pip

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd student_performance_tracker
    ```
3.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Set up the environment variables:**
    Create a `.env` file and add the following:
    ```
    DATABASE_URL=<your-database-url>
    SECRET_KEY=<your-secret-key>
    DEFAULT_TEACHER_USERNAME=Mourique
    DEFAULT_TEACHER_PASSWORD=izya
    ```
6.  **Initialize the database:**
    ```bash
    flask init-db
    ```
7.  **Create a default user:**
    ```bash
    flask create-user
    ```
8.  **Run the application:**
    ```bash
    python app.py
    ```

The application will be available at `http://127.0.0.1:5000`.

### Default Login

*   **Username:** Mourique
*   **Password:** izya
