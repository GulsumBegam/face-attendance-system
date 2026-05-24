"""
╔══════════════════════════════════════════════════════════════╗
║       Face Recognition Attendance System                     ║
║       Author  : Gulsum Begam  |  Full Stack Developer        ║
║       Tools   : DeepFace, OpenCV, Tkinter, SQLite3, CSV      ║
╚══════════════════════════════════════════════════════════════╝

INSTALL (one command only!):
    pip install deepface opencv-python pillow numpy tf-keras

HOW TO USE:
    1. Run → python face_attendance.py
    2. Register Student → enter name & roll no → capture face
    3. Start Attendance → webcam auto-recognizes & marks attendance
    4. View Attendance / Export CSV anytime
"""

import cv2
import os
import csv
import sqlite3
import threading
import shutil
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime, date
from PIL import Image, ImageTk
import numpy as np

# DeepFace import (lazy so UI loads fast)
deepface_ready = False
DeepFace = None

def load_deepface():
    global DeepFace, deepface_ready
    try:
        from deepface import DeepFace as DF
        DeepFace = DF
        deepface_ready = True
    except Exception as e:
        deepface_ready = False


# ─── PATHS ─────────────────────────────────────────────────────────────────────

DB_FILE   = "attendance.db"
FACES_DIR = "registered_faces"
os.makedirs(FACES_DIR, exist_ok=True)


