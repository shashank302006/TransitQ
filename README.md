#  TransitQ

TransitQ is a machine learning project, the idea was to explore how historical public transport data can be used to predict bus requirements for different routes and time periods.

##  What it does

TransitQ takes information such as the route, stop, time, day, distance and travel time and uses a trained **Random Forest Regressor** to estimate the number of buses required.

The trained model is connected to a **FastAPI backend**, so predictions can be made through REST API endpoints.

##  Tech Stack

- Python
- Pandas
- Scikit-learn
- Random Forest Regressor
- FastAPI
- Jupyter Notebook
- Joblib

##  How it works

Data → Preprocessing → Random Forest Model → Prediction → FastAPI

The model was trained using transport data containing information about routes, stops, passenger demand, travel times and bus allocation.

##  Project Structure

- `backend/` — FastAPI backend
- `notebooks/` — ML development and experimentation
- `data/` — Transport dataset
- `models/` — Trained ML model
- `DATA_C/` — Data generation/processing scripts

##  Frontend

There is currently **no frontend** for TransitQ. This version of the project focuses on the machine learning pipeline and backend API. The API can be tested using FastAPI's interactive Swagger documentation at `/docs`.

##  Future Improvements

I plan to improve TransitQ by integrating real-world transport data, improving the prediction pipeline and eventually building a frontend to make the system easier to use.

---

Built as a learning project to understand how an ML model can go from a Jupyter Notebook to a working backend API.
