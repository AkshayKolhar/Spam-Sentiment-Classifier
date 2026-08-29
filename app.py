from flask import Flask,request,jsonify,render_template
from classify import predict_message

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")




@app.route("/predict",methods=["POST"])
def predict():

    data=request.get_json()
    message=data.get("message")

    if not message:  
        return jsonify({
            "error":"Message is required"
        }),400
    result=predict_message(message)

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True)


