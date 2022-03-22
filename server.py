from flask import render_template,request,Flask,redirect

app = Flask(__name__,template_folder='templates')


@app.route('/')
def index():
    return render_template('hello.html')

@app.route('/results')
def resultfunction():
    results = {'Accuracy Percentage': 90,'f1score Percentage': 81}
    return results

print("Hello World")
    
if __name__=="__main__":
    app.debug = True
    app.run(host='0.0.0.0')


