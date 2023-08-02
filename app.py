from flask import Flask, request, jsonify
import Gui

app = Flask(__name__)

#API Post Request for Spam Classification
@app.route('/classification', methods=['POST'])
def spam_classification():
    #Storing email text
    text = request.json['text'].lower().split()
    
    #Storing model, list of columns and appropriate array used for model prediction
    g1 = Gui.App()
    model = g1.get_model()
    col_list = g1.get_columns()
    df = g1.prepare_df(col_list, text)

    #Classifying email
    if model.predict([df])[0] == 1:
        result = "SPAM"
    else:
        result = "Not Spam"
               
    response = jsonify({
        'classification': result
    })

    return response, 200


if __name__ == '__main__':
    app.run()