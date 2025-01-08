# -*- coding: utf-8 -*-
"""Learner_Notebook_Full_Code.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-i1nAwi6BlEgjOltHRHmxd9NwIJ30Ton

# Project Python Foundations: FoodHub Data Analysis

### Context

The number of restaurants in New York is increasing day by day. Lots of students and busy professionals rely on those restaurants due to their hectic lifestyles. Online food delivery service is a great option for them. It provides them with good food from their favorite restaurants. A food aggregator company FoodHub offers access to multiple restaurants through a single smartphone app.

The app allows the restaurants to receive a direct online order from a customer. The app assigns a delivery person from the company to pick up the order after it is confirmed by the restaurant. The delivery person then uses the map to reach the restaurant and waits for the food package. Once the food package is handed over to the delivery person, he/she confirms the pick-up in the app and travels to the customer's location to deliver the food. The delivery person confirms the drop-off in the app after delivering the food package to the customer. The customer can rate the order in the app. The food aggregator earns money by collecting a fixed margin of the delivery order from the restaurants.

### Objective

The food aggregator company has stored the data of the different orders made by the registered customers in their online portal. They want to analyze the data to get a fair idea about the demand of different restaurants which will help them in enhancing their customer experience. Suppose you are hired as a Data Scientist in this company and the Data Science team has shared some of the key questions that need to be answered. Perform the data analysis to find answers to these questions that will help the company to improve the business.

### Data Description

The data contains the different data related to a food order. The detailed data dictionary is given below.

### Data Dictionary

* order_id: Unique ID of the order
* customer_id: ID of the customer who ordered the food
* restaurant_name: Name of the restaurant
* cuisine_type: Cuisine ordered by the customer
* cost_of_the_order: Cost of the order
* day_of_the_week: Indicates whether the order is placed on a weekday or weekend (The weekday is from Monday to Friday and the weekend is Saturday and Sunday)
* rating: Rating given by the customer out of 5
* food_preparation_time: Time (in minutes) taken by the restaurant to prepare the food. This is calculated by taking the difference between the timestamps of the restaurant's order confirmation and the delivery person's pick-up confirmation.
* delivery_time: Time (in minutes) taken by the delivery person to deliver the food package. This is calculated by taking the difference between the timestamps of the delivery person's pick-up confirmation and drop-off information

### Let us start by importing the required libraries
"""

# Installing the libraries with the specified version.
!pip install numpy==1.25.2 pandas==1.5.3 matplotlib==3.7.1 seaborn==0.13.1 -q --user

"""**Note**: *After running the above cell, kindly restart the notebook kernel and run all cells sequentially from the start again.*"""

# import libraries for data manipulation
import numpy as np
import pandas as pd

# import libraries for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
import os

"""### Understanding the structure of the data"""

# uncomment and run the following lines for Google Colab
from google.colab import drive
drive.mount('/content/drive/')

# Define the path to the CSV file
foodhub_orders = '/content/drive/MyDrive/foodhub_order.csv'

data = pd.read_csv(foodhub_orders)
print(f"Imported data from {foodhub_orders}")

# Print the DataFrame
print(data)

"""### **Question 1:** How many rows and columns are present in the data? [0.5 mark]"""

print(data.shape)
# Two methods to get the rows and columns
rows, columns = data.shape  # Using the shape attribute to get the dimensions of the DataFrame
print(f'The dataset contains {rows} rows and {columns} columns.')  # Printing the result

"""#### Observations:
# The dataset contains 1898 rows and 9 columns.

### **Question 2:** What are the datatypes of the different columns in the dataset? (The info() function can be used) [0.5 mark]
"""

print(data.info())  # The info() method provides a concise summary of the DataFrame, including data types and non-null counts

"""#### Observations:
# Observation:

# The columns have the following data types:
# - order_id: int64
# - customer_id: int64
# - restaurant_name: object
# - cuisine_type: object
# - cost_of_the_order: float64
# - day_of_the_week: object
# - rating: float64
# - food_preparation_time: int64

### **Question 3:** Are there any missing values in the data? If yes, treat them using an appropriate method. [1 mark]
"""

missing_values = data.isnull().sum()  # The isnull() method detects missing values, and sum() counts them
print(missing_values)  # Printing the count of missing values for each column

# Handling missing values by filling with the mean value for numeric columns
# Using numeric_only=True to calculate the mean only for numeric columns
data.fillna(data.mean(numeric_only=True), inplace=True)  # The fillna() method replaces missing values with the specified value; inplace=True modifies the DataFrame in place

"""#### Observations:
# Doesn't seem to be missing values

### **Question 4:** Check the statistical summary of the data. What is the minimum, average, and maximum time it takes for food to be prepared once an order is placed? [2 marks]
"""

print(data.describe())
# Method one is above and gives all the necessary info in a concise method. The below shows the values manually.

prep_time_summary = data['food_preparation_time'].describe()  # The describe() method provides summary statistics for a column
print(prep_time_summary)  # Printing the summary statistics

# Getting the minimum, average, and maximum food preparation time
min_time = data['food_preparation_time'].min()  # The min() method returns the minimum value
avg_time = data['food_preparation_time'].mean()  # The mean() method returns the average value
max_time = data['food_preparation_time'].max()  # The max() method returns the maximum value
print(f'Minimum: {min_time}, Average: {avg_time}, Maximum: {max_time}')  # Printing the results

"""#### Observations:
# Minimum prep time was around 20
# Max was 35
# Average was around 27.37

### **Question 5:** How many orders are not rated? [1 mark]
"""

# Q5: Counting the number of orders that are not rated
unrated_orders = data[data['rating'].isnull()].shape[0]  # Filtering rows where 'rating' is null and counting them using shape[0]
print(f'Number of unrated orders: {unrated_orders}')  # Printing the count of unrated orders

"""#### Observations:

### Exploratory Data Analysis (EDA)

### Univariate Analysis

### **Question 6:** Explore all the variables and provide observations on their distributions. (Generally, histograms, boxplots, countplots, etc. are used for univariate exploration.) [9 marks]
"""

# Set up the plotting environment
sns.set(style="whitegrid")

# Plot histogram for numerical variables
numerical_vars = ['cost_of_the_order', 'rating', 'food_preparation_time', 'delivery_time']
for var in numerical_vars:
    plt.figure(figsize=(10, 6))
    sns.histplot(data[var], bins=20, kde=True)
    plt.title(f'Distribution of {var}')
    plt.xlabel(var)
    plt.ylabel('Frequency')
    plt.show()

# Plot boxplot for numerical variables
for var in numerical_vars:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=data[var])
    plt.title(f'Boxplot of {var}')
    plt.xlabel(var)
    plt.show()

# Plot countplot for categorical variables
categorical_vars = ['restaurant_name', 'cuisine_type', 'day_of_the_week']
for var in categorical_vars:
    plt.figure(figsize=(12, 6))
    sns.countplot(y=data[var], order=data[var].value_counts().index)
    plt.title(f'Countplot of {var}')
    plt.ylabel(var)
    plt.xlabel('Count')
    plt.show()

"""### **Question 7**: Which are the top 5 restaurants in terms of the number of orders received? [1 mark]"""

top_5_restaurants = data['restaurant_name'].value_counts().head(5)  # Counting the occurrences of each 'restaurant_name' and selecting the top 5
print(top_5_restaurants)  # Printing the top 5 restaurants

"""#### Observations:
# restaurant_name
# Shake Shack                  219
# The Meatball Shop            132
# Blue Ribbon Sushi            119
# Blue Ribbon Fried Chicken     96
# Parm                          68
# Name: count, dtype: int64

### **Question 8**: Which is the most popular cuisine on weekends? [1 mark]
"""

# Filtering the data for weekdays
# The isin() method checks if each element in the 'day_of_the_week' column is in the list of weekdays
weekday_data = data[data['day_of_the_week'].isin(['Weekday'])]

# Filtering the data for weekends
# The isin() method checks if each element in the 'day_of_the_week' column is in the list of weekends
weekend_data = data[data['day_of_the_week'].isin(['Weekend'])]


# Check if weekend_data is empty before calculating mode
if weekend_data.empty:
    print("No orders found for weekends.")
    popular_cuisine_weekend = None  # Or assign a default value
else:
    popular_cuisine_weekend = weekend_data['cuisine_type'].mode()[0]  # Finding the most frequent 'cuisine_type' using mode()
    print(f'Most popular cuisine on weekends: {popular_cuisine_weekend}')  # Printing the most popular cuisine type on weekends

# Check if weekday_data is empty before calculating mode
if weekday_data.empty:
    print("No orders found for weekdays.")
    popular_cuisine_weekday = None  # Or assign a default value
