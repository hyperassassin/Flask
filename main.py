from flask import Flask , render_template , send_from_directory
import os

from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/')

def file_default():
    try:
        with open('file1.txt','r',encoding="utf-8",errors="ignore") as f:
            return render_template('content.html',text = f.read())
    except FileNotFoundError:
        return render_template("Error.html")

@app.route('/<name>')

def content(name):
    try:
        if name == "file4.txt":
            with open("file4.txt",'r',encoding="utf-16le",errors="ignore") as f:
                return render_template('content.html',text = f.read())
        else:
            with open(name,'r',encoding="utf-8",errors="ignore") as f:
                return render_template('content.html',text = f.read())
    except FileNotFoundError:
        return render_template("Error.html")

@app.route('/<name>/start=<int:a>&end=<int:b>')

def filter(a,b,name):
    try:
        if name == "file4.txt":
            with open("file4.txt",encoding="utf-16le",errors="ignore") as f:
                file = f.readlines()
                con = file[a:b+1]
                str1 = " "
                ltext = str1.join(con)
                return render_template('content.html',text = ltext)
        else:
            with open(name,encoding="utf-8",errors="ignore") as f:
                file = f.readlines()
                con = file[a:b+1]
                str1 = " "
                ltext = str1.join(con)
                return render_template('content.html',text = ltext)
    except FileNotFoundError:
        return render_template("Error.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("Error.html")

@app.errorhandler(500)
def internal_err(error):
    return render_template("Error.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/icon.ico')

app.run()