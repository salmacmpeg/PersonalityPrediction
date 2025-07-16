import pandas as pd
from pipeline.model_inference_pipeline import model_inference_service


def main():
    mis = model_inference_service()

    test = {'Time_spent_Alone': [5],
            'Stage_fear': [0],
            'Social_event_attendance': [1],
            'Going_outside': [3],
            'Drained_after_socializing': [1],
            'Friends_circle_size': [2],
            'Post_frequency': [1]}
    print("testing data ", test)
    pred = mis.predict(pd.DataFrame(test))

    print('Predicted personality is ',
          'Introverted' if pred == 1 else 'Extroverted')


if __name__ == '__main__':
    main()
