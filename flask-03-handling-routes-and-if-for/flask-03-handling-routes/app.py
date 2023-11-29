from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return "No Path, <h1> Welcome Home</h1>" 

@app.route("/error")
def error():
    return "<h1>There is an ERROR !</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("error"))

# @app.route('/<name1>')
# def greet_template(name1):
#     return render_template('greet.html', name=name1)

@app.route("/<name2>")
def greet(name2):
    greet_format=f"""
<!DOCTYPE html>
<html>
<head>
    <title>Greeting Page</title>
</head>
<body>
    <h1>Hello, { name2 }!<h1>
    <h1>Welcome to HTML Page</h1>
</body>
</html>
    """
    return greet_format

@app.route("/greet-admin")
def greet_admin():
    return redirect(url_for("greet", name2="Admin!"))

@app.route("/list10")
def list10():
    return render_template("list10.html")

@app.route("/evens")
def evens():
    return render_template("evens.html")

if __name__== "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8081)