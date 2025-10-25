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

To run the application locally, use the following command:

```sh
flask run
```

Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## 🌐 Deployment

This application is deployed on Render and is live at:
[https://student-performance-tracker-s6wf.onrender.com](https://student-performance-tracker-s6wf.onrender.com)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
