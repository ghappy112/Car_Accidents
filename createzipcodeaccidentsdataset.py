import pandas as pd

#zip code data
#load data
df = pd.read_csv(r"US_Accidents_June20.tar\US_Accidents_June20.csv", usecols=["Zipcode"])
print(df.head())
print()
df.to_csv(r'zipcodes.csv', index = False, header = True)