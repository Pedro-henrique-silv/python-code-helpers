import pandas as pd

# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('./GOOG.csv')

# We print some information about Google_stock
print('Google_stock is of type:', type(Google_stock))
print('Google_stock has shape:', Google_stock.shape)

#show some of the data
Google_stock.head()
Google_stock.tail()

# We get descriptive statistics on our stock data
Google_stock.describe()

# We load fake Company data in a DataFrame
data = pd.read_csv('./fake_company.csv')

# We display the total amount of money spent in salaries each year
data.groupby(['Year'])['Salary'].sum()

# We display the average salary per year
data.groupby(['Year'])['Salary'].mean()

# We display the salary distribution per department per year.
data.groupby(['Year', 'Department'])['Salary'].sum()
