# AUTOMOBILE SALES DATA ANALYSIS 
import pandas as pd 
import numpy as np


# LOAD DATA
#---------------------------------------------------
df = pd.read_csv("automobile_sales_dataset.csv")

print("File read successfully")

print("Shape :", df.shape)

print("First 10 rows: ", df.head(10))
#---------------------------------------------------


# DATA EXPLORATION
#---------------------------------------------------
print("data information: \n")
print(df.info())

print("data summary: \n")
print(df.describe())

print("data types: \n")
print(df.dtypes)
#---------------------------------------------------


# DATA CLEANING
#---------------------------------------------------
print("missing values: \n", df.isnull().sum())

df.drop_duplicates(inplace = True)

df['Date'] = pd.to_datetime(df['Date'])
print("New Datatypes: \n")
print(df.dtypes)
#---------------------------------------------------


# CREATE NEW COLUMN
#---------------------------------------------------
df['Year'] = df["Date"].dt.year

#---------------------------------------------------


# KPIs
#---------------------------------------------------------------------------------------------------
total_revenue = df['Revenue'].sum()
print("Total_Revenue: ",total_revenue)

total_units = df['Units_Sold'].sum()
print("total units sold : ", total_units)

avg_satisfaction = df["Customer_Satisfaction_Score"].mean().__round__(2)
print("average customer satisfaction: ", avg_satisfaction)

top_dealers = df.groupby('Dealer')["Revenue"].sum().sort_values(ascending=False).head(5)
print("Top 5 dealers: \n", top_dealers)

top_models = df.groupby('Vehicle_Model')["Revenue"].sum().sort_values(ascending=False).head(10)
print(" Top 10 Vehicle Models: \n",top_models)

region_sales = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print("Sales by Region: \n",region_sales)

yearly_sales = df.groupby("Year")["Revenue"].sum()
print("Sales per year: \n", yearly_sales)

#----------------------------------------------------------------------------------------------------


# DATA VISUALIZATION
#------------------------------------------------------------------------------------------------
image_urls = {
    'SUV': 'https://raw.githubusercontent.com/aniketaditya29/Automobile-Sales-Market-Trend-Analysis-Power-BI-Python-Project/main/stock%20images/SUV%203D.jpg',
    'Sedan': 'https://raw.githubusercontent.com/aniketaditya29/Automobile-Sales-Market-Trend-Analysis-Power-BI-Python-Project/main/stock%20images/SEDAN%203D.jpg',
    'Hatchback': 'https://raw.githubusercontent.com/aniketaditya29/Automobile-Sales-Market-Trend-Analysis-Power-BI-Python-Project/main/stock%20images/HATCHBACK%203D.jpg',
    'Electric': 'https://raw.githubusercontent.com/aniketaditya29/Automobile-Sales-Market-Trend-Analysis-Power-BI-Python-Project/main/stock%20images/EV%203D.jpg'
}
df['Image_URL'] = df['Category'].map(image_urls)
print(df)
#------------------------------------------------------------------------------------------------

df.to_csv("Automobile_Sales_Analysis.csv", index=False)