from flask import Flask,render_template,jsonify

app = Flask(__name__)

def calculo():
    return 3+5

@app.route("/")
def read_root():
    return render_template('index.html')

@app.get("/ejemplo")
def health():
    return render_template('ejemplo.html',RESULTADO=calculo())

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port=5000)