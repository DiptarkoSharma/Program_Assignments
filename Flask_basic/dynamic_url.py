'''
    Integrate Jinja with HTML.
    {% %} - loops
    {{val}} - values
    {# #} -Comments

'''


from flask import Flask,redirect,url_for,render_template,request
#WSGI Application instance

#Building URL dynamically
app = Flask(__name__)
@app.route('/')
def welcome():
    #return ' Welcome World to my code'
    return render_template('index.html')

@app.route('/home')
def my_home():
    return '<h1>Welcome to my home page</h1>'

@app.route('/success/<int:score>')
def success(score):
   
    return f"<h1>You have passed, your marks is {str(score)}</h1>"
@app.route('/fail/<int:score>')
def fail(score):
    return f"<h1>You have failed, your marks is {str(score)}</h1>"

@app.route('/results/<int:marks>')
def results(marks):
    if marks >= 50:
        result = 'success'
    else:
        result = 'fail'
    print(result)
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    app.run(debug=True)

    
