from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/patients')
def patients():
    return render_template('patient_page.html')

@app.route('/medications')
def medications():
    return render_template('medication_page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
