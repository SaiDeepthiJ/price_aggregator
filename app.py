from flask import Flask, request, render_template
from mock_data import get_mock_prices

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form["product"]
        results = get_mock_prices(query)
        return render_template("results.html", product=query, results=results)
    return render_template("base.html")
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
