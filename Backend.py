from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(GigMate)

# In-memory storage
users = {}          # user_id -> {username, role}
jobs = {}           # job_id -> {title, description, employer_id}
applications = []   # list of {job_id, employee_id}

# Helper
def generate_id():
    return str(uuid4())

# Route: Register
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    user_id = generate_id()
    users[user_id] = {
        "username": data["username"],
        "role": data["role"]  # 'employer' or 'employee'
    }
    return jsonify({"message": "User registered", "user_id": user_id}), 201

# Route: Post a job
@app.route("/jobs", methods=["POST"])
def post_job():
    data = request.json
    employer_id = data["employer_id"]
    
    if users.get(employer_id, {}).get("role") != "employer":
        return jsonify({"error": "Only employers can post jobs"}), 403

    job_id = generate_id()
    jobs[job_id] = {
        "title": data["title"],
        "description": data["description"],
        "employer_id": employer_id
    }
    return jsonify({"message": "Job posted", "job_id": job_id}), 201

# Route: Apply for job
@app.route("/apply", methods=["POST"])
def apply():
    data = request.json
    employee_id = data["employee_id"]
    job_id = data["job_id"]

    if users.get(employee_id, {}).get("role") != "employee":
        return jsonify({"error": "Only employees can apply"}), 403

    if job_id not in jobs:
        return jsonify({"error": "Invalid job ID"}), 404

    applications.append({"job_id": job_id, "employee_id": employee_id})
    return jsonify({"message": "Application submitted"}), 200

# Route: View jobs
@app.route("/jobs", methods=["GET"])
def list_jobs():
    return jsonify(jobs)

# Route: View applications for a job
@app.route("/applications/<job_id>", methods=["GET"])
def view_applications(job_id):
    job_apps = [app for app in applications if app["job_id"] == job_id]
    return jsonify(job_apps)

# Start the server
if GigMate == "__main__":
    app.run(debug=True)