# ─── DATABASE ──────────────────────────────────────────────────────────────────

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            name     TEXT NOT NULL,
            roll_no  TEXT UNIQUE NOT NULL,
            img_path TEXT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS attendance (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            roll_no    TEXT,
            name       TEXT,
            date       TEXT,
            time       TEXT,
            status     TEXT DEFAULT 'Present'
        )
    """)
    conn.commit()
    conn.close()


def db_add_student(name, roll_no, img_path):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try:
        c.execute(
            "INSERT INTO students (name, roll_no, img_path) VALUES (?, ?, ?)",
            (name, roll_no, img_path)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def db_mark_attendance(roll_no, name):
    """Mark once per day."""
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    today = date.today().strftime("%Y-%m-%d")
    c.execute("SELECT id FROM attendance WHERE roll_no=? AND date=?", (roll_no, today))
    if c.fetchone() is None:
        now = datetime.now().strftime("%H:%M:%S")
        c.execute(
            "INSERT INTO attendance (roll_no, name, date, time) VALUES (?, ?, ?, ?)",
            (roll_no, name, today, now)
        )
        conn.commit()
        conn.close()
        return True
    conn.close()
    return False


def db_get_attendance(filter_date=None):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    if filter_date:
        c.execute(
            "SELECT name, roll_no, date, time, status FROM attendance WHERE date=? ORDER BY time DESC",
            (filter_date,)
        )
    else:
        c.execute(
            "SELECT name, roll_no, date, time, status FROM attendance ORDER BY date DESC, time DESC"
        )
    rows = c.fetchall()
    conn.close()
    return rows


def db_get_students():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT name, roll_no, img_path FROM students")
    rows = c.fetchall()
    conn.close()
    return rows


def db_delete_student(roll_no):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT img_path FROM students WHERE roll_no=?", (roll_no,))
    row = c.fetchone()
    if row and row[0] and os.path.exists(row[0]):
        os.remove(row[0])
    c.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    conn.close()


# ─── DEEPFACE RECOGNITION ──────────────────────────────────────────────────────

def recognize_face(frame_bgr):
    """
    Compare frame against registered_faces folder.
    Returns (name, roll_no) or (None, None).
    """
    if not deepface_ready or DeepFace is None:
        return None, None

    students = db_get_students()
    if not students:
        return None, None

    tmp_path = "temp_frame.jpg"
    cv2.imwrite(tmp_path, frame_bgr)

    best_name    = None
    best_roll    = None
    best_dist    = 999

    for name, roll_no, img_path in students:
        if not img_path or not os.path.exists(img_path):
            continue
        try:
            result = DeepFace.verify(
                img1_path = tmp_path,
                img2_path = img_path,
                model_name = "VGG-Face",
                enforce_detection = False,
                silent = True,
            )
            dist = result.get("distance", 999)
            verified = result.get("verified", False)
            if verified and dist < best_dist:
                best_dist = dist
                best_name = name
                best_roll = roll_no
        except Exception:
            continue

    if os.path.exists(tmp_path):
        os.remove(tmp_path)

    return best_name, best_roll


# ─── MAIN APP ──────────────────────────────────────────────────────────────────

class AttendanceApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition Attendance System — Gulsum Begam")
        self.root.geometry("1020x700")
        self.root.configure(bg="#0f0f1a")
        self.root.resizable(True, True)

        self.is_capturing  = False
        self.cap           = None
        self.marked_today  = set()
        self.cam_photo     = None

        init_db()
        self._setup_styles()
        self._build_ui()
        self._update_clock()
        self._update_stats()

        # Load DeepFace in background so UI doesn't freeze
        self._set_status("⏳ Loading AI model in background…", "#facc15")
        threading.Thread(target=self._init_deepface, daemon=True).start()

    # ── DEEPFACE INIT ─────────────────────────────────────────────────────────

    def _init_deepface(self):
        load_deepface()
        if deepface_ready:
            self.root.after(0, self._set_status,
                "✅ AI model ready! You can register students and start attendance.", "#4ade80")
        else:
            self.root.after(0, self._set_status,
                "❌ DeepFace failed to load. Run: pip install deepface tf-keras", "#f87171")

    # ── STYLES ────────────────────────────────────────────────────────────────

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
            background="#1a1a2e", foreground="white",
            fieldbackground="#1a1a2e", rowheight=28,
            font=("Segoe UI", 10)
        )
        style.configure("Treeview.Heading",
            background="#2d1b69", foreground="white",
            font=("Segoe UI", 10, "bold"), relief="flat"
        )
        style.map("Treeview", background=[("selected", "#7c3aed")])
        style.configure("TScrollbar", background="#1a1a2e", troughcolor="#0f0f1a")

    # ── UI ────────────────────────────────────────────────────────────────────

    def _build_ui(self):
        # Header
        hdr = tk.Frame(self.root, bg="#1a0533", height=72)
        hdr.pack(fill="x")
        hdr.pack_propagate(False)

        tk.Label(hdr,
            text="🎓  Face Recognition Attendance System",
            font=("Segoe UI", 17, "bold"), bg="#1a0533", fg="white"
        ).pack(side="left", padx=20, pady=16)

        self.clock_lbl = tk.Label(hdr, text="",
            font=("Segoe UI", 11), bg="#1a0533", fg="#a78bfa")
        self.clock_lbl.pack(side="right", padx=20)

        # Body
        body = tk.Frame(self.root, bg="#0f0f1a")
        body.pack(fill="both", expand=True, padx=14, pady=10)

        sidebar = tk.Frame(body, bg="#0f0f1a", width=215)
        sidebar.pack(side="left", fill="y", padx=(0, 12))
        sidebar.pack_propagate(False)

        content = tk.Frame(body, bg="#0f0f1a")
        content.pack(side="left", fill="both", expand=True)

        self._build_sidebar(sidebar)
        self._build_content(content)

    # ── SIDEBAR ───────────────────────────────────────────────────────────────

    def _mk_btn(self, parent, text, cmd, bg="#7c3aed", fg="white"):
        b = tk.Button(parent, text=text, command=cmd,
            bg=bg, fg=fg, font=("Segoe UI", 9, "bold"),
            relief="flat", cursor="hand2", pady=9, padx=4,
            activebackground="#6d28d9", activeforeground="white"
        )
        b.pack(fill="x", pady=3)
        hover_bg = "#6d28d9" if bg == "#7c3aed" else bg
        b.bind("<Enter>", lambda e, h=hover_bg: b.config(bg=h))
        b.bind("<Leave>", lambda e: b.config(bg=bg))
        return b

    def _build_sidebar(self, p):
        tk.Label(p, text="ACTIONS",
            font=("Segoe UI", 8, "bold"), bg="#0f0f1a", fg="#6b7280"
        ).pack(anchor="w", pady=(0, 5))

        self._mk_btn(p, "📷  Register Student",  self.register_student)
        self._mk_btn(p, "✅  Start Attendance",   self.start_attendance)
        self._mk_btn(p, "⏹  Stop Camera",        self.stop_camera, "#dc2626")

        tk.Label(p, text="VIEW",
            font=("Segoe UI", 8, "bold"), bg="#0f0f1a", fg="#6b7280"
        ).pack(anchor="w", pady=(12, 5))

        self._mk_btn(p, "📅  Today's Records",   self.show_today,      "#0369a1")
        self._mk_btn(p, "📋  All Attendance",     self.show_attendance, "#0369a1")
        self._mk_btn(p, "👥  All Students",       self.show_students,   "#0369a1")

        tk.Label(p, text="TOOLS",
            font=("Segoe UI", 8, "bold"), bg="#0f0f1a", fg="#6b7280"
        ).pack(anchor="w", pady=(12, 5))

        self._mk_btn(p, "💾  Export to CSV",      self.export_csv,      "#059669")
        self._mk_btn(p, "🗑  Delete Student",     self.delete_student,  "#b45309")
        self._mk_btn(p, "🔄  Clear Today Marks",  self.clear_today,     "#6b7280")

        # Stats box
        sf = tk.LabelFrame(p, text=" 📊 Stats ",
            bg="#1a1a2e", fg="#a78bfa",
            font=("Segoe UI", 9, "bold"), labelanchor="n"
        )
        sf.pack(fill="x", pady=(16, 0))

        self.lbl_students = tk.Label(sf, text="Students : 0",
            bg="#1a1a2e", fg="white", font=("Segoe UI", 10), anchor="w")
        self.lbl_students.pack(fill="x", padx=10, pady=3)

        self.lbl_present = tk.Label(sf, text="Present Today : 0",
            bg="#1a1a2e", fg="#4ade80", font=("Segoe UI", 10), anchor="w")
        self.lbl_present.pack(fill="x", padx=10, pady=3)

        self.lbl_model = tk.Label(sf, text="Model : Loading…",
            bg="#1a1a2e", fg="#facc15", font=("Segoe UI", 9), anchor="w")
        self.lbl_model.pack(fill="x", padx=10, pady=(0, 6))

    # ── CONTENT ───────────────────────────────────────────────────────────────

    def _build_content(self, p):
        # Camera frame
        cam_lf = tk.LabelFrame(p, text=" 📷 Camera Feed ",
            bg="#1a1a2e", fg="#a78bfa",
            font=("Segoe UI", 9, "bold"), labelanchor="n"
        )
        cam_lf.pack(fill="x", pady=(0, 8))

        self.cam_lbl = tk.Label(cam_lf,
            text="Camera not active\nClick 'Start Attendance' to begin",
            bg="#111827", fg="#4b5563",
            font=("Segoe UI", 12), height=10
        )
        self.cam_lbl.pack(fill="x", padx=6, pady=6)

        # Status bar
        self.status_var = tk.StringVar(value="Ready.")
        tk.Label(p, textvariable=self.status_var,
            bg="#0f0f1a", fg="#a78bfa",
            font=("Segoe UI", 9), anchor="w"
        ).pack(fill="x", pady=(0, 6))

        # Table
        tbl_lf = tk.LabelFrame(p, text=" 📋 Records ",
            bg="#1a1a2e", fg="#a78bfa",
            font=("Segoe UI", 9, "bold"), labelanchor="n"
        )
        tbl_lf.pack(fill="both", expand=True)

        cols   = ("Name", "Roll No", "Date", "Time", "Status")
        widths = [170, 110, 110, 100, 90]

        self.tree = ttk.Treeview(tbl_lf, columns=cols, show="headings", height=9)
        for col, w in zip(cols, widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="center")

        self.tree.tag_configure("present", foreground="#4ade80")
        self.tree.tag_configure("student", foreground="#93c5fd")

        vsb = ttk.Scrollbar(tbl_lf, orient="vertical",   command=self.tree.yview)
        hsb = ttk.Scrollbar(tbl_lf, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side="right",  fill="y")
        hsb.pack(side="bottom", fill="x")
        self.tree.pack(fill="both", expand=True, padx=4, pady=4)

    # ── CLOCK ─────────────────────────────────────────────────────────────────

    def _update_clock(self):
        now = datetime.now().strftime("%d %b %Y   %H:%M:%S")
        self.clock_lbl.config(text=now)
        self.root.after(1000, self._update_clock)

    # ── STATUS & STATS ────────────────────────────────────────────────────────

    def _set_status(self, msg, color="#a78bfa"):
        self.status_var.set(msg)
        # find status label widget and update color
        for widget in self.root.winfo_children():
            pass  # colour updated via direct call below
        # update model label too
        if deepface_ready:
            self.lbl_model.config(text="Model : VGG-Face ✅", fg="#4ade80")
        else:
            self.lbl_model.config(text="Model : Loading…", fg="#facc15")

    def _update_stats(self):
        students = db_get_students()
        today    = db_get_attendance(date.today().strftime("%Y-%m-%d"))
        self.lbl_students.config(text=f"Students : {len(students)}")
        self.lbl_present.config(text=f"Present Today : {len(today)}")

    # ── REGISTER STUDENT ──────────────────────────────────────────────────────

    def register_student(self):
        name = simpledialog.askstring("Register Student",
            "Enter student full name:", parent=self.root)
        if not name or not name.strip():
            return
        name = name.strip().title()

        roll = simpledialog.askstring("Register Student",
            "Enter Roll Number / ID:", parent=self.root)
        if not roll or not roll.strip():
            return
        roll = roll.strip().upper()

        # Check duplicate
        existing = [s[1] for s in db_get_students()]
        if roll in existing:
            messagebox.showerror("Duplicate",
                f"Roll No '{roll}' is already registered!", parent=self.root)
            return

        messagebox.showinfo("Capture Face",
            f"Registering: {name}\n\n"
            "• Look straight at the camera\n"
            "• Make sure your face is well lit\n"
            "• Press SPACE to capture\n"
            "• Press ESC to cancel",
            parent=self.root
        )
        self._capture_and_register(name, roll)

    def _capture_and_register(self, name, roll):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "Cannot open camera!", parent=self.root)
            return

        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        captured = False

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))

            display = frame.copy()
            for (x, y, w, h) in faces:
                cv2.rectangle(display, (x, y), (x+w, y+h), (109, 40, 217), 2)
                cv2.putText(display, "Face Detected", (x, y-8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (109, 40, 217), 2)

            cv2.putText(display,
                f"Registering: {name} | SPACE=Capture  ESC=Cancel",
                (10, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.58, (255, 255, 255), 2)

            cv2.imshow("Register Face — Press SPACE to capture", display)
            key = cv2.waitKey(1) & 0xFF

            if key == 32:  # SPACE
                if len(faces) == 0:
                    messagebox.showwarning("No Face",
                        "No face detected! Please try again.", parent=self.root)
                    continue

                img_path = os.path.join(FACES_DIR, f"{roll}.jpg")
                cv2.imwrite(img_path, frame)

                ok = db_add_student(name, roll, img_path)
                if ok:
                    captured = True
                else:
                    os.remove(img_path)
                    messagebox.showerror("Error",
                        f"Roll No '{roll}' already exists!", parent=self.root)
                break

            elif key == 27:  # ESC
                break

        cap.release()
        cv2.destroyAllWindows()

        if captured:
            self._update_stats()
            self._set_status(f"✅ Registered: {name} ({roll})", "#4ade80")
            messagebox.showinfo("Success",
                f"✅ Student '{name}' registered successfully!\n"
                f"Roll No: {roll}",
                parent=self.root
            )
            self.show_students()

    # ── START ATTENDANCE ──────────────────────────────────────────────────────

    def start_attendance(self):
        if not deepface_ready:
            messagebox.showwarning("Not Ready",
                "AI model is still loading. Please wait a moment.",
                parent=self.root)
            return

        students = db_get_students()
        if not students:
            messagebox.showwarning("No Students",
                "No students registered yet!\nPlease register students first.",
                parent=self.root)
            return

        if self.is_capturing:
            self._set_status("⚠️ Camera is already running!", "#facc15")
            return

        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            messagebox.showerror("Error", "Cannot open camera!", parent=self.root)
            return

        self.is_capturing = True
        self.marked_today = set()
        self._set_status("📷 Attendance camera running — looking for faces…", "#facc15")

        threading.Thread(target=self._attendance_loop, daemon=True).start()

    def _attendance_loop(self):
        face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
        )

        frame_count    = 0
        recognize_every = 15   # run DeepFace every N frames (performance)
        last_name      = None
        last_roll      = None
        last_color     = (100, 100, 100)

        while self.is_capturing:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 5, minSize=(80, 80))

            frame_count += 1

            # Run recognition every N frames
            if frame_count % recognize_every == 0 and len(faces) > 0:
                name, roll = recognize_face(frame)
                if name and roll:
                    last_name  = name
                    last_roll  = roll
                    last_color = (40, 167, 109)   # green
                    if roll not in self.marked_today:
                        marked = db_mark_attendance(roll, name)
                        if marked:
                            self.marked_today.add(roll)
                            self.root.after(0, self._on_marked, name, roll)
                else:
                    last_name  = "Unknown"
                    last_roll  = None
                    last_color = (220, 38, 38)    # red

            # Draw boxes
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), last_color, 2)
                label = last_name if last_name else "Detecting…"
                cv2.rectangle(frame, (x, y+h), (x+w, y+h+28), last_color, cv2.FILLED)
                cv2.putText(frame, label, (x+5, y+h+20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

            # Overlay info
            today_count = len(self.marked_today)
            cv2.putText(frame,
                f"Present Today: {today_count}  |  ESC = Stop",
                (10, 28), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (167, 139, 250), 2)

            # Show in Tkinter
            rgb   = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img   = Image.fromarray(rgb).resize((760, 260), Image.LANCZOS)
            photo = ImageTk.PhotoImage(image=img)
            self.root.after(0, self._set_cam_image, photo)

        if self.cap:
            self.cap.release()
            self.cap = None

    def _set_cam_image(self, photo):
        self.cam_photo = photo   # keep reference
        self.cam_lbl.config(image=photo, text="", height=0)

    def _on_marked(self, name, roll):
        self._update_stats()
        self._set_status(f"✅ Attendance marked: {name}  ({roll})", "#4ade80")
        self.show_today()

    def stop_camera(self):
        self.is_capturing = False
        self.cam_lbl.config(
            image="", text="Camera stopped\nClick 'Start Attendance' to begin again",
            fg="#4b5563", height=10
        )
        self._set_status("Camera stopped.", "#a78bfa")

    # ── TABLE VIEWS ───────────────────────────────────────────────────────────

    def _fill_table(self, rows, tag="present"):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert("", "end", values=row, tags=(tag,))

    def show_attendance(self):
        rows = db_get_attendance()
        self._fill_table(rows)
        self._set_status(f"All attendance records — {len(rows)} entries.")

    def show_today(self):
        today = date.today().strftime("%Y-%m-%d")
        rows  = db_get_attendance(today)
        self._fill_table(rows)
        self._update_stats()
        self._set_status(f"Today ({today}) — {len(rows)} student(s) present.")

    def show_students(self):
        students = db_get_students()
        for item in self.tree.get_children():
            self.tree.delete(item)
        for name, roll, _ in students:
            self.tree.insert("", "end",
                values=(name, roll, "—", "—", "Registered"), tags=("student",))
        self._set_status(f"Registered students — {len(students)} total.")

    # ── TOOLS ─────────────────────────────────────────────────────────────────

    def export_csv(self):
        rows = db_get_attendance()
        if not rows:
            messagebox.showinfo("Empty", "No records to export.", parent=self.root)
            return
        fname = f"attendance_{date.today()}.csv"
        with open(fname, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["Name", "Roll No", "Date", "Time", "Status"])
            w.writerows(rows)
        self._set_status(f"✅ Exported → {os.path.abspath(fname)}", "#4ade80")
        messagebox.showinfo("Exported",
            f"Saved successfully!\n\n📁 {os.path.abspath(fname)}", parent=self.root)

    def delete_student(self):
        roll = simpledialog.askstring("Delete Student",
            "Enter Roll No of student to delete:", parent=self.root)
        if not roll:
            return
        roll = roll.strip().upper()
        students = {s[1]: s[0] for s in db_get_students()}
        if roll not in students:
            messagebox.showerror("Not Found",
                f"Roll No '{roll}' not found!", parent=self.root)
            return
        confirm = messagebox.askyesno("Confirm Delete",
            f"Delete student: {students[roll]} ({roll})?\nThis cannot be undone!",
            parent=self.root)
        if confirm:
            db_delete_student(roll)
            self._update_stats()
            self.show_students()
            self._set_status(f"🗑 Deleted: {students[roll]} ({roll})", "#f87171")

    def clear_today(self):
        confirm = messagebox.askyesno("Clear Today",
            "Clear all attendance marks for today?\nThis cannot be undone!",
            parent=self.root)
        if confirm:
            self.marked_today.clear()
            conn = sqlite3.connect(DB_FILE)
            c = conn.cursor()
            today = date.today().strftime("%Y-%m-%d")
            c.execute("DELETE FROM attendance WHERE date=?", (today,))
            conn.commit()
            conn.close()
            self._update_stats()
            self.show_today()
            self._set_status("✅ Today's attendance cleared.", "#facc15")


# ─── ENTRY POINT ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    root = tk.Tk()
    app  = AttendanceApp(root)
    root.mainloop()
