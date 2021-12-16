#Integrate HTML with flask
##HTTP verb GET  and POST

##JINJA2 Template
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score < 50:
        res= 'FAIL'
    else:
        res='PASS'
    exp={'score':score,'result':res}
    return render_template('results.html',result=exp)


@app.route('/fail/<int:score>')
def fail(score):
    return "<html><body></body><h1>The person has failed and  scored this marks {{{score}}}  </h1></html>"
###Result Checker
@app.route('/result/<int:marks>')
def result(marks):
    result=""
    if marks<50:
        result= 'fail'
    else:
        result='pass1'
    return redirect(url_for(result,score=marks))

##REsult Checker submit HTML PAGE
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience']) 
        total_score=(maths+science+c+data_science)/4
    
    return redirect(url_for('success',score=total_score))
if __name__ == '__main__':
    app.run(debug=True)
