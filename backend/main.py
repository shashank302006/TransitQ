from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib

app = FastAPI(title="TransitQ API")

model = joblib.load("../models/transitq_model.pkl")


class PredictionRequest(BaseModel):
    route_id: str
    stop_id: str
    hour: int
    day_of_week: int
    is_weekend: int
    is_holiday: int
    distance_km: float
    travel_time_min: float


@app.get("/")
def home():
    return {
        "message": "TransitQ API is running"
    }


@app.post("/predict")
def predict(request: PredictionRequest):

    peak_hour = int(
        (7 <= request.hour <= 9) or
        (17 <= request.hour <= 20)
    )

    input_data = pd.DataFrame([{
        "route_id": request.route_id,
        "stop_id": request.stop_id,
        "hour": request.hour,
        "day_of_week": request.day_of_week,
        "is_weekend": request.is_weekend,
        "is_holiday": request.is_holiday,
        "peak_hour": peak_hour,
        "distance_km": request.distance_km,
        "travel_time_min": request.travel_time_min
    }])

    predicted_demand = model.predict(input_data)[0]

    predicted_demand = max(
        0,
        round(predicted_demand)
    )

    bus_capacity = 40

    required_buses = int(
        np.ceil(predicted_demand / bus_capacity)
    )

    return {
        "predicted_demand": predicted_demand,
        "required_buses": required_buses,
        "bus_capacity": bus_capacity
    }
