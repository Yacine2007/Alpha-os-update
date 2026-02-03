import tkinter as tk
from tkinter import ttk

def start_system():
    print("جاري تشغيل النظام...")
    root.destroy()

# إعداد النافذة الرئيسية
root = tk.Tk()
root.title("Alpha OS v26.3 - Boot Sequence")
root.geometry("500x300")
root.configure(bg="#1a1a1a")  # لون خلفية داكن
root.resizable(False, False)

# تنسيق النصوص
style = ttk.Style()
style.configure("TButton", font=("Segoe UI", 10), padding=10)

# محتوى الواجهة
header_label = tk.Label(
    root, 
    text="ALPHA OS", 
    fg="#00ffcc", 
    bg="#1a1a1a", 
    font=("Courier New", 30, "bold")
)
header_label.pack(pady=(40, 5))

version_label = tk.Label(
    root, 
    text="v26.3 TEST BUILD", 
    fg="#888888", 
    bg="#1a1a1a", 
    font=("Consolas", 12)
)
version_label.pack()

status_label = tk.Label(
    root, 
    text="Welcome, System Administrator", 
    fg="#ffffff", 
    bg="#1a1a1a", 
    font=("Segoe UI", 11)
)
status_label.pack(pady=20)

# زر الدخول
enter_button = tk.Button(
    root, 
    text="INITIALIZE SYSTEM", 
    command=start_system,
    bg="#00ffcc",
    fg="#1a1a1a",
    font=("Segoe UI", 10, "bold"),
    activebackground="#00ccaa",
    bd=0,
    padx=20,
    pady=10
)
enter_button.pack(pady=20)

# تذييل الصفحة
footer_label = tk.Label(
    root, 
    text="Unauthorized access is prohibited.", 
    fg="#444444", 
    bg="#1a1a1a", 
    font=("Arial", 8)
)
footer_label.pack(side="bottom", pady=10)

root.mainloop()
