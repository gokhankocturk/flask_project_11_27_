from flask import Flask, render_template, request
app = Flask(__name__)

def lcm(num1,num2):
    common_multiplications = [] 
    for i in range(max(num1, num2),num1*num2+1):
        if i%num1==0 and i%num2==0:
           common_multiplications.append(i) 
    return min(common_multiplications)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calc", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        num1 = request.form.get("number1")
        num2 = request.form.get("number2")
        return render_template("result.html", 
                               result1 = num1, 
                               result2 = num2, 
                               lcm = lcm(int(num1),int(num2)), 
                               developer_name = 'gokhan')
    else:
        return render_template("result.html", 
                               developer_name = "gokhan")

if __name__== "__main__":
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8081)