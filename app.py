from flask import Flask, render_template

app = Flask(__name__)
#tasks = ("check email", "do laundry", "call bernie")

@app.route("/new/")
def new():
    return render_template('new.html') 

@app.route("/")
def tasks( tasks = ("check email", "do laundry", "call bernie") ):
    return render_template('tasks.html', tasks=tasks)