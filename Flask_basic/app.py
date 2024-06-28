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
    #return "<h1>The person has passed and the score is <h1>"+ str(score)
   
    res = ''

    if score >=50:
        res = 'Pass'
    else:
        res = 'Fail'
    expr = {'score':score,'res':res}

    #return render_template('result.html',result=expr)
    return render_template('checkresults.html',result=score)
   


@app.route('/result/<int:score>')
def result(score):
    res = ''

    if score >=50:
        res = 'Pass'
    else:
        res = 'Fail'
    expr = {'score':score,'res':res}

    return render_template('result.html',result=expr)


@app.route('/fail/<int:score>')
def fail(score):
    return render_template('failure.html')

@app.route('/results/<int:marks>')
def results(marks):
    if marks >= 50:
        result = 'success'
    else:
        result = 'fail'
    return redirect(url_for(result,score=marks))

@app.route('/submit',methods =['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        english = float(request.form['english'])
        avg_score = round((science+maths+english),2)/3
        print(f'Average score is {avg_score}')
    res =''
    if avg_score > 50:
        res = 'success'
    else:
        res = 'fail'
    #res = 'results'
    return redirect(url_for(res,score=avg_score))


if __name__ == '__main__':
    app.run(debug=True)

    