else:
    popular_cuisine_weekday = weekday_data['cuisine_type'].mode()[0]  # Finding the most frequent 'cuisine_type' using mode()
    print(f'Most popular cuisine on weekdays: {popular_cuisine_weekday}')  # Printing the most popular cuisine type on weekdays

"""#### Observations:
# Most popular Cusisine for both weekdays and weekends were both American

### **Question 9**: What percentage of the orders cost more than 20 dollars? [2 marks]
"""

expensive_orders = data[data['cost_of_the_order'] > 20].shape[0]  # Counting the number of orders with 'cost_of_the_order' greater than 20
percentage_expensive_orders = (expensive_orders / data.shape[0]) * 100  # Calculating the percentage of such orders
print(f'Percentage of orders costing more than 20 dollars: {percentage_expensive_orders:.2f}%')  # Printing the percentage

"""#### Observations:
# Percentage of order costing more than 20 was around 29.24% of the orders

### **Question 10**: What is the mean order delivery time? [1 mark]
"""

mean_delivery_time = data['delivery_time'].mean()  # Using the mean() method to find the average delivery time
print(f'Mean order delivery time: {mean_delivery_time:.2f} minutes')  # Printing the mean delivery time

"""#### Observations:
# Mean order delivery time was 24.16 mins

### **Question 11:** The company has decided to give 20% discount vouchers to the top 3 most frequent customers. Find the IDs of these customers and the number of orders they placed. [1 mark]
"""

top_3_customers = data['customer_id'].value_counts().head(3)  # Counting the occurrences of each 'customer_id' and selecting the top 3
print(top_3_customers)  # Printing the IDs of the top 3 most frequent customers and their order counts

"""#### Observations:
# Top 3 customers was
# 52832    Order x 13
# 47440    Order x 10
# 83287     Order x 9

### Multivariate Analysis

### **Question 12**: Perform a multivariate analysis to explore relationships between the important variables in the dataset. (It is a good idea to explore relations between numerical variables as well as relations between numerical and categorical variables) [10 marks]
"""

plt.figure(figsize=(10, 6))  # Creating a new figure with specified size
sns.scatterplot(x='cost_of_the_order', y='rating', data=data)  # Creating a scatter plot with 'cost_of_the_order' on the x-axis and 'rating' on the y-axis
plt.title('Cost of the Order vs Rating')  # Setting the title of the plot
plt.xlabel('Cost of the Order')  # Setting the label for the x-axis
plt.ylabel('Rating')  # Setting the label for the y-axis
plt.show()  # Displaying the plot

"""### **Question 13:** The company wants to provide a promotional offer in the advertisement of the restaurants. The condition to get the offer is that the restaurants must have a rating count of more than 50 and the average rating should be greater than 4. Find the restaurants fulfilling the criteria to get the promotional offer. [3 marks]"""

# Convert 'rating' column to numeric, handling errors
data['rating'] = pd.to_numeric(data['rating'], errors='coerce')

# Group by restaurant name and calculate the count and mean of ratings
restaurant_ratings = data.groupby('restaurant_name').agg({'rating': ['count', 'mean']})

# Filter the restaurants based on the criteria
promotional_restaurants = restaurant_ratings[(restaurant_ratings[('rating', 'count')] > 50) & (restaurant_ratings[('rating', 'mean')] > 4)]

# Rename columns for better readability
promotional_restaurants.columns = ['rating_count', 'average_rating']

# Display the qualifying restaurants
print(promotional_restaurants)

"""#### Observations:
# Blue Ribbon Fried Chicken            64        4.328125
# Blue Ribbon Sushi                    73        4.219178
# Shake Shack                         133        4.278195
# The Meatball Shop                    84        4.511905

### **Question 14:** The company charges the restaurant 25% on the orders having cost greater than 20 dollars and 15% on the orders having cost greater than 5 dollars. Find the net revenue generated by the company across all orders. [3 marks]
"""

# Applying a lambda function to calculate revenue based on order cost
data['revenue'] = data['cost_of_the_order'].apply(lambda x: x * 0.25 if x > 20 else (x * 0.15 if x > 5 else 0))
total_revenue = data['revenue'].sum()  # Summing up the revenue column to get the total revenue
print(f'Total revenue generated: {total_revenue}')  # Printing the total revenue generated

