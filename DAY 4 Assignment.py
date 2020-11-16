#Question 1:
import pandas as pd
print(pd.__version__)

#Question 2
population_dict={"India":2463839, "New_York":68493453,"Brazil":34243432}
S=pd.Series(population_dict) #Converting our dict to series
print(S)

#Question 3
import numpy as np
Arr=np.array([10,42,63,49,25])
SR=pd.Series(Arr)
Con = SR.to_frame().reset_index()
print(Con)

#Question 4:
import seaborn as sns
print("Datasets available in seaborn:\n",sns.get_dataset_names())
mpg=sns.load_dataset('mpg')
print("*****Dataset mpg loaded:*****\n",mpg)

#Question 5:
import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg['origin'].unique())


#Question 6
import seaborn as sns
mpg=sns.load_dataset('mpg')
print(mpg[mpg['origin']=='usa'])
