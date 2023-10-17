from flask import Flask, jsonify, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Python Developer',
    'location': 'New York',
    'salary': '$100,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Atlanta',
}, {
    'id': 3,
    'title': 'Software Engineer',
    'location': 'Chicago',
    'salary': '$90,000'
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Houston',
    'salary': '$86,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company="Redd")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
