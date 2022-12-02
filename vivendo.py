import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

#importing our data set
claims = pd.read_csv('claims.csv')

#cleaning the data frame
claims['Claim Amount'] = claims['Claim Amount'].apply(lambda st: st[st.find("$")+1:st.find(".")]).str.replace(",","")
claims['Claim Amount'] = pd.to_numeric(claims['Claim Amount'])
claims['Linked Cases'] = claims['Linked Cases'].astype(str)
claims['Linked Cases'] = claims['Linked Cases'].str.upper()
claims['Cause'] = claims['Cause'].fillna('unknown').str.replace('vegetables', 'vegetable')
print(claims.head())
print("There are " + str(claims['Cause'].nunique()) + " Unique Cause,")
print("____________")
print("Count 3 Causes of the Food Poisoning :")
print(claims['Cause'].value_counts())

#creating a histogram presenting the causes of food poisioning 
plt.figure(figsize=(10,6))
color = ['#E15759','#59A14F','#F28E2B']
splot = sns.countplot(data=claims,x=claims['Cause'],palette=color)
plt.xlabel("Cause")
plt.ylabel("Counts")
plt.title('Total 3 Main Cause of The Food Poisoning Injuries', fontsize = 14)
for p in splot.patches:
  splot.annotate(format(p.get_height(), '.2f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 5), textcoords = 'offset points')
plt.show()

#creating a bar chart presenting the average number of days taken to close the claims
viveto_claims = claims.groupby('Location')['Time to Close'].mean().round().astype(int)
color = ['royalblue', 'red', 'purple', 'yellow']
print(viveto_claims)

#creating list containing the number of claims for each location
claims_location = {'FORTALEZA':22, 'NATAL':21, 'RECIFE':25, 'SAO LUIS':30}
location = list(claims_location.keys())
number_of_claims = list(claims_location.values())

#creating a bar chart of the number of claims per location


#creating a bar chart of the number of claims per location
style.use('ggplot')
plt.figure(figsize=(5,5))
plt.bar(location, number_of_claims, color=color, width=0.5)
plt.xlabel('claims location')
plt.ylabel('number of claims')
plt.title('number of claims and their locations')
plt.show()

#creating a scatterplot presenting the relationship between average time to close claims and location
plt.scatter(claims['Location'], claims['Time to Close'], s= 10, color='g')
plt.xlabel('locations')
plt.ylabel('average time to close claims')
plt.show()