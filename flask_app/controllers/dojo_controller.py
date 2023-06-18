from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.dojo_model import Dojo


@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def submit_form():
    
    if not Dojo.validate_dojo(request.form):
        return redirect('/')

    results = Dojo.add_dojo(request.form)

    return redirect(f'/result/{results}')

@app.route('/result/<int:id>')
def show_result(id):

    one_dojo = Dojo.get_one({'id' :id })

    return render_template('results.html', one_dojo = one_dojo)
