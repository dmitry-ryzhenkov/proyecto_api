import datetime
import pickle

from fastapi import APIRouter

from .models import Prediction, IrisFeatures

router = APIRouter(
    prefix="/ml",
    tags=["Machine Learning"]
)

with open("assets/model.pkl", "br") as file:
    model = pickle.load(file)

@router.post("/predict")
def predict(body: IrisFeatures) -> Prediction:
    data = [[body.sepal_length, body.sepal_width, body.petal_length, body.petal_width]]

    prediction = model.predict(data)

    return Prediction(
        value=prediction[0],
        dt = datetime.datetime.now()
    )