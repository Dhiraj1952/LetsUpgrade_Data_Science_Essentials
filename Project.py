import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("------Module 1------")
#Read the dataset
Ex=pd.read_csv("pubg.csv")
print(Ex.head())
print()
print("------Module 2------")
#Check the datatype of all the columns
print(Ex.dtypes)
print()
print("------Module 3------")
#Find the summary of all the numerical columns and write your findings about it
print(Ex.describe())
print()
print("------Module 4------")
#The average person kills how many players?
print(Ex['kills'].mean(axis=0))
print()
print("------Module 5------")
#99% of people have how many kills?
print("99% of people have",np.percentile(Ex.kills,99),"kills")
print()
print("------Module 6------")
#The most kills ever recorded are how much?
print("The most kill ever recorded are :",Ex.kills.max())
print()
print("------Module 7------")
#Print all the columns of the dataframe
print(Ex.columns)
print()
print("------Module 8------")
#Comment on distribution of the match's duration. Use seaborn.
M=sns.distplot( Ex['matchDuration'] )
plt.title('Match Duration')
plt.xticks(rotation=70);
plt.show();
print()
print("------Module 9------")
#Comment on distribution of the Walk duration. Use seaborn.
W=sns.distplot( Ex['walkDistance'] )
plt.title('Walk Distance')
plt.xticks(rotation=70);
plt.show();
print()
print("------Module 10------")
#Plot distribution of the match's duration vs walk distance one below the other.
plt.style.use('classic')
plt.subplot(2,1,1)
plt.plot(Ex['matchDuration'],'-b')
plt.subplot(2,1,2)
plt.plot(Ex['walkDistance'],'--g',)
plt.show()
print("------Module 11------")
#Plot distribution of the match's duration vs walk distance side by side..
plt.style.use('classic')
plt.figure(figsize=(15,3))
plt.subplot(1,2,1)
plt.plot(Ex['matchDuration'],'-b')
print(plt.xlabel('Match Duration'))
plt.subplot(1,2,2)
plt.plot(Ex['walkDistance'],'--g',)
print(plt.xlabel('Walk Duration'))
plt.show()
print("------Module 12------")
#Pairplot the dataframe. Comment on kills vs damage dealt, Comment on maxPlace vs numGroups
print(sns.pairplot(Ex.head(500)));
plt.figure()
plt.xticks(rotation=70);
plt.show()
print("Kills and Damage dealt have linear relationship\n")
print("Kills and Damagae dealt numGroups have linear relationship")
print()
print("----------Module 13-----------")
#How many unique values are there in 'matchType' and what are their counts?
uni = pd.unique(Ex['matchType'])
print("\nUnique value in matchType is :",uni)
n_uni = len(uni)
print("\nCount of unique value in matchType is :",n_uni)
print()
print("---------Module 14----------")
#Plot a barplot of ‘matchType’ vs 'killPoints'. Write your inferences.
print(sns.barplot(Ex['matchType'],Ex['killPoints']));
plt.xticks(rotation=70);
plt.show()
print("normal-squad-fpp and normal-squad-fpp match types has the most kill points\n",
    "solo-fpp and solo match types has the less kill points")
print()
print("-----------Module 15-------------")
#Plot a barplot of ‘matchType’ vs ‘weaponsAcquired’. Write your inferences
print(sns.barplot(Ex['matchType'],Ex['weaponsAcquired']));
plt.xticks(rotation=70);
plt.show()
print("In crashtpp and crashfpp match types weapons acquired by players are very less\n,"
      "In normal-solo-fpp and normal-squad-fpp match types weapons acquired by players are more")
print()

print("-------------Module 16--------------")
#Find the Categorical columns.
print(Ex.select_dtypes(exclude=['number']))
print()
print("-------------Module 17---------------")
#Plot a boxplot of ‘matchType’ vs ‘winPlacePerc’. Write your inferences
print(sns.boxplot(x='matchType', y='winPlacePerc', data=Ex));
plt.xticks(rotation=70);
plt.show()
print()
print("-------------Module 18---------------")
#Plot a boxplot of ‘matchType’ vs ‘matchDuration’. Write your inferences.
print(sns.boxplot(x='matchType', y='matchDuration', data=Ex));
plt.xticks(rotation=70);
plt.show()
print()
print("-------------Module 19---------------")
#Change the orientation of the above plot to horizontal
print(sns.boxplot( x='matchDuration', y='matchType',data=Ex));
plt.xticks(rotation=70);
plt.show()
print()
print("-------------Module 20---------------")
#Add a new column called ‘KILL’ which contains the sum of following columns viz. headshotKills, teamKills, roadKills.
Ex['KILL'] = Ex['headshotKills'] + Ex['teamKills'] + Ex['roadKills']
print(Ex['KILL'])
print()
print("-------------Module 21---------------")
#Round off column ‘winPlacePerc’ to 2 decimals.
print(Ex['winPlacePerc'].round(decimals=2))
print()
print("-------------Module 22---------------")
#Take a sample of size 50 from the column damageDealt for 100 times and calculate its mean. Plot it on a histogram and comment on its distribution
x = []
for i in range(100):
    mean1=Ex['damageDealt'].sample(50).mean()
    x.append(mean1)
print("the mean of the 50 sample will:\n",x)
means = np.array(x)
print(sns.histplot(means));
plt.xticks(rotation=70);
plt.show()







