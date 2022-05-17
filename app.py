from flask import Flask,render_template,request
import requests 
app = Flask(__name__)
# Api
api_key = "api_key"
url = "http://data.fixer.io/api/latest?access_key=" + api_key


# Route
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
       firstCurrency = request.form.get("firstCurrency") # USD
       secondCurrency = request.form.get("secondCurrency")# EURO
       amount = request.form.get("amount") # 15
       response = requests.get(url).json()
       firstValue = response["rates"][firstCurrency]
       secondValue = response["rates"][secondCurrency] 
       result = (secondValue / firstValue) * float(amount)
       currencyInfo = dict()
       currencyInfo["firstCurrency"] = firstCurrency
       currencyInfo["secondCurrency"] = secondCurrency
       currencyInfo["amount"] = amount
       currencyInfo["result"] = result
       return render_template("index.html",info = currencyInfo)
    else: 
        return render_template("index.html",info = dict())

if __name__ == "__main__":
    app.run(debug=True)