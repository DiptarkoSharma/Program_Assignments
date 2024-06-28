'''
    Integrate Jinja with HTML.
    {% %} - loops
    {{val}} - values
    {# #} -Comments

'''

#Building HTML with Flask
#HTML verbs
from flask import Flask,redirect,url_for,render_template,request
#WSGI Application instance

#Building URL dynamically
app = Flask(__name__)
@app.route('/home')
def my_home():
    return render_template ('welcome.html')

@app.route('/success/<int:score>')
def success(score):
   
    return f"<h1>You have passed, your marks is {str(score)}</h1>"
@app.route('/fail/<int:score>')
def fail(score):
    return f"<h1>You have failed, your marks is {str(score)}</h1>"



if __name__ == '__main__':
    app.run(debug=True)

    
