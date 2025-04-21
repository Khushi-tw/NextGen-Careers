
from flask import Flask, render_template,jsonify,request,redirect, url_for
from database import load_jobs_from_db,load_job_from_db

app = Flask(__name__, template_folder='templates')

#Route of home page
@app.route("/")
def home_page():
    jobs_list = load_jobs_from_db()
    return render_template("home.html", Jobs=jobs_list,company_name = 'NextGen')

#To get JSON of Job list
@app.route("/api/jobs_list")
def list_jobs():
    jobs_list = load_jobs_from_db()
    return jsonify(jobs_list)

#To return dat in JSON Format for api route
@app.route("/job/<id>")
def show_job(id):
    try:
        job = load_job_from_db(id)
        if job is None:
            return jsonify({"error": "Job not found"}), 404
        return jsonify(job)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

#To render jobpage.html based on job id
@app.route("/jobs/<id>")
def showing_job(id):
    job =load_job_from_db(id)
    if not job :
        return "Job Not Found."
    return render_template('jobpage.html',job=job)

#Using POST Method to fetch job id from db and submitting the form.
@app.route("/jobs/<id>/apply", methods=["POST"])
def apply_to_jobs(id):
    data = request.form
    job = load_job_from_db(id)
    return render_template('application_submit.html',application = data,job =job)



'''@app.route("/apply", methods=["POST"])
def apply():
    # Collect core form data
    name = request.form.get("name")
    email = request.form.get("email")

    # Optional fields
    linkedin = request.form.get("linkedin", "")
    github = request.form.get("github", "")

    # Education (multiple entries)
    degrees = request.form.getlist("degree[]")
    colleges = request.form.getlist("college[]")
    years = request.form.getlist("year[]")
    cgpas = request.form.getlist("cgpa[]")

    # Work Experience (multiple entries)
    companies = request.form.getlist("company[]")
    roles = request.form.getlist("job_role[]")
    responsibilities = request.form.getlist("responsibility[]")
    start_dates = request.form.getlist("start_date[]")
    end_dates = request.form.getlist("end_date[]")

    # File upload (resume)
    resume = request.files.get("resume")

    # Cover letter
    cover_letter = request.form.get("coverletter")

    # Optional: Save all data to a database or process further here
    # For now, just pass name/email to confirmation page
    return render_template("application_submit.html", name=name, email=email)
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

 