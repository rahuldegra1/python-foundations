import pandas as pd
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt

# Fetch the dataset and load it as a Pandas DataFrame
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Plot Latitude vs Longitude to see if geography impacts price
plt.scatter(
    df['Longitude'], 
    df['Latitude'], 
    c=df['MedHouseVal'], # Color the dots by house value
    cmap='jet',          # Blue is cheap, Red is expensive
    alpha=0.4
)

plt.colorbar(label='Median House Value ($100,000s)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('California Housing Prices')

from sklearn.model_selection import train_test_split

x = df.drop("MedHouseVal", axis = 1) # x axis is everything except price of house
y = df["MedHouseVal"]  #y is only the price

# split the data: 80% for train, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print(f"Training on {len(X_train)} houses...")
print(f"Holding back {len(X_test)} houses for testing...")

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# initalize the algorithm
model = LinearRegression()

print("Training the AI model...")
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {round(mse, 3)}")