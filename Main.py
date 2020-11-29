import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

#load data
df = pd.read_csv(r"US_Accidents_June20.tar\US_Accidents_June20.csv", usecols=["Weather_Condition", "Sunrise_Sunset", "Zipcode"])

#look at the data
print(df.head())
print()
print(df.shape)
print()

#clean data
print(df.isnull().values.any())
print(df.isnull().sum().sum())
df = df.dropna()
print(df.isnull().values.any())
print()

#look at the cleaned data
print(df.head())
print()
print(df.shape)

print(2*'\n')

#show list of all weather conditions
print(df['Weather_Condition'].unique())

print()

#prepare data
weatherdf = df
weatherdf['Clear_Weather'] = df.Weather_Condition == 'Clear'
del weatherdf['Weather_Condition']
del weatherdf['Zipcode']

#look at the data
print(weatherdf.head())
print()

#look at the frequency of clear weather
print(df['Clear_Weather'].unique())
print(df['Clear_Weather'].value_counts())

print()

#look at the frequency of accidents during day vs night (measured by after sunrise or after sunset)
print(df['Sunrise_Sunset'].unique())
print(df['Sunrise_Sunset'].value_counts())

print(2*'\n')

#Two-Way Frequency Table
print(pd.crosstab(weatherdf.Clear_Weather, weatherdf.Sunrise_Sunset, margins=True, margins_name="Total"))

#freq-bar chart
total = 3437488
NotClearWeatherAtDay = (1966561 / total) * 100
NotClearWeatherAtNight = (662750 / total) * 100
ClearWeatherAtDay = (572087 / total) * 100
ClearWeatherAtNight = (236090 / total) * 100
data_dict = {'Not Clear & Day': NotClearWeatherAtDay, 'Not Clear & Night': NotClearWeatherAtNight, 'Clear & Day': ClearWeatherAtDay, 'Clear & Night': ClearWeatherAtNight}
names = list(data_dict.keys())
values = list(data_dict.values())
#fig, axs = plt.subplots(1, 3, figsize=(9,3), sharey=True)
#axs[0]
plt.bar(names, values)
plt.show()

#weather pie chart
clearweathernumber = 808177
notclearnumber = 2629311
cwratio = clearweathernumber / total
ncwratio = notclearnumber / total
labels = 'Clear Weather', 'Not Clear Weather'
sizes = [cwratio, ncwratio]
explode = (0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
plt.show()

#day      #night
#2538648  898840

#day night pie chart
daynumber = 2538648
nightnumber = 898840
dayratio = daynumber / total
nightratio = nightnumber / total
labels = 'Night', 'Day'
sizes = [nightratio, dayratio]
explode = (0, 0)
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=90)
ax1.axis('equal')
plt.show()

#car accidents by population by zip code table
df = pd.read_csv(r"accidentsbypopulation.csv")
print(df.head())

print(7*'\n')
#correlation between population and total car accidents
print("Correlation between population and total car accidents for a zip code")
print()
print("Pearson's r")
print(scipy.stats.pearsonr(df["Population"], df["Accidents"]))    # Pearson's r

print()
print("Spearman's rho")
print(scipy.stats.spearmanr(df["Population"], df["Accidents"]))   # Spearman's rho

print()
print("Kendall's tau")
print(scipy.stats.kendalltau(df["Population"], df["Accidents"]))  # Kendall's tau

# 2-way scatter plot! xaxis = population; yaxis=total car accidents
plt.scatter(df["Population"], df["Accidents"], s=0.2, c='C9')
plt.xlabel("Population")
plt.ylabel("Car Accidents")
plt.show()

# 2-way scatter plot with a regression line fitted over items
predict = "Accidents"
X = df[["Population"]]
y = df[predict]
linear = LinearRegression()
linear.fit(X, y)
predictions = linear.predict(X)
fig, ax = plt.subplots()
ax.plot(df["Population"], predictions, c="#ff7f0e")
ax.scatter(df["Population"], df["Accidents"], s=0.2, c='C9')
ax.set_xlabel('Population')
ax.set_ylabel('Car Accidents')
plt.show()

print(7*'\n')
# regression table for above scatter plot regression line
# note: I decided to do the regression table in r because it looks nicer, but i kept the code
import statsmodels.api as sm
X = df["Population"]
X = sm.add_constant(X, prepend=False)
mod = sm.OLS(y, X)
res = mod.fit()
print(res.summary())