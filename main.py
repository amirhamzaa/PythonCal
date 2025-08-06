import tkinter as tk
from tkinter import messagebox

# ================= Grade Mapping ===================
def percentage_to_grade_point_letter(percentage):
    if percentage >= 80:
        return 4.0, "A+"
    elif 75 <= percentage < 80:
        return 3.75, "A"
    elif 70 <= percentage < 75:
        return 3.5, "A-"
    elif 65 <= percentage < 70:
        return 3.25, "B+"
    elif 60 <= percentage < 65:
        return 3.0, "B"
    elif 55 <= percentage < 60:
        return 2.75, "B-"
    elif 50 <= percentage < 55:
        return 2.5, "C+"
    elif 45 <= percentage < 50:
        return 2.25, "C"
    elif 40 <= percentage < 45:
        return 2.0, "D"
    else:
        return 0.0, "F"

# ================= Calculation =====================
def calculate_final():
    try:
        mid = float(entry_mid.get())
        test = float(entry_test.get())
        assign = float(entry_assign.get())
        pres = float(entry_pres.get())
        attend = float(entry_attend.get())
        final = float(entry_final.get())

        total = (mid * 0.25) + (test * 0.10) + (assign * 0.10) + \
                (pres * 0.10) + (attend * 0.05) + (final * 0.40)

        grade_point, letter_grade = percentage_to_grade_point_letter(total)

        if letter_grade == "F":
            messagebox.showinfo("Result", f"Final Percentage: {total:.2f}%\nGrade: {letter_grade}\nGrade Point: {grade_point:.2f}\n\nI hope things go better for you next time.")
        else:
            messagebox.showinfo("Result", f"Final Percentage: {total:.2f}%\nGrade: {letter_grade}\nGrade Point: {grade_point:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for all fields.")

# ================= Dark/Light Mode Toggle =================
def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg="#121212")
        canvas.config(bg="#121212")
        for label in labels_widgets:
            label.config(bg="#121212", fg="white")
        for entry in entries_widgets:
            entry.config(bg="#1a1a1a", fg="white", insertbackground='white')
        calc_button.config(bg="#333333", fg="white")
        theme_button.config(bg="#555555", fg="white")
    else:
        root.config(bg="#f0f0f0")
        canvas.config(bg="#f0f0f0")
        for label in labels_widgets:
            label.config(bg="#f0f0f0", fg="black")
        for entry in entries_widgets:
            entry.config(bg="white", fg="black", insertbackground='black')
        calc_button.config(bg="#4CAF50", fg="white")
        theme_button.config(bg="#dddddd", fg="black")

# ================= Main UI =========================
root = tk.Tk()
root.title("Futuristic CGPA Calculator")
root.geometry("500x450")
root.resizable(False, False)
dark_mode = False

# Background canvas
canvas = tk.Canvas(root, width=500, height=450, bg="#f0f0f0")
canvas.place(x=0, y=0)

# Top toggle button
theme_button = tk.Button(root, text="Dark/Light Mode", command=toggle_theme)
theme_button.place(x=10, y=10)

# Labels and entries
labels_text = ["Mid Term", "Class Test", "Assignment",
               "Presentation", "Attendance", "Final Exam"]

labels_widgets = []
entries_widgets = []

for i, text in enumerate(labels_text):
    label = tk.Label(root, text=text, width=20, anchor="w", font=("Helvetica", 11, "bold"), bg="#f0f0f0", fg="black")
    label.place(x=50, y=50 + i*50)
    entry = tk.Entry(root, width=10, font=("Helvetica", 12), bg="white", fg="black", insertbackground='black')
    entry.place(x=300, y=50 + i*50)
    labels_widgets.append(label)
    entries_widgets.append(entry)

entry_mid, entry_test, entry_assign, entry_pres, entry_attend, entry_final = entries_widgets

# Calculate button
calc_button = tk.Button(root, text="Submit", font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", command=calculate_final)
calc_button.place(x=200, y=360)

root.mainloop()
