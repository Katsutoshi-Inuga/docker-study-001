from flask import Flask,render_template,request

app = Flask(__name__)

def calc_tax(v,rate):
    try:
        rs = str(int(float(v)*(1 + rate)))
    except:
        print('calc error')
        rs = "計算できませんでした。"
    return rs

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health-check", methods=["GET"])
def health_check():
    return "ok"

@app.route("/std", methods=["POST"])
def stdtaxinc():
    print(request.get_data())
    return calc_tax(request.get_data(), 0.1)

@app.route("/red", methods=["POST"])
def reducedtaxinc():
    print(request.get_data())
    return calc_tax(request.get_data(), 0.08)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

