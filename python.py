import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import seaborn as sns

## df is the data name
df = pd.read_csv(r"C:\Users\needs\Desktop\JU\Rumana Rois\w3\haberman.csv")

####Figure 1
df.boxplot()
plt.show()
####Figure 2
plt.boxplot(df.age)
plt.title('Boxplot for Age of Breast Cancer Patients')
plt.show()
####Figure 3
##Histogram
plt.hist(df.age, bins=10)
plt.xlabel('Age of Patients')
plt.ylabel('Number of Patients')
plt.title('Histogram of Age of Breast Cancer Patients')
plt.show()
####Figure 4
plt.boxplot(df.axil_nodes)
plt.title('Boxplot for Axillary Nodes of Breast Cancer Patients')
plt.show()
####Figure 5
##Histogram
plt.hist(df.axil_nodes, bins=10)
plt.xlabel('Axillary Nodes of Patients')
plt.ylabel('Number of Patients')
plt.title('Histogram of Axillary Nodes of Breast Cancer Patients')
plt.show()
####Figure 6
plt.boxplot(df.operation_year)
plt.title('Boxplot for Operation Year of Breast Cancer Patients')
plt.show()
####Figure 7 ##Histogram
plt.hist(df.operation_year, bins=10)
plt.xlabel('Operation Year')
plt.ylabel('Number of Patients')
plt.title('Histogram of Operation Year of Breast Cancer Patients')
plt.show()
####Figure 8 ## Bar diagram
objects = ('Survived', 'Dead')
x_pos = np.arange(len(objects))
status_fre=[225, 81] # get the frequency value from df.status.value_counts()

plt.bar(x_pos, status_fre)
plt.xticks(x_pos, objects)
plt.ylabel('Number of Patients')
plt.title('Survival Status of Breast Cancer Patients')
plt.show()
####Figure 9 ## Pie Chart
status_fre=[225, 81]
plt.pie(status_fre, labels=['Survived', 'Dead'], colors=['yellowgreen', 'lightcoral'],  autopct='%.1f%%')
plt.show()
############### Stem-and-leaf Plot
import stemgraphic
fig, ax = stemgraphic.stem_graphic(df.age)
plt.show()
#######################
datarowsSeries = [pd.Series([30, 66, 2, 1], index=df.columns ),
                  pd.Series([100, 3, 1, 0], index=df.columns ),]
df = df.append(datarowsSeries , ignore_index=True)
fig, ax = stemgraphic.stem_graphic(df.age)
plt.show()

####Figure 10 ##Scatter Diagram
plt.scatter(df['age'],df['axil_nodes'], color = 'g')
plt.xlabel('Age')
plt.ylabel('Axil Nodes')
plt.title('Axil_nodes vs Age')
plt.show()

##to label status variable in readable format, 1 labeled as 'survived' and 2 labeled as 'dead'
df['status'] = df['status'].map({1:'survived', 2:'dead'})
####Figure 11
sns.set_style('whitegrid');
sns.FacetGrid(df, hue = 'status', height = 6)\
.map(plt.scatter, 'age', 'axil_nodes')\
.add_legend();
plt.show();
####Figure 12##Scatter Diagram
plt.scatter(df['age'],df['operation_year'], c = 'b')
plt.xlabel('Age')
plt.ylabel('Operation year')
plt.title('Operation year vs Age')
plt.show()
####Figure 13##Scatter Diagram
plt.scatter(df['operation_year'],df['axil_nodes'], color = 'r')
plt.xlabel('Operation Year')
plt.ylabel('Axillary Nodes')
plt.title('Operation Year vs Axillary Nodes')
plt.show()

######Figure 14
sns.boxplot(x='status',y='axil_nodes', data=df)
plt.show()
####Figure 15
sns.boxplot(x='status',y='age', data=df)
plt.show()
####Figure 16
sns.boxplot(x='status',y='operation_year', data=df)
plt.show()
####Figure 17##Pairplots
sns.set_style('whitegrid');
sns.pairplot(df, hue = 'status', height = 4)
plt.show()