from flask import Flask,render_template,request,jsonify
import pickle

app=Flask(__name__)

model=pickle.load(open('model/spam_model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    data=request.get_json()
    message=data['message']
    prediction=model.predict([message])[0]
    return jsonify({"prediction": int(prediction)})

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)