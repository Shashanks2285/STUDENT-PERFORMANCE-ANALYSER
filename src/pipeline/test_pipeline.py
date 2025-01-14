import os
from predict_pipeline import CustomData, PredictPipeline

def test_predict_pipeline():
    try:
        

        # Step 1: Create an instance of CustomData with sample input values
        data = CustomData(
            gender='male',
            race_ethnicity='group A',
            parental_level_of_education="bachelor's degree",
            lunch='standard',
            test_preparation_course='none',
            reading_score=75,
            writing_score=80
        )

        # Step 2: Convert the input data to a DataFrame
        features = data.get_data_as_data_frame()

        # Step 3: Create an instance of PredictPipeline
        pipeline = PredictPipeline()

        # Step 4: Make predictions
        predictions = pipeline.predict(features)

        # Step 5: Print the predictions
        print("Predictions:", predictions)

    except Exception as e:
        print("Error during testing:", str(e))

# Run the test
if __name__ == "__main__":
    test_predict_pipeline()
