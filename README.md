# 🎓 Face Recognition Attendance System

A desktop attendance management application that uses real-time face recognition to mark student attendance automatically. Built with **Python, OpenCV, DeepFace, and Tkinter**, with attendance records stored in **SQLite** and exportable to **CSV**.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?logo=opencv&logoColor=white)
![DeepFace](https://img.shields.io/badge/DeepFace-AI%20Powered-orange)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-yellowgreen)
![SQLite](https://img.shields.io/badge/Database-SQLite-07405E?logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📸 Demo

![App Demo](./demo.gif)

---

## ✨ Features

- 🧑‍🎓 **Register Students** — Add new students with name, roll number, and a captured face photo
- 🎥 **Live Camera Feed** — Real-time face detection and recognition via webcam
- ✅ **Automatic Attendance Marking** — Detects and recognizes faces, marks attendance instantly
- 📅 **Today's Records** — View a quick summary of who's present today
- 📊 **All Attendance** — Browse the complete attendance history
- 👥 **All Students** — View the full list of registered students
- 📤 **Export to CSV** — One-click export of attendance data for reporting
- 🗑️ **Delete Student** — Remove a student and their records with confirmation
- 🧹 **Clear Today's Marks** — Reset today's attendance with a safety confirmation
- 📈 **Live Stats Panel** — Shows total students and number present today

---

## 🖥️ Application Walkthrough

### 🏠 Home Screen
The main dashboard showing the camera feed, action buttons, and live attendance records.

![Home Screen](./01_home.png)

### ➕ Registering a New Student

**Step 1 — Enter Name**

![Register Name](./02_register_name.png)

**Step 2 — Enter Roll Number / ID**

![Register Roll No](./03_register_roll.png)

**Step 3 — Capture Instructions**

![Capture Instructions](./04_capture_prompt.png)

**Step 4 — Face Capture**

The system detects the face in real time and captures it for recognition training.

![Face Capture](./05_face_capture.png)

### 🎯 Live Face Recognition & Attendance Marking

Once attendance starts, the system recognizes registered faces and marks them present automatically.

![Live Recognition](./06_recognition.png)

### 📅 Today's Records

![Today's Records](./07_today_records.png)

### 📊 All Attendance History

![All Attendance](./08_all_attendance.png)

### 👥 All Registered Students

![All Students](./09_all_students.png)

### 📤 Export to CSV

Attendance data can be exported to a CSV file with a single click.

![Export to CSV](./10_export_csv.png)

### 🗑️ Delete Student

**Step 1 — Enter Roll Number**

![Delete Student](./11_delete_student.png)

**Step 2 — Confirm Deletion**

![Confirm Delete](./12_delete_confirm.png)

### 🧹 Clear Today's Attendance

![Clear Today](./13_clear_today.png)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **OpenCV (cv2)** | Camera access, face detection, image processing |
| **DeepFace** | Deep learning-based face recognition |
| **TensorFlow / Keras (tf-keras)** | Backend for DeepFace models |
| **Tkinter** | GUI framework |
| **Pillow (PIL)** | Image handling for the GUI |
| **SQLite3** | Local database for students & attendance |
| **NumPy** | Numerical operations on image arrays |
| **CSV** | Attendance export |

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/face-recognition-attendance-system.git
   cd face-recognition-attendance-system
   ```

2. **Install the required dependencies**
   ```bash
   pip install opencv-python pillow numpy deepface tensorflow tf-keras
   ```

3. **Run the application**
   ```bash
   python face_attendance.py
   ```

---

## 🚀 Usage

1. Click **Register Student** to add a new student — enter their name, roll number, and capture their face.
2. Click **Start Attendance** to activate the camera and begin recognizing faces in real time.
3. Recognized students are automatically marked **Present** for the day.
4. Use **Today's Records**, **All Attendance**, or **All Students** to view data.
5. Click **Export to CSV** to save attendance records for the day.
6. Use **Delete Student** or **Clear Today Marks** for management/admin tasks.

---

## 📁 Project Structure

```
face-recognition-attendance-system/
├── face_attendance.py        # Main application file
├── attendance.db              # SQLite database (auto-created)
├── student_images/            # Captured face images
├── attendance_YYYY-MM-DD.csv  # Exported attendance reports
└── README.md
```

---

## 👩‍💻 Author

**Gulsum Begam A**

⭐ If you found this project useful, consider giving it a star!
