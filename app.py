from flask import Flask,render_template,request
import requests,json,urllib
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/', methods=['POST','GET'])
def predict():

    feat = [float(x) for x in request.form.values()]
    test = json.dumps({"data": feat})
    headers = {'Content-Type': 'application/json'}
    service = 'http://6f3f9952-eb52-420a-af8c-4cf105fedd42.centralus.azurecontainer.io/score'
    resp = requests.post(service, test, headers=headers)
    m = resp.json()[0]
    print(m)
    # flash(m)
    if (m>0):
        resu = "Flight is delayed"
    else:
        resu = "Flight is not delayed"
    return render_template('index.html', result = resu)




