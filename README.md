cat > /mnt/user-data/outputs/README.md << 'MDEOF'
# 🎓 Face Recognition Attendance System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![DeepFace](https://img.shields.io/badge/DeepFace-VGG--Face-purple?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-orange?style=for-the-badge&logo=sqlite&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-red?style=for-the-badge)

**An AI-powered automated attendance system using face recognition**
Built with ❤️ by **Gulsum Begam** | MCA 2026

</div>

---

## 📸 Screenshots

### 🏠 Main Dashboard

```
╔══════════════════════════════════════════════════════════════════════╗
║  🎓 Face Recognition Attendance System          25 May 2026 10:30AM ║
╠═══════════════╦══════════════════════════════════════════════════════╣
║   ACTIONS     ║  📷 Camera Feed                                      ║
║               ║ ┌──────────────────────────────────────────────────┐ ║
║ 📷 Register   ║ │                                                  │ ║
║ ✅ Start      ║ │         Camera not active                        │ ║
║ ⏹ Stop       ║ │    Click 'Start Attendance' to begin             │ ║
║               ║ │                                                  │ ║
║   VIEW        ║ └──────────────────────────────────────────────────┘ ║
║ 📅 Today      ║  System ready. Register students first.              ║
║ 📋 All        ╠══════════════════════════════════════════════════════╣
║ 👥 Students   ║  📋 Records                                          ║
║               ║  Name     │ Roll No │  Date      │ Time  │ Status   ║
║   TOOLS       ║  ─────────┼─────────┼────────────┼───────┼────────  ║
║ 💾 Export     ║                                                      ║
║ 🗑 Delete     ║                                                      ║
║               ║                                                      ║
║ ─────────     ║                                                      ║
║ 📊 Stats      ║                                                      ║
║ Students: 0   ║                                                      ║
║ Present: 0    ║                                                      ║
║ Model: ✅     ║                                                      ║
╚═══════════════╩══════════════════════════════════════════════════════╝
```

---

### 👥 Registered Students

```
╔══════════════════════════════════════════════════════════════════════╗
║  🎓 Face Recognition Attendance System          25 May 2026 10:32AM ║
╠═══════════════╦══════════════════════════════════════════════════════╣
║   ACTIONS     ║  📷 Camera Feed                                      ║
║               ║ ┌──────────────────────────────────────────────────┐ ║
║ 📷 Register   ║ │         Camera not active                        │ ║
║ ✅ Start      ║ └──────────────────────────────────────────────────┘ ║
║ ⏹ Stop       ║  ✅ Registered: Guls (101)                           ║
║               ╠══════════════════════════════════════════════════════╣
║   VIEW        ║  📋 Records — Registered Students (2 total)          ║
║ 📅 Today      ║                                                      ║
║ 📋 All        ║  Name     │ Roll No │  Date  │ Time │   Status      ║
║ 👥 Students   ║  ─────────┼─────────┼────────┼──────┼────────────   ║
║               ║  Guls     │   101   │   —    │  —   │ Registered   ║
║   TOOLS       ║  Aksh     │   102   │   —    │  —   │ Registered   ║
║ 💾 Export     ║                                                      ║
║ 🗑 Delete     ║                                                      ║
║               ║                                                      ║
║ ─────────     ║                                                      ║
║ 📊 Stats      ║                                                      ║
║ Students: 2   ║                                                      ║
║ Present: 0    ║                                                      ║
║ Model: ✅     ║                                                      ║
╚═══════════════╩══════════════════════════════════════════════════════╝
```

---

### 📷 Live Attendance Running

```
╔══════════════════════════════════════════════════════════════════════╗
║  🎓 Face Recognition Attendance System          25 May 2026 10:35AM ║
╠═══════════════╦══════════════════════════════════════════════════════╣
║   ACTIONS     ║  📷 Camera Feed                                      ║
║               ║ ┌──────────────────────────────────────────────────┐ ║
║ 📷 Register   ║ │  Present Today: 1  |  ESC = Stop                 │ ║
║ ✅ Start      ║ │                                                   │ ║
║ ⏹ Stop       ║ │         🟣─────────────────┐                      │ ║
║               ║ │         │   😊 FACE BOX   │                      │ ║
║   VIEW        ║ │         │─────────────────┘                      │ ║
║ 📅 Today      ║ │         │      Guls        │                      │ ║
║ 📋 All        ║ └──────────────────────────────────────────────────┘ ║
║ 👥 Students   ║  ✅ Attendance marked: Guls (101)                    ║
║               ╠══════════════════════════════════════════════════════╣
║   TOOLS       ║  📋 Records — Today 25 May 2026                      ║
║ 💾 Export     ║                                                      ║
║ 🗑 Delete     ║  Name  │ Roll No │    Date    │  Time   │  Status   ║
║               ║  ──────┼─────────┼────────────┼─────────┼────────   ║
║ ─────────     ║  Guls  │   101   │ 2026-05-25 │ 10:35:22│ Present  ║
║ 📊 Stats      ║                                                      ║
║ Students: 2   ║                                                      ║
║ Present: 1    ║                                                      ║
║ Model: ✅     ║                                                      ║
╚═══════════════╩══════════════════════════════════════════════════════╝
```

---

### ✅ Attendance Marked — Both Students

```
╔══════════════════════════════════════════════════════════════════════╗
║  🎓 Face Recognition Attendance System          25 May 2026 10:38AM ║
╠═══════════════╦══════════════════════════════════════════════════════╣
║   ACTIONS     ║  📷 Camera Feed (Running)                            ║
║               ║ ┌──────────────────────────────────────────────────┐ ║
║ 📷 Register   ║ │  Present Today: 2  |  ESC = Stop                 │ ║
║ ✅ Start      ║ │                                                   │ ║
║ ⏹ Stop       ║ │    🟣──────┐        🟣──────┐                     │ ║
║               ║ │    │ 😊  │        │ 😊  │                     │ ║
║   VIEW        ║ │    │ Guls│        │ Aksh│                     │ ║
║ 📅 Today      ║ │    └─────┘        └─────┘                     │ ║
║ 📋 All        ║ └──────────────────────────────────────────────────┘ ║
║ 👥 Students   ║  ✅ Attendance marked: Aksh (102)                    ║
║               ╠══════════════════════════════════════════════════════╣
║   TOOLS       ║  📋 Records — Today 25 May 2026 (2 Present)          ║
║ 💾 Export     ║                                                      ║
║ 🗑 Delete     ║  Name  │ Roll No │    Date    │  Time   │  Status   ║
║               ║  ──────┼─────────┼────────────┼─────────┼────────   ║
║ ─────────     ║  Aksh  │   102   │ 2026-05-25 │ 10:38:05│ Present  ║
║ 📊 Stats      ║  Guls  │   101   │ 2026-05-25 │ 10:35:22│ Present  ║
║ Students: 2   ║                                                      ║
║ Present: 2    ║                                                      ║
║ Model: ✅     ║                                                      ║
╚═══════════════╩══════════════════════════════════════════════════════╝
```

---

### 💾 CSV Export Sample

```
Name  | Roll No |    Date    |   Time   | Status
------|---------|------------|----------|--------
Guls  |   101   | 2026-05-25 | 10:35:22 | Present
Aksh  |   102   | 2026-05-25 | 10:38:05 | Present
```

---

## 🎭 Meet The Students

```
        Roll No: 101                    Roll No: 102
       ╭──────────────╮               ╭──────────────╮
       │   \  😊  /   │               │   \  😎  /   │
       │    (Guls)    │               │    (Aksh)    │
       │   /──────\   │               │   /──────\   │
       │  Student 👩  │               │  Student 👦  │
       ╰──────────────╯               ╰──────────────╯
        ✅ Registered                   ✅ Registered
        ✅ Present Today                ✅ Present Today
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 📷 **Face Registration** | Capture student face via webcam |
| 🤖 **AI Recognition** | DeepFace VGG-Face model |
| ✅ **Auto Attendance** | Marks once per day automatically |
| 🗄️ **SQLite Database** | Stores all records permanently |
| 💾 **CSV Export** | Download attendance as spreadsheet |
| 🗑️ **Delete Student** | Remove registered students |
| 📊 **Live Stats** | Real-time present count |
| 🎨 **Dark UI** | Beautiful dark themed Tkinter GUI |

---

## 🛠️ Tech Stack

```
Python 3.11
├── DeepFace      → Face recognition (VGG-Face model)
├── OpenCV        → Webcam & face detection
├── Tkinter       → Desktop GUI
├── SQLite3       → Database
├── Pillow        → Image processing
└── NumPy         → Array operations
```

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/GulsumBegam/face-attendance-system.git
cd face-attendance-system

# 2. Create virtual environment
py -3.11 -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Run

```bash
python face_attendance.py
```

---

## 📖 How To Use

```
Step 1 → Click "Register Student"
         Enter name (e.g. Guls) and Roll No (e.g. 101)
         Look at camera → Press SPACE to capture face

Step 2 → Click "Start Attendance"
         Webcam opens → AI detects & recognizes faces
         Attendance marked automatically ✅

Step 3 → Click "Today's Records" to view attendance

Step 4 → Click "Export to CSV" to download as spreadsheet
```

---

## 📁 Project Structure

```
face-attendance-system/
├── face_attendance.py     ← Main application
├── requirements.txt       ← Dependencies
├── README.md              ← This file
├── attendance.db          ← SQLite database (auto-created)
└── registered_faces/      ← Student face images (auto-created)
    ├── 101.jpg
    └── 102.jpg
```

---

## 👩‍💻 Author

**Gulsum Begam**
MCA Student | Graduating May 2026
The Standard Fireworks Rajaratnam College for Women
Madurai Kamaraj University

[![GitHub](https://img.shields.io/badge/GitHub-GulsumBegam-black?style=flat-square&logo=github)](https://github.com/GulsumBegam)
[![Portfolio](https://img.shields.io/badge/Portfolio-gulsumportfolio.github.io-purple?style=flat-square)](https://gulsumportfolio.github.io)

---

<div align="center">
Made with ❤️ and Python 🐍
</div>
MDEOF
echo "Done!"

#  Face Recognition Attendance System

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
