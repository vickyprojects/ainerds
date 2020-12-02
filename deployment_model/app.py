import flask
from flask import request , render_template
import joblib

app=flask.Flask(__name__)
app.config["DEBUG"] = True

#from flask_cors import CORS
#CORS(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/',methods={'POST'})
def getvalue():
    name= request.form['gender']
    religion= request.form['religion']
    mother_tongue= request.form['mother_tongue']
    country= request.form['country']
    height= request.form['height']
    model = joblib.load('Marriage_age_model.ml')
    age_predict = model.predict([[name,religion,mother_tongue,country,height]])
    age=str(age_predict)
    return render_template('index.html',Age=age)


#@app.route('/predict')
#def predict():
#    model = joblib.load('Marriage_age_model.ml')
#    age_predict = model.predict([[name,religion,mother_tongue,country,height]])
#    return str(age_predict)

app.run(debug=True)