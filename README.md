# U-Notes-app
U Notes is a simple note-taking web application built using FastAPI, MongoDB, Jinja2, HTML, CSS, and Bootstrap. It allows users to create, store, and view notes, with an option to mark important notes for easy identification.
# 📝 U Notes – Notes Management App

U Notes is a simple note-taking web application built using **FastAPI, MongoDB, Jinja2, HTML, CSS, and Bootstrap**. It allows users to create, store, and view notes, with an option to mark important notes.

## 🚀 Features

- Add notes with a title and description
- Store notes in MongoDB
- Mark notes as important
- Display notes dynamically using Jinja2 templates
- Responsive user interface using Bootstrap and custom CSS

## 🛠️ Tech Stack

- **Backend:** Python, FastAPI
- **Database:** MongoDB
- **Frontend:** HTML, CSS, Bootstrap
- **Templating Engine:** Jinja2
- **Data Validation:** Pydantic

## 📂 Project Structure

```text
fastApi/
├── main.py
├── config/
│   └── dib.py
├── models/
│   └── note.py
├── routes/
│   └── note.py
├── schema/
│   └── note.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
└── README.md
```
<p align="center">
  <img src="Screenshot 2026-10-08 161738.png" alt="U Notes Home Page" width="700">
</p>

<p align="center">
  <img src="Screenshot 2026-10-08 161758.png" alt="U Notes Home Page" width="700">
</p>

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <https://github.com/danishnehru/U-Notes-app.git>
cd fastApi
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn pymongo jinja2 python-multipart
```

### 4. Start MongoDB

Make sure MongoDB is running locally at:

```text
mongodb://localhost:27017/
```

The application uses the `mydatabase` database and the `notes` collection.

### 5. Run the application

```bash
uvicorn main:app --reload
```

Open your browser and visit:

**http://127.0.0.1:8000**



## 👨‍💻 Author

Built as a hands-on project to strengthen my understanding of **FastAPI and backend development**.

---

⭐ If you find this project useful, consider giving the repository a star!
