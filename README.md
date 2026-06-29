# 📄 CVGen – Django Resume Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?logo=django)
![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3)
![License](https://img.shields.io/badge/License-MIT-yellow)

A web-based **Resume/CV Generator** built with **Django** that enables users to create professional, ATS-friendly resumes through a simple interface. The application collects user information and generates a clean, structured CV ready for job applications.

---

## 🚀 Features

* 📝 Create professional resumes through an intuitive form
* 📄 Generate clean and ATS-friendly CVs
* 🎯 User-friendly interface
* ⚡ Built using Django's MTV architecture
* 🔒 Secure form handling
* 📱 Responsive design
* ✨ Easy to customize and extend

---

## 🛠 Tech Stack

| Technology | Purpose                  |
| ---------- | ------------------------ |
| Python     | Backend                  |
| Django     | Web Framework            |
| HTML5      | Frontend                 |
| CSS3       | Styling                  |
| SQLite     | Default Database         |
| JavaScript | Client-side Interactions |

---

## 📂 Project Structure

```text
cv-genrator/
│
├── mysite/
│   ├── manage.py
│   ├── myapp/
│   │   ├── migrations/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── tests.py
│   │   └── __init__.py
│   │
│   └── mysite/
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       ├── wsgi.py
│       └── __init__.py
│
├── .gitignore
└── README.md
```

---

## ⚙️ Getting Started

### Clone the Repository

```bash
git clone https://github.com/harshselokar26/cv-genrator.git
```

### Navigate to the Project

```bash
cd cv-genrator
```

### Create a Virtual Environment

```bash
python -m venv env
```

### Activate the Virtual Environment

**Windows (PowerShell)**

```powershell
.\env\Scripts\Activate.ps1
```

**Windows (Command Prompt)**

```cmd
env\Scripts\activate.bat
```

**Linux/macOS**

```bash
source env/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Database Migrations

```bash
cd mysite

python manage.py migrate
```

### Start the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Add screenshots of your application here.

```
screenshots/
├── home.png
├── form.png
├── preview.png
└── generated_cv.png
```

---

## 🎯 Future Enhancements

* Multiple resume templates
* PDF download support
* User authentication
* Resume preview before download
* AI-powered resume suggestions
* Resume scoring
* Dark mode
* Cloud storage integration

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Harsh Selokar**

* GitHub: https://github.com/harshselokar26

---

## ⭐ Support

If you found this project helpful, consider giving it a **Star ⭐** on GitHub.

It helps others discover the project and motivates further development.

---
