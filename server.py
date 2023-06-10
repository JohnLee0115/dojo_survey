from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['favlang'] = request.form['favlang']
    session['comment'] = request.form['comment']
    print(request.form)
    return redirect('/result')

@app.route('/result/')
def show_result():
    return render_template('results.html')

if __name__=="__main__":
    app.run(debug=True)