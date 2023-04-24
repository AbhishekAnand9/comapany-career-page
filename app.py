from flask import Flask, render_template , jsonify
app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'title':'data analyst',
    'location':'bengaluru,India',
    'salary':'₹12 LPA'
  },
   {
    'id':2,
    'title':'data scientist',
    'location':'kolkata,India',
     'salary' : '₹7LPA'
  },
   {
    'id':3,
    'title':'Front-end-Engineer',
    'location':'Mumbai,India',
    'salary':'₹10 LPA'
  },
   {
    'id':4,
    'title':'back-end-engineer',
    'location':'San fransisco,USA',
    'salary':'$120,000 PA'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='CompanyName')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__== "__main__":
  app.run(host='0.0.0.0', debug=True)
  