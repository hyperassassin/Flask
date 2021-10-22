from flask import Flask , render_template , send_from_directory,request
import os

from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/',defaults={'name':'file1.txt'})
@app.route("/<name>")

def main(name):
    start = request.args.get('start',default=0,type=int)
    end = request.args.get('end',default=":",type=int)
    try:
        if name == "file4.txt":
            if end != ":":
                with open("file4.txt",encoding="utf-16le",errors="ignore") as f:
                    file = f.readlines()
                    con = file[start:end+1]
                    str1 = " "
                    ltext = str1.join(con)
                    return render_template('content.html',text = ltext)
            else:
                with open("file4.txt",encoding="utf-16le",errors="ignore") as f:
                    file = f.readlines()
                    con = file[start:]
                    str1 = " "
                    ltext = str1.join(con)
                    return render_template('content.html',text = ltext)
        else:
            if end != ":":
                with open(name,encoding="utf-8",errors="ignore") as f:
                    file = f.readlines()
                    con = file[start:end+1]
                    str1 = " "
                    ltext = str1.join(con)
                    return render_template('content.html',text = ltext)
            else:
                with open(name,encoding="utf-8",errors="ignore") as f:
                    file = f.readlines()
                    con = file[start:]
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
