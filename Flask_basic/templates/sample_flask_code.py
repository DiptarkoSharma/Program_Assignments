from flask import Flask,redirect,url_for,render_template,request
#WSGI Application instance

#Building URL dynamically
app = Flask(__name__)

@app.route('/home')
def my_home():
    return 'Welcome to my home page'

@app.route('/success/<int:score>')
def success(score):
    return "<h1>The person has passed and the score is <h1>"+ str(score)


if __name__ == '__main__':
    app.run(debug=True)

