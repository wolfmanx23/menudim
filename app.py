from flask import Flask
from flask import render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/dimensionamiento/cloud_pak')
def dim_cp():
    return render_template('dim_cp.html')

@app.route('/menu')
def menu():
    return render_template('men.html')

@app.route('/cr')
def cr():
    return render_template('m1.html')

@app.route('/cp4d')
def hello():
    return redirect("https://ui.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/cp4d")

@app.route('/backup')
def hello2():
    return redirect("https://pxbackup.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/")

@app.route('/iks')
def hello3():
    return redirect("https://iks-ocp.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/iks")

@app.route('/ocp')
def hello1():
    return redirect("https://iks-ocp.9sxuen7c9q9.us-south.codeengine.appdomain.cloud/ocp")

if __name__ == "__main__":
    app.run(host="0.0.0.0")
