from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy, and_
from helpers import login_required, apology
from flask_session import Session
import sys
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:abcd@localhost/company_db'

db = SQLAlchemy(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

class Company(db.Model):
  __tablename__ = 'company'

  companyid = db.Column(db.Integer, primary_key=True)
  cname = db.Column(db.String())

  def __init__(self, companyid, cname):
    self.companyid = companyid
    self.cname = cname
  
  def __repr__(self):
    return f"<Company name: {self.cname}"


class Department(db.Model):
	__tablename__ = 'department'


	dname=db.Column(db.String()) 
	mgr_ssn=db.Column(db.String(9))
	companyid=db.Column(db.Integer,primary_key=True)
	departmentid=db.Column(db.Integer,primary_key=True)


	def __init__(self, dname,mgr_ssn,companyid,departmentid):
		self.dname=dname
		self.mgr_ssn = mgr_ssn
		self.companyid=companyid
		self.departmentid = departmentid

class Employee(db.Model):
    __tablename__ = 'employee'
    ssn=db.Column(db.String(),primary_key=True) 
    name=db.Column(db.String()) 
    employeeid=db.Column(db.Integer) 
    address=db.Column(db.String()) 
    phone_number=db.Column(db.BigInteger) 
    job= db.Column(db.String()) 
    salary=db.Column(db.Float())
    companyid=db.Column(db.Integer,primary_key=True)
    departmentid=db.Column(db.Integer,primary_key=True)
    

    def __init__(self,ssn,name,employeeid,address,phone_number,job,salary,companyid,departmentid):
      self.ssn=ssn
      self.name = name
      self.employeeid=employeeid
      self.address=address
      self.phone_number=phone_number
      self.job=job
      self.salary=salary
      self.companyid=companyid
      self.departmentid = departmentid
#   CREATE TABLE TECHNOLOGIES
#  (	
# 	TechID INT NOT NULL, 
# 	Tname VARCHAR(35) NOT NULL,
# 	CompanyID INT NOT NULL,
# 	DepartmentID INT NOT NULL,
class Technologies(db.Model):
    __tablename__ = 'technologies'

    techid = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String())
    companyid=db.Column(db.Integer,primary_key=True)
    departmentid=db.Column(db.Integer,primary_key=True)

    def __init__(self, techid,tname,companyid, departmentid):
      self.techid=techid
      self.tname=tname
      self.CompanyID=companyid
      self.DepartmentID = departmentid
#   CREATE TABLE Teaching
#  (	
# 	Teacher_rating INT NOT NULL,
# 	Teacher_SSN CHAR(9) NOT NULL,
# 	Tech_Name VARCHAR(50) NOT NULL, 
# 	Techid INT ,
# 	DepartmentID INT NOT NULL,
# 	CompanyID INT NOT NULL,
#PRIMARY KEY (Techid, DepartmentID, CompanyID, Teacher_SSN),
class Teaching(db.Model):
    __tablename__ = 'teaching'

    teacher_rating= db.Column(db.Integer)
    teacher_ssn= db.Column(db.String(),primary_key=True)
    tech_name=db.Column(db.String())
    techid= db.Column(db.Integer,primary_key=True)
    companyid=db.Column(db.Integer,primary_key=True)
    departmentid=db.Column(db.Integer,primary_key=True)

    def __init__(self, teacher_rating,teacher_ssn,tech_name,techid,companyid, departmentid):
      self.techid=techid
      self.teacher_rating=teacher_rating
      self.teacher_ssn=teacher_ssn
      self.tech_name=tech_name
      self.companyid=companyid
      self.departmentid = departmentid
      
# CREATE TABLE Learning
#  (	
# 	Student_score INT NOT NULL,
# 	Trainee_SSN CHAR(9) NOT NULL,
# 	Tech_Name VARCHAR(50) NOT NULL, 
# 	Techid INT ,
# 	DepartmentID INT NOT NULL,
# 	CompanyID INT NOT NULL,
# 	PRIMARY KEY (Techid, DepartmentID, CompanyID, Trainee_SSN),
# 	FOREIGN KEY (Techid, DepartmentID, CompanyID) REFERENCES Technologies(TechID,DepartmentID,CompanyID),
# 	FOREIGN KEY(DepartmentID, CompanyID) REFERENCES DEPARTMENT(DepartmentID, CompanyID),
# 	FOREIGN KEY (Trainee_SSN) REFERENCES Employee(Ssn)
# 	);
class Learning(db.Model):
    __tablename__ = 'learning'

    student_score= db.Column(db.Integer)
    trainee_ssn= db.Column(db.String(),primary_key=True)
    tech_name=db.Column(db.String())
    techid= db.Column(db.Integer,primary_key=True)
    companyid=db.Column(db.Integer,primary_key=True)
    departmentid=db.Column(db.Integer,primary_key=True)

    def __init__(self, student_score,trainee_ssn,tech_name,techid,companyid, departmentid):
      self.techid=techid
      self.student_score=student_score
      self.trainee_ssn=trainee_ssn
      self.tech_name=tech_name
      self.companyid=companyid
      self.departmentid = departmentid


# Default page before logging in
@app.route('/login', methods=["GET", "POST"])
def login():
 	# Forget any user_id
	session.clear()

 	# User reached route via POST (as by submitting a form via POST)
	if request.method == "POST":

		# Ensure username was submitted
		if not request.form.get("companyid"):
			return apology("must provide Company ID", 403)

		# Ensure password was submitted
		# elif not request.form.get("password"):
		# 	return apology("must provide password", 403)

		# Query database for username
		companies = db.session.query(Company).filter(Company.companyid == int(request.form.get("companyid")))
		
		results = [
		{
			"companyid": company.companyid, 
			"cname": company.cname
		}
		for company in companies]

		# Ensure company exists and password is correct
		if len(results) != 1:# or not check_password_hash(rows[0]["hash"], request.form.get("password")):
			return apology("invalid username and/or password", 403)

		# Remember which user has logged in
		session["companyid"] = results[0]["companyid"]

		# Redirect user to home page
		return redirect("/")

	# User reached route via GET (as by clicking a link or via redirect)
	else:
		return render_template("login.html")

# Route for when logout is clicked
@app.route("/logout")
def logout():
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

# Home page
@app.route('/')
@login_required
def index():
	companies = Company.query.filter(Company.companyid == session["companyid"])
	results = [
	{
		"companyid": company.companyid, 
		"cname": company.cname
	}
	for company in companies]

	return render_template('index.html', row = results)

# Show departments table
@app.route('/departments')
@login_required
def departments():
	departments = Department.query.filter(Department.companyid == session["companyid"])

	results = [
    {
		"departmentName": department.dname,
        "departmentID": department.departmentid, 
        "managerSSN": department.mgr_ssn,
		"companyID": department.companyid
    }
    for department in departments]

	return render_template('departments.html', row = results)

# Show employee table
@app.route('/employees')
@login_required
def employees():
	employees = Employee.query.filter(Employee.companyid == session["companyid"])

	results = [
    {
		"ssn": employee.ssn,
		"name": employee.name,
		"employeeid": employee.employeeid,
		"address": employee.address,
		"phone_number": employee.phone_number,
		"job": employee.job,
		"salary": employee.salary,
		"companyid": employee.companyid,
		"departmentid": employee.employeeid
    }
    for employee in employees]

	return render_template('employees.html', row = results)

# Show technologies table
@app.route('/technologies')
@login_required
def technologies():
	technologies = Technologies.query.filter(Technologies.companyid == session["companyid"])

	results = [
    {
		"techid": technology.techid,
		"tname": technology.tname,
		"companyid": technology.companyid,
		"departmentid": technology.departmentid
    }
    for technology in technologies]

	return render_template('technologies.html', row = results)

# Show technologies table
@app.route('/classes')
@login_required
def classes():
	teachers = Teaching.query.filter(Teaching.companyid == session["companyid"])

	teacher_result = [
    {
		"techid": teacher.techid,
		"teacher_rating": teacher.teacher_rating,
		"teacher_ssn": teacher.teacher_ssn,
		"tech_name": teacher.tech_name,
		"companyid": teacher.companyid,
		"departmentid":  teacher.departmentid
    }
    for teacher in teachers]

	learner_result = dict()
	for teacher in teachers:
		learners = Learning.query.filter(and_(Learning.companyid == session["companyid"], Learning.techid == teacher.techid))

		learner_result[teacher.techid] = [
		{
			"techid": learner.techid,
			"student_score": learner.student_score,
			"trainee_ssn": learner.trainee_ssn,
			"tech_name": learner.tech_name,
			"companyid": learner.companyid,
			"departmentid": learner.departmentid
		}
		for learner in learners]

	return render_template('technologies.html', teacher_result = teacher_result, learner_result = learner_result)

'''
self.techid=techid
self.teacher_rating=teacher_rating
self.teacher_ssn=teacher_ssn
self.tech_name=tech_name
self.companyid=companyid
self.departmentid = departmentid

self.techid=techid
self.student_score=student_score
self.trainee_ssn=trainee_ssn
self.tech_name=tech_name
self.companyid=companyid
self.departmentid = departmentid
'''

if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug = True)

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)