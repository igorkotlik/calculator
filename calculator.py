from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["get", "POST"])

def index():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["operation"]
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = substract(a,b)
            else:
                result = "Unknown operation"
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

def add(a, b):
    return a + b

def substract(a, b):
    return a - b

if __name__ == "__main__":
    app.run(host="0.0.0.0")
