# 🎓 Face Recognition Attendance System

> An AI-powered smart attendance management system using DeepFace, OpenCV, Tkinter, and SQLite.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![DeepFace](https://img.shields.io/badge/DeepFace-AI-orange?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

---

## ✨ Overview

The **Face Recognition Attendance System** is a real-time AI-based desktop application that automates student attendance using facial recognition technology.

Instead of manual attendance marking, the system:
- detects faces through webcam
- recognizes registered students
- marks attendance automatically
- stores records securely in SQLite database
- exports attendance reports as CSV files

Built with:
- 🧠 DeepFace AI
- 🎥 OpenCV
- 🖥 Tkinter GUI
- 🗄 SQLite3 Database

---

# 🚀 Features

✅ Real-Time Face Recognition  
✅ AI-Powered Student Verification  
✅ Student Registration with Webcam  
✅ Automatic Attendance Marking  
✅ Modern Dark-Themed GUI  
✅ SQLite Database Integration  
✅ CSV Attendance Export  
✅ Duplicate Attendance Prevention  
✅ Student Management System  
✅ Multi-threaded Performance Optimization  

---

# 🛠 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Programming |
| OpenCV | Camera & Face Detection |
| DeepFace | AI Face Recognition |
| Tkinter | Desktop GUI |
| SQLite3 | Local Database |
| Pillow | Image Processing |
| NumPy | Numerical Operations |

---

# 📸 Application Modules

## 👤 Student Registration
- Capture student face through webcam
- Store face image securely
- Register student details in database

## 🎯 Face Recognition
- Detect faces in real time
- Compare with registered students
- Verify identity using DeepFace AI

## 📅 Attendance Management
- Auto-mark attendance
- Prevent duplicate entries
- View daily attendance records

## 📤 Export System
- Export attendance reports to CSV
- Easy sharing and documentation

---

# 🧠 AI Recognition Flow

```text
Webcam Feed
     ↓
Face Detection (OpenCV)
     ↓
Face Verification (DeepFace)
     ↓
Student Match Found
     ↓
Attendance Stored in SQLite
```

---

# 📂 Project Structure

```text
face-attendance-system/
│
├── face_attendance.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── registered_faces/
├── attendance.db
└── exports/
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/GulsumBegam/face-attendance-system.git
```

---

## 2️⃣ Move Into Project Folder

```bash
cd face-attendance-system
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Environment

### Windows
```bash
venv\Scripts\activate
```

### Linux / Mac
```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python face_attendance.py
```

---

# 📋 How To Use

## Register Student
1. Click **Register Student**
2. Enter student details
3. Capture face using webcam
4. Student gets added to database

## Start Attendance
1. Click **Start Attendance**
2. AI recognizes faces automatically
3. Attendance gets marked instantly

## Export Attendance
1. Click **Export CSV**
2. Attendance report saves locally

---

# 🔒 Database Design

## Students Table
| Field | Description |
|---|---|
| id | Primary Key |
| name | Student Name |
| roll_no | Unique Roll Number |
| img_path | Stored Face Image |

## Attendance Table
| Field | Description |
|---|---|
| id | Primary Key |
| roll_no | Student Roll Number |
| name | Student Name |
| date | Attendance Date |
| time | Attendance Time |
| status | Present/Absent |

---

# 🎯 Future Improvements

- 🌐 Web-Based Version
- ☁ Cloud Database Integration
- 📱 Mobile App Support
- 🔔 Email Notifications
- 📊 Analytics Dashboard
- 🧾 PDF Report Export
- 👥 Multi-Face Recognition
- 🔐 User Authentication System

---

# 💡 Key Highlights

- Real-world AI application
- Practical automation system
- Modern UI experience
- Efficient database handling
- Beginner-to-intermediate level AI integration
- Resume-ready full project

---

# 👩‍💻 Author

## Gulsum Begam
Aspiring Full Stack Developer & AI Enthusiast 🌙

- 💻 Passionate about Full Stack Development
- 🤖 Interested in AI-Powered Applications
- 🚀 Building real-world software projects

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the project  
🚀 Share with others  

---


> “Turning ideas into intelligent software.” 🌙
