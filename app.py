from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from helpers import login_required, apology
from flask_session import Session

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Messi10@localhost/company_db'

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

		# Ensure username exists and password is correct
		# if len(rows) != 1:# or not check_password_hash(rows[0]["hash"], request.form.get("password")):
		# 	return apology("invalid username and/or password", 403)

		# Remember which user has logged in
		session["user_id"] = request.form.get("companyid")#rows[0]["id"]

		# Redirect user to home page
		return redirect("/")

	# User reached route via GET (as by clicking a link or via redirect)
	else:
		return render_template("login.html")

@app.route('/')
@login_required
def index():
  companies = Company.query.all()
  results = [
    {
        "companyid": company.companyid, 
        "cname": company.cname
    }
    for company in companies]

  return {"count": len(results), "companies": results}
  # return render_template('index.html')

# @app.route('/submit', methods=['POST'])
# def submit():
#   fname = request.form['fname']
#   lname = request.form['lname']
#   pet = request.form['pets']

#   company = Company(fname,lname,pet)
#   db.session.add(company)
#   db.session.commit()

#   #fetch a certain student2
#   companyResult = db.session.query(Company).filter(Company.id==1)

#   for result in companyResult:
#     print(result.cname)

#   return render_template('success.html', data=fname)


if __name__ == '__main__':  #python interpreter assigns "__main__" to the file you run
  app.run(debug = True)





