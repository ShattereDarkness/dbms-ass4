
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from helpers import login_required, apology
from flask_session import Session
import sys

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Imawesome@localhost/company'

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

    
    Dname=db.Column(db.String()) 
    Mgr_ssn=db.Column(db.String(9))
    CompanyID=db.Column(db.Integer,primary_key=True)
    DepartmentID=db.Column(db.Integer,primary_key=True)
    

    def __init__(self, Dname,Mgr_ssn,CompanyID,DepartmentID):
      self.Dname=Dname
      self.Mgr_ssn = Mgr_ssn
      self.CompanyID=CompanyID
      self.DepartmentID = DepartmentID

class Employee(db.Model):
    __tablename__ = 'employee'
    Ssn=db.Column(db.String(9),primary_key=True) 
    Name=db.Column(db.String(50)) 
    EmployeeID=db.Column(db.Integer) 
    Address=db.Column(db.String(50)) 
    Phone_number=db.Column(db.BigInteger) 
    Job= db.Column(db.String()) 
    Salary=db.Column(db.Float())
    CompanyID=db.Column(db.Integer,primary_key=True)
    DepartmentID=db.Column(db.Integer,primary_key=True)
    

    def __init__(self,Ssn,Name,EmployeeID,Address,Phone_number,Job,Salary,CompanyID,DepartmentID):
      self.Ssn=Ssn
      self.Name = Name
      self.EmployeeID=EmployeeID
      self.Address=Address
      self.Phone_number=Phone_number
      self.Job=Job
      self.Salary=Salary
      self.CompanyID=CompanyID
      self.DepartmentID = DepartmentID
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
    CompanyID=db.Column(db.Integer,primary_key=True)
    DepartmentID=db.Column(db.Integer,primary_key=True)

    def __init__(self, techid,tname,CompanyID, DepartmentID):
      self.techid=techid
      self.tname=tname
      self.CompanyID=CompanyID
      self.DepartmentID = DepartmentID
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

    Teacher_rating= db.Column(db.Integer)
    Teacher_SSN= db.Column(db.String(9),primary_key=True)
    Tech_Name=db.Column(db.String(50))
    Techid= db.Column(db.Integer,primary_key=True)
    CompanyID=db.Column(db.Integer,primary_key=True)
    DepartmentID=db.Column(db.Integer,primary_key=True)

    def __init__(self, Teacher_rating,Teacher_SSN,Tech_Name,Techid,CompanyID, DepartmentID):
      self.Techid=Techid
      self.Teacher_rating=Teacher_rating
      self.Teacher_SSN=Teacher_SSN
      self.Tech_Name=Tech_Name
      self.CompanyID=CompanyID
      self.DepartmentID = DepartmentID
      
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

    Student_score= db.Column(db.Integer)
    Trainee_SSN= db.Column(db.String(9),primary_key=True)
    Tech_Name=db.Column(db.String(50))
    Techid= db.Column(db.Integer,primary_key=True)
    CompanyID=db.Column(db.Integer,primary_key=True)
    DepartmentID=db.Column(db.Integer,primary_key=True)

    def __init__(self, Student_score,Trainee_SSN,Tech_Name,Techid,CompanyID, DepartmentID):
      self.Techid=Techid
      self.Student_score=Student_score
      self.Trainee_SSN=Trainee_SSN
      self.Tech_Name=Tech_Name
      self.CompanyID=CompanyID
      self.DepartmentID = DepartmentID

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
		# rows = db.execute("SELECT * FROM users WHERE username = :username",
		# 				username=request.form.get("username"))
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

#   return {"count": len(results), "companies": results}
  return render_template('index.html', row = results)

if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug = True)