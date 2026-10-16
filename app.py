from flask import Flask, abort, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/puerta1")
def puerta1():
    return render_template("puerta1.html")


@app.route("/puerta2")
def puerta2():
    return render_template("puerta2.html")


@app.route("/puerta3")
def puerta3():
    return render_template("puerta3.html")


@app.route("/puerta4")
def puerta4():
    return render_template("puerta4.html")


@app.route("/puerta5")
def puerta5():
    return render_template("puerta5.html")


@app.route("/styles/<filename>")
def door_stylesheet(filename):
    if filename not in {f"puerta{number}.css" for number in range(1, 6)}:
        abort(404)
    return send_from_directory(app.template_folder, filename)
