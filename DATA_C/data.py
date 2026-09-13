from datetime import datetime, timedelta
import numpy as np
import pandas as pd

np.random.seed(42)


routes = {
    "R101": 1.30,
    "R102": 1.00,
    "R103": 0.65,
    "R201": 1.20,
    "R202": 0.85,
    "R301": 1.10,
    "R302": 0.70,
    "R401": 0.90,
}

stops = {
    "S01": "Central Station",
    "S02": "City Mall",  
    "S03": "University",
    "S04": "Market",
    "S05": "Bus Terminal",
    "S06": "Industrial Area",
}

stop_factors = {
    "S01": 1.4,
    "S02": 1.2,
    "S03": 1.3,
    "S04": 1.0,
    "S05": 1.5,
    "S06": 0.8,
}

bus_capacity = 40

start_date = datetime(2025, 8, 1)
end_date = datetime(2026, 7, 31)

rows = []
current_date = start_date



while current_date <= end_date:
    day_of_week = current_date.weekday()


    is_weekend = int(day_of_week >= 5)

 
    is_holiday = int(np.random.random() < 0.03)

    for route_id, route_factor in routes.items():
        for stop_id, stop_name in stops.items():
            for hour in range(6, 23):

                demand = 20.0


                if 7 <= hour <= 9:
                    demand += 70  
                elif 17 <= hour <= 20:
                    demand += 80  
                elif 11 <= hour <= 15:
                    demand += 30  
                elif hour >= 21:
                    demand -= 10 


                if is_weekend:
                    demand *= 0.65
                if is_holiday:
                    demand *= 0.55

                demand *= route_factor
                demand *= stop_factors[stop_id]


                demand += np.random.normal(0, 10)
                passenger_count = max(5, int(round(demand)))


                ideal_buses = int(np.ceil(passenger_count / bus_capacity))
                allocation_variation = np.random.choice([-1, 0, 0, 0, 1])
                buses_allocated = max(1, ideal_buses + allocation_variation)


                distance_km = round(np.random.uniform(2, 15), 2)
                travel_time = int(distance_km * np.random.uniform(2.5, 4))
                peak_hour = int(7 <= hour <= 9 or 17 <= hour <= 20)

                rows.append({
                    "date": current_date.strftime("%Y-%m-%d"),
                    "route_id": route_id,
                    "stop_id": stop_id,
                    "stop_name": stop_name,
                    "hour": hour,
                    "day_of_week": day_of_week,
                    "is_weekend": is_weekend,
                    "is_holiday": is_holiday,
                    "peak_hour": peak_hour,
                    "passenger_count": passenger_count,
                    "bus_capacity": bus_capacity,
                    "buses_allocated": buses_allocated,
                    "distance_km": distance_km,
                    "travel_time_min": travel_time,
                })

    current_date += timedelta(days=1)


df = pd.DataFrame(rows)


output_filename = "synthetic_transport_data.csv"
df.to_csv(output_filename, index=False)

print(f"Dataset created successfully: {output_filename}")
print("Total Rows:", len(df))
print("\nSample Data:")
print(df.head())