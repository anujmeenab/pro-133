#Importing flask module in the project
from flask import Flask,render_template

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/SA")

#‘/’ URL is bound with first_flask function.


#run the application on local server




def student_webpage():
    name="anuj"
    return render_template("SA.html",student_name=name)
app.run(debug=True)
