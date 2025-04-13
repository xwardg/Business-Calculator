from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculator():
    totalcost = None
    if request.method == "POST":
        try:
            materialcost = float(request.form["materialcost"])
            Jhours = float(request.form["Jhours"])
            Jdays = float(request.form["Jdays"])
            Whours = float(request.form["Whours"])

            Jhours2 = (Jhours - Jdays)
            matcostfinal = (materialcost * 1.1)
            totalcost = (Jhours2 * 45) + (Jdays * 65) + (Whours * 35) + matcostfinal
        except:
            totalcost = "Invalid input. Please enter numbers only."

    return render_template("calculator.html", totalcost=totalcost)

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