"""#### Observations:
# Total revenue generated: 6166.303

### **Question 15:** The company wants to analyze the total time required to deliver the food. What percentage of orders take more than 60 minutes to get delivered from the time the order is placed? (The food has to be prepared and then delivered.) [2 marks]
"""

# Creating a new column 'total_time' by adding 'food_preparation_time' and 'delivery_time'
data['total_time'] = data['food_preparation_time'] + data['delivery_time']
orders_more_than_60 = data[data['total_time'] > 60].shape[0]  # Counting the number of orders with 'total_time' greater than 60 minutes
percentage_orders_more_than_60 = (orders_more_than_60 / data.shape[0]) * 100  # Calculating the percentage of such orders
print(f'Percentage of orders taking more than 60 minutes: {percentage_orders_more_than_60:.2f}%')  # Printing

"""#### Observations:
# Percentage of orders taking more than 60 minutes: 10.54%

### **Question 16:** The company wants to analyze the delivery time of the orders on weekdays and weekends. How does the mean delivery time vary during weekdays and weekends? [2 marks]
"""

# Filtering the data for weekdays
# The isin() method checks if each element in the 'day_of_the_week' column is in the list of weekdays
weekday_data = data[data['day_of_the_week'].isin(['Weekday'])]

# Filtering the data for weekends
# The isin() method checks if each element in the 'day_of_the_week' column is in the list of weekends
weekend_data = data[data['day_of_the_week'].isin(['Weekend'])]

# Calculating the mean delivery time for weekdays
mean_delivery_time_weekday = weekday_data['delivery_time'].mean()

# Calculating the mean delivery time for weekends
mean_delivery_time_weekend = weekend_data['delivery_time'].mean()

# Printing the mean delivery times for both weekdays and weekends
print(f'Mean delivery time on weekdays: {mean_delivery_time_weekday:.2f} minutes')
print(f'Mean delivery time on weekends: {mean_delivery_time_weekend:.2f} minutes')

"""#### Observations:
# Mean delivery time on weekdays: 28.34 minutes
# Mean delivery time on weekends: 22.47 minutes

### Conclusion and Recommendations

### **Question 17:** What are your conclusions from the analysis? What recommendations would you like to share to help improve the business? (You can use cuisine type and feedback ratings to drive your business recommendations.) [6 marks]

### Conclusions:
General Conclusions:

Order Costs:

The distribution of the cost of orders shows that most orders fall within a specific price range. There might be a few high-cost orders, indicated by the presence of outliers in the boxplot.

Ratings:

The ratings given by customers are generally distributed across the entire scale, but there might be a tendency towards higher ratings if the mean is skewed towards the higher end.

Food Preparation Time:

The distribution of food preparation time might show that most orders are prepared within a reasonable timeframe, but there are some orders that take significantly longer, indicated by the tail in the histogram or outliers in the boxplot.

Delivery Time:

Similar to the food preparation time, the delivery time distribution might show that most deliveries are made within a standard time frame, but there are instances of significantly longer deliveries.

Restaurant Popularity:

The countplot for restaurant names will reveal which restaurants are the most popular based on the number of orders received. The top 5 restaurants can be identified from this plot.

Cuisine Popularity:

The most popular cuisines can be determined by the countplot for cuisine types. This can be further filtered to see which cuisines are most popular on weekends.

Order Frequency by Day:

The countplot for day_of_the_week will show the distribution of orders between weekdays and weekends. This can provide insights into customer behavior and peak ordering times.

Customer Preferences:

By analyzing the top customers and their order frequencies, you can identify loyal customers who might be targeted for promotions or loyalty programs

### Recommendations:

Recommendations for Business Improvement:

Focus on Popular Restaurants and Cuisines:

Enhance partnerships with the most popular restaurants and cuisines to ensure they are well-stocked and can handle high demand.

Improve Delivery Efficiency:

Analyze the delivery times and identify any patterns or factors contributing to delays. Improving logistics can enhance customer satisfaction.

Customer Feedback:

Monitor and address customer ratings and feedback to improve service quality and customer experience.

Promotions for Loyal Customers:

Implement loyalty programs and discounts for the top customers to retain them and encourage frequent orders.

Weekend Promotions:

Since weekends might have a higher order volume, consider offering special promotions or discounts to boost sales further during these peak times.
"""

!jupyter nbconvert --execute --to html "/content/drive/MyDrive/Colab Notebooks/Learner_Notebook_Full_Code.ipynb"

"""---"""