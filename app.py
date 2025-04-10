
from flask import Flask, render_template,jsonify
from database import load_jobs_from_db
from sqlalchemy import text

app = Flask(__name__, template_folder='templates')




@app.route("/")
def hello_World():
    jobs_list = load_jobs_from_db()
    return render_template("home.html", Jobs=jobs_list,company_name = 'NextGen')

@app.route("/api/jobs_list")
def list_jobs():
    jobs_list = load_jobs_from_db()
    return jsonify(jobs_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

