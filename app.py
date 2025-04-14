from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    totalcost = None
    if request.method == "POST":
        try:
            materialcost = float(request.form["materialcost"])
            matpercent1 = float(request.form["matpercent1"])
            jhourly = float(request.form["jhourly"])
            jpd = float(request.form["jpd"])
            Jhours = float(request.form["Jhours"])
            Jdays = float(request.form["Jdays"])
            Whours = float(request.form["Whours"])
            wpd = float(request.form["wpd"])

            matpercent2 = matpercent1 / 100
            Jhours2 = Jhours - Jdays
            matcostfinal = materialcost * (1 + matpercent2)

            totalcost = (Jhours2 * jhourly) + (Jdays * (jhourly + jpd)) + (Whours * 35) + matcostfinal + wpd
        except:
            totalcost = "Invalid input. Please enter valid numbers."

    return render_template("calculator.html", totalcost=totalcost)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

