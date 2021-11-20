from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask.templating import render_template_string
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import DatabaseError, SQLAlchemyError
from helpers import login_required, apology
from flask_session import Session
import sys
import os
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
# from sqlalchemy.orm import sessionmaker

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:abcd@localhost/company_db'

db = SQLAlchemy(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
# Session = session(bind = engine)

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
    companyid=db.Column(db.Integer)
    departmentid=db.Column(db.Integer)
   
    

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

class Technologies(db.Model):
    __tablename__ = 'technologies'

    techid = db.Column(db.Integer,primary_key=True)
    tname = db.Column(db.String())
    companyid=db.Column(db.Integer,primary_key=True)
    departmentid=db.Column(db.Integer,primary_key=True)
	

    def __init__(self, techid,tname,companyid, departmentid):
      self.techid=techid
      self.tname=tname
      self.companyid=companyid
      self.departmentid = departmentid

class Teaching(db.Model):
    __tablename__ = 'teaching'

    teacher_rating= db.Column(db.Integer)
    teacher_ssn= db.Column(db.String(), nullable=False)
    techid= db.Column(db.Integer,primary_key=True)
    companyid=db.Column(db.Integer,primary_key=True)
    departmentid=db.Column(db.Integer,primary_key=True)
    
    

    def __init__(self, teacher_rating,teacher_ssn,techid,companyid, departmentid):
      self.techid=techid
      self.teacher_rating=teacher_rating
      self.teacher_ssn=teacher_ssn
    #   self.tech_name=tech_name
      self.companyid=companyid
      self.departmentid = departmentid
      
class Learning(db.Model):
    __tablename__ = 'learning'

    student_score= db.Column(db.Integer)
    trainee_ssn= db.Column(db.String(),primary_key=True)
    # tech_name=db.Column(db.String())
    techid= db.Column(db.Integer,primary_key=True)
    companyid=db.Column(db.Integer,primary_key=True)
    departmentid=db.Column(db.Integer,primary_key=True)

    def __init__(self, student_score,trainee_ssn,techid,companyid, departmentid):
      self.techid=techid
      self.student_score=student_score
      self.trainee_ssn=trainee_ssn
    #   self.tech_name=tech_name
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
		companies = db.session.query(Company).filter(Company.companyid == request.form.get("companyid"))
		
		results = [
		{
			"companyid": company.companyid, 
			"cname": company.cname
		}
		for company in companies]

		# Ensure company exists and password is correct
		if len(results) != 1:# or not check_password_hash(rows[0]["hash"], request.form.get("password")):
			return apology("invalid Company ID", 403)

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
	# ratings_teacher=Teaching.query.filter(Teaching.companyid==session["companyid"]).order_by(Teaching.teacher_rating)
	# rating_student=Learning.query.filter(Learning.companyid==session["companyid"]).order_by(Learning.student_score)
	results = [
    {
		"departmentName": department.dname,
        "departmentID": department.departmentid, 
        "managerSSN": department.mgr_ssn,
		"companyID": department.companyid
    }
    for department in departments]
	
	# results = [
    # {
	# 	"teacher_ssn": rating.teacher_ssn,
	# 	"teacher_rating":rating.teacher_rating,
    #     "departmentID": rating.departmentid, 
		
    # }
    # for rating in ratings_teacher]
	# results2 = [
    # {
	# 	"trainee_ssn":rating.trainee_ssn,
	# 	"student_rating":rating.student_score, 
	# 	"departmentID": rating.departmentid, 

		
    # }
    # for rating in rating_student]
  
	return render_template('departments.html', row=results)


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
	# teachers=Teaching.query.join(Employee,Employee.ssn==Teaching.teacher_ssn).filter
	# teachers = Teaching.query.join(Employee)\
	# 					.add_columns(Teaching.techid, Teaching.teacher_rating, Teaching.teacher_ssn, Teaching.tech_name, Teaching.companyid, Teaching.departmentid, Employee.name)\
	# 					.filter(Teaching.companyid == session["companyid"])
	
	teachers = db.session.execute("select * from teaching\
		 						inner join technologies on\
								(teaching.techid = technologies.techid and teaching.departmentid = technologies.departmentid and teaching.companyid=technologies.companyid)\
								inner join employee on teaching.teacher_ssn = employee.ssn\
								where teaching.companyid=:id",\
								{'id': session["companyid"]})
	# print(session["companyid"], file=sys.stdout)
	# teachers = Teaching.query.from_statement(db.text("select * from teaching inner join employee on teaching.teacher_ssn = employee.ssn where Teaching.companyid=:id").params(id=session["companyid"]))
	teacher_result = [
    {
		"techid": teacher.techid,
		"teacher_rating": teacher.teacher_rating,
		"teacher_ssn": teacher.teacher_ssn,
		"tech_name": teacher.tname,
		"companyid": teacher.companyid,
		"departmentid":  teacher.departmentid,
		"tname": teacher.name
    }
    for teacher in teachers]
# 1
# 	list of learner==how many learning this technologies
	learner_result = dict()
	for teacher in teacher_result:
		# learners = Learning.query.filter(Learning.companyid == session["companyid"], Learning.techid == teacher['techid'])
		learners = db.session.execute("select * from learning inner join employee on learning.trainee_ssn = employee.ssn\
									inner join technologies on learning.techid = technologies.techid and learning.companyid=technologies.companyid\
									where learning.companyid=:id and Learning.techid = :techid order by student_score desc",
		 							{'id': session["companyid"], 'techid': teacher['techid']})

		learner_result[teacher["techid"]] = [
		{
			"techid": learner.techid,
			"student_score": learner.student_score,
			"trainee_ssn": learner.trainee_ssn,
			"tech_name": learner.tname,
			"companyid": learner.companyid,
			"departmentid": learner.departmentid,
			"name": learner.name
		}
		for learner in learners]

	return render_template('teaching.html', teacher_result =teacher_result, learner_result = learner_result)


@app.route('/insert',methods=["GET","POST"])
@login_required
def insert():
	if request.method=="POST":
		x = request.form.get('stuff') + 'Ins'
		return redirect('/' + x)
	else:
		return render_template('insertions/insertion_head.html')


@app.route('/technologiesIns',methods=["GET","POST"])
@login_required
def ins():
	if request.method=="POST":
		techid=request.form.get('techid')
		tname=request.form.get('tname')
		companyid=session["companyid"]
		departmentid=request.form.get('departmentid')
		try:

			tec=Technologies(techid, tname, companyid, departmentid)
			db.session.add(tec)
			db.session.commit()
		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error
		return redirect('/technologies')
	else:
		return render_template('insertions/insert_tech.html')

@app.route('/teachingIns',methods=["GET","POST"])
@login_required
def ins1():
	if request.method=="POST":
		teacher_rating=request.form.get('teacher_rating')
		teacher_ssn=request.form.get('teacher_ssn')
		techid=request.form.get('techid')
		# tname=request.form.get('tname')
		companyid=session["companyid"]
		departmentid=request.form.get('departmentid')
		try:
			tec=Teaching(teacher_rating,teacher_ssn,techid,companyid, departmentid)
			
			db.session.add(tec)
			db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		
		return redirect('/classes')
	else:
		return render_template('insertions/insert_teach.html')
@app.route('/learningIns',methods=["GET","POST"])
@login_required
def ins2():
	if request.method=="POST":
		student_score=request.form.get('student_score')
		trainee_ssn=request.form.get('trainee_ssn')
		techid=request.form.get('techid')
		companyid=session["companyid"]
		departmentid=request.form.get('departmentid')
		try:
			tec=Learning(student_score,trainee_ssn,techid,companyid, departmentid)
			
			db.session.add(tec)
			db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		
		return redirect('/classes')
	else:
		return render_template('insertions/insert_learn.html')
		
@app.route('/employeeIns',methods=["GET","POST"])
@login_required
def ins2q():
	if request.method=="POST":
		salary=request.form.get('salary')
		ssn=request.form.get('ssn')
		employeeid=request.form.get('employeeid')
		address=request.form.get('address')
		phone_number=request.form.get('phone_number')
		job=request.form.get('job')
		departmentid=request.form.get('departmentid')
		name=request.form.get('name')
		companyid=session["companyid"]
		departmentid=request.form.get('departmentid')

		try:
			tec=Employee(ssn,name,employeeid,address,phone_number,job,salary,companyid,departmentid)
			
			db.session.add(tec)
			db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		
		return redirect('/employees')
	else:
		return render_template('insertions/insert_employee.html')


@app.route('/update',methods=["GET","POST"])
@login_required
def update():
	if request.method=="POST":
		x = request.form.get('stuff') + 'Ups'
		return redirect('/' + x)
	else:
		return render_template('updations/updation_head.html')

@app.route('/technologiesUps',methods=["GET","POST"])
@login_required
def TechUps():
	if request.method=="POST":
		companyid=session["companyid"]	   
		techid=request.form.get('techid')		
		departmentid=request.form.get('departmentid')

		try:
			q = Technologies.query.filter(
					Technologies.companyid == companyid,
					Technologies.techid == techid,
					Technologies.departmentid == departmentid
				)

			if q.count() == 0:
				flash("No such record exists")
				return redirect('/technologiesUps')
			else:
				tname = request.form.get('tname') or q[0].tname
				q.update({'tname' : (tname)})
				
				db.session.commit()
		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		return redirect('/technologies')
	else:
		return render_template('updations/update_tech.html')

@app.route('/teachingUps',methods=["GET","POST"])
@login_required
def TeachUps():
	if request.method=="POST":
		companyid=session["companyid"]
		techid=request.form.get('techid')
		departmentid=request.form.get('departmentid')

		try:
			# Get record
			q = Teaching.query.filter(
				Teaching.companyid == companyid, Teaching.techid == techid, Teaching.departmentid == departmentid
			)
			
			if q.count() == 0:
				flash("No such record exists")
				return redirect('/teachingUps')
			else:
				teacher_rating = request.form.get('teacher_rating') or q[0].teacher_rating
				teacher_ssn = request.form.get('teacher_ssn')  or q[0].teacher_ssn

				db.session.execute('''UPDATE Teaching SET teacher_rating=:teacher_rating,   
				teacher_ssn=:teacher_ssn     
				WHERE   
				companyid=:companyid and techid=:techid and departmentid=:departmentid ''',{
						'teacher_rating':(teacher_rating),
						'teacher_ssn':(teacher_ssn),
						'companyid':companyid,
						'techid':techid,
						'departmentid':departmentid}						
					)
				
				db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		return redirect('/classes')
	else:
		return render_template('updations/update_teaching.html')

@app.route('/learningUps',methods=["GET","POST"])
@login_required
def LearnUps():
	if request.method == "POST":
		companyid = session["companyid"]
		trainee_ssn = request.form.get('trainee_ssn')
		techid = request.form.get('techid')
		departmentid = request.form.get('departmentid')
		try:
			q = Learning.query.filter(
					Learning.companyid == session["companyid"],
					Learning.techid == techid,
					Learning.departmentid == departmentid,
					Learning.trainee_ssn == trainee_ssn
				)
			if q.count() == 0:
				flash("No such record exists")
				return redirect('/learningUps')
			else:
				student_score = request.form.get('student_score') or q[0].student_score				
				q.update({'student_score':(student_score)})
				db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		
		return redirect('/classes')
	else:
		return render_template('updations/update_learning.html')

@app.route('/employeeUps',methods=["GET","POST"])
@login_required
def EmployeeUps():
	if request.method == "POST":
		companyid=session["companyid"]
		ssn=request.form.get('ssn')
		try:
			q = Employee.query.filter(Employee.ssn == ssn)
			if q.count() == 0:
				flash("No such record exists")
				return redirect('/employeeUps')
			else:				
				salary = request.form.get('salary') or q[0].salary
				employeeid = request.form.get('employeeid') or q[0].employeeid
				address = request.form.get('address') or q[0].address
				phone_number = request.form.get('phone_number') or q[0].phone_number
				job = request.form.get('job') or q[0].job
				departmentid = request.form.get('departmentid') or q[0].departmentid
				name = request.form.get('name')	or q[0].name
				
				# q.update(
						
				# 	)
				db.session.execute('''UPDATE Employee SET salary=:salary,   
				employeeid = :employeeid,
				address=:address,
				phone_number=:phone_number,
				job=:job,
				departmentid=:departmentid,
				name=:name     
				WHERE   
				ssn=:ssn''',{'salary':(salary),
						'employeeid':(employeeid),
						'address':(address),
						'phone_number':(phone_number),
						'job':(job),
						'departmentid':(departmentid),
						'name':(name),
						'ssn':ssn})
				db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		
		return redirect('/employees')
	else:
		return render_template('updations/update_employee.html')


@app.route('/delete',methods=["GET","POST"])
@login_required
def delete():
	if request.method == "POST":
		x = '/' + request.form.get('stuff') + 'Del'
		return redirect(x)
	else:
		return render_template('deletions/deletion_head.html')

@app.route('/technologiesDel',methods=["GET","POST"])
@login_required
def v():
	if request.method == "POST":
		techid = request.form.get('techid')
		companyid = session["companyid"]
		departmentid = request.form.get('departmentid')

		try:
			# Delete record
			q = Technologies.query.filter(
				Technologies.companyid == companyid,
				Technologies.departmentid == departmentid,
				Technologies.techid == techid
			)
			if q.count() == 0:
				flash("No such record exists")
				return redirect('/technologiesDel')
			else:
				q.delete()
				db.session.commit()
		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		return redirect('/technologies')
	else:
		return render_template('deletions/delete_tech.html')

@app.route('/teachingDel',methods=["GET","POST"])
@login_required
def teachingDel():
	if request.method == "POST":
		companyid = session["companyid"]
		techid = request.form.get('techid')
		departmentid = request.form.get('departmentid')

		try:
			# Delete teacher
			q = Teaching.query.filter(
				Teaching.companyid == companyid,
				Teaching.departmentid == departmentid,
				Teaching.techid == techid
			)
			
			if q.count() == 0:
				flash("No such record exists")
				return redirect('/teachingDel')

			else:
				q.delete()
				db.session.commit()
		
		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		return redirect('/classes')
	else:
		return render_template('deletions/delete_teach.html')

@app.route('/learningDel',methods=["GET","POST"])
@login_required
def learningDel():
	if request.method == "POST":
		companyid = session["companyid"]
		trainee_ssn = request.form.get('trainee_ssn')
		techid = request.form.get('techid')
		departmentid = request.form.get('departmentid')

		try:
			# Delete learner
			q = Learning.query.filter(
				Learning.companyid == companyid,
				Learning.departmentid == departmentid,
				Learning.techid == techid,
				Learning.trainee_ssn == trainee_ssn
			)
			
			if q.count() == 0:
				flash("No such record exists")
				return redirect('/learningDel')

			else:
				q.delete()
				db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error

		
		return redirect('/classes')
	else:
		return render_template('deletions/delete_learn.html')
		
@app.route('/employeeDel',methods=["GET","POST"])
@login_required
def employeeDel():
	if request.method == "POST":
		ssn = request.form.get('ssn')

		try:
			# Delete employee
			q = Employee.query.filter(Employee.ssn == ssn)
			
			if q.count() == 0:
				flash("No such record exists")
				return redirect('/employeeDel')

			else:
				q.delete()
				db.session.commit()

		except SQLAlchemyError as e:
			error = str(e.__dict__['orig'])
			return error
		
		return redirect('/employees')
	else:
		return render_template('deletions/delete_employee.html')


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




 
	# ratings_teach_to_student this one table will have teacher(ssn) student(ssn) rating(1:n relation)  teacher rates the student
	# ratings_student_to_teach this one table will have teacher(ssn) student(ssn) rating(1:n relation) student rates the teacher 
	