# 🎓 Student Performance Tracker

![License](https://img.shields.io/badge/license-MIT-blue.svg)

A simple and effective web application to track the academic performance of students.

---

## ✨ Features

*   🔐 **Teacher Authentication:** Secure login for teachers.
*   👨‍🎓 **Student Management:** Add, edit, and delete student records.
*   📝 **Grade Management:** Add, edit, and delete grades for each student.
*   📊 **Performance Statistics:** View individual student performance and class-wide statistics.
*   💾 **Data Backup:** Export student data to a text file.

---

## 🛠️ Technologies Used

*   **Backend:** Python, Flask
*   **Database:** PostgreSQL (for production on Render), SQLite (for local development)
*   **ORM:** Flask-SQLAlchemy
*   **Authentication:** Flask-Login
*   **Frontend:** HTML, CSS

---

## 📂 File Structure

```
.
├── .gitignore
├── Procfile
├── README.md
├── app.py
├── requirements.txt
├── static
│   └── css
│       └── style.css
├── templates
│   ├── edit_grade.html
│   ├── edit_student.html
│   ├── index.html
│   ├── login.html
│   ├── stats.html
│   └── student_details.html
└── test_db.py
```

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

*   Python 3.x
*   pip

### Installation

1.  **Clone the repo:**
    ```sh
    git clone https://github.com/naskarmourique/Student-Performance-Tracker.git
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd Student-Performance-Tracker
    ```
3.  **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```
4.  **Activate the virtual environment:**
    *   **Windows:**
        ```sh
        venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```sh
        source venv/bin/activate
        ```
5.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
6.  **Initialize the database and create a default user:**
    ```sh
    flask init-db
    flask create-user
    ```

---

## 💻 Usage

### 1. Logging In

The application requires teachers to log in to access the student data.

*   **Username:** Mourique
*   **Password:** izya

### 2. Home Page

After logging in, you will be redirected to the home page, which displays a list of all the students.

### 3. Adding a Student

To add a new student:
1.  On the home page, you will find a form to add a new student.
2.  Enter the student's name and roll number.
3.  Click the "Add Student" button.

### 4. Viewing Student Details and Performance

To view a student's details and performance:
1.  On the home page, click on the student's name.
2.  This will take you to the student's details page, where you can see their grades for each subject and their average score.

### 5. Adding Grades

To add a grade for a student:
1.  Go to the student's details page.
2.  You will find a form to add a new grade.
3.  Enter the subject and the marks obtained.
4.  Click the "Add Grade" button.

### 6. Editing and Deleting Students and Grades

You can edit or delete students and grades from their respective pages.
*   To edit a student's details, click the "Edit" button on the home page next to the student's name.
*   To delete a student, click the "Delete" button on the home page next to the student's name.
*   To edit or delete a grade, go to the student's details page and you will find options to edit or delete each grade.

### 7. Viewing Subject Statistics

To view statistics for a specific subject:
1.  Click on the "Stats" link in the navigation bar.
2.  Enter the subject name and click "Get Stats".
3.  This will show you the class average and the topper for that subject.

### 8. Backing Up Data

To back up all student data:
1.  Click on the "Backup" link in the navigation bar.
2.  This will download a text file containing all the student data.

---

## 🌐 Deployment

This application is deployed on Render and is live at:
[https://student-performance-tracker-s6wf.onrender.com](https://student-performance-tracker-s6wf.onrender.com)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.