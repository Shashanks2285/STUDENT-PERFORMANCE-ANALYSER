# from flask import Flask,request,render_template
# import numpy as np
# import pandas as pd

# from sklearn.preprocessing import StandardScaler
# from src.pipeline.predict_pipeline import CustomData,PredictPipeline

# application=Flask(__name__)

# app=application

# ## Route for a home page

# @app.route('/')
# def index():
#     return render_template('index.html') 

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_datapoint():
#     if request.method=='GET':
#         return render_template('home.html')
#     else:
#         data=CustomData(
#             gender=request.form.get('gender'),
#             race_ethnicity=request.form.get('ethnicity'),
#             parental_level_of_education=request.form.get('parental_level_of_education'),
#             lunch=request.form.get('lunch'),
#             test_preparation_course=request.form.get('test_preparation_course'),
#             reading_score=float(request.form.get('writing_score')),
#             writing_score=float(request.form.get('reading_score'))

#         )
#         pred_df=data.get_data_as_data_frame()
#         print(pred_df)
#         print("Before Prediction")

#         predict_pipeline=PredictPipeline()
#         print("Mid Prediction")
#         results=predict_pipeline.predict(pred_df)
#         print("after Prediction")
#         return render_template('home.html',results=results[0])
    

# if __name__=="__main__":
#     app.run(host="0.0.0.0")   
# 
     
from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
from flask_cors import CORS
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

# Initialize Flask app
app = Flask(__name__)
CORS(app)
# Route for home page (renders index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for web form-based prediction (renders home.html)
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)
            return render_template('home.html', results=results[0])
        except Exception as e:
            return render_template('home.html', results=f"Error: {str(e)}")


@app.route('/status', methods=['GET'])
def status():
    return ({"status": "Server is running"}), 200

# ✅ Route for API-based prediction (JSON input)
@app.route('/api', methods=['POST'])
def api_predict():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid or missing JSON in request'}), 400
        
        custom_data = CustomData(
            gender=data['gender'],
            race_ethnicity=data['ethnicity'],
            parental_level_of_education=data['parental_level_of_education'],
            lunch=data['lunch'],
            test_preparation_course=data['test_preparation_course'],
            reading_score=float(data['reading_score']),
            writing_score=float(data['writing_score'])
        )

        pred_df = custom_data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return jsonify({'prediction': results[0]}) , 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ✅ Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
