import tkinter as tk
from tkinter import ttk, messagebox

# Sample job data
jobs = [
    {"title": "Software Developer", "company": "TechCorp", "location": "Remote"},
    {"title": "Data Analyst", "company": "DataSolutions", "location": "New York"},
    {"title": "UI/UX Designer", "company": "DesignHub", "location": "San Francisco"},
]

# Function to apply for a job
def apply_job(job):
    messagebox.showinfo("Application Sent", f"You applied for {job['title']} at {job['company']}")

# Function to display jobs
def show_jobs(filter_text=""):
    for widget in job_frame.winfo_children():
        widget.destroy()
    for job in jobs:
        if filter_text.lower() in job['title'].lower():
            card = ttk.Frame(job_frame, padding=10, relief="raised")
            card.pack(fill="x", pady=5)

            ttk.Label(card, text=job["title"], font=("Arial", 14, "bold")).pack(anchor="w")
            ttk.Label(card, text=f"{job['company']} - {job['location']}", font=("Arial", 11)).pack(anchor="w")

            apply_btn = ttk.Button(card, text="Apply", command=lambda j=job: apply_job(j))
            apply_btn.pack(anchor="e")

# Search functionality
def search_jobs():
    search_text = search_var.get()
    show_jobs(search_text)

# Main window
root = tk.Tk()
root.title("GigMate - Job Finder")
root.geometry("500x500")

# Search bar
search_var = tk.StringVar()
search_entry = ttk.Entry(root, textvariable=search_var, width=30)
search_entry.pack(pady=10)
ttk.Button(root, text="Search", command=search_jobs).pack()

# Job list frame
job_frame = ttk.Frame(root)
job_frame.pack(fill="both", expand=True, padx=10, pady=10)

show_jobs()

root.mainloop()
