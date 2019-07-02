from flask import Flask
from SER import Predict
import keras
from flask import Flask, jsonify, abort, request, make_response, url_for,redirect, render_template
app = Flask(__name__)
import os
from werkzeug.utils import secure_filename
from Utils import load_model, Radar
UPLOAD_FOLDER = os.path.dirname(os.path.realpath(__file__)) + '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/predict',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST' or request.method == 'GET':
        print(request.method)
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return

        file = request.files['file']
        print(file.filename)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:  # and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            inputloc = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            model = load_model(load_model_name="LSTM_LIBROSA", model_name="lstm")
            emotion,prob=Predict(model, model_name = "lstm", file_path = inputloc, feature_method = 'l')
            keras.backend.clear_session()
            result={"emotion":emotion,
                    "prob":{
                        "angry":prob[0].tolist(),
                        "fear":prob[1].tolist(),
                        "happy":prob[2].tolist(),
                        "neutral":prob[3].tolist(),
                        "sad":prob[4].tolist(),
                        "surprise":prob[5].tolist()
                    }
                    }
            return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
