import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn
#EDA Process
df=pd.read_csv("C:/Users/anusr/OneDrive/Desktop/CA 2 Project 12319748/Dealer Wise Particular Part Stock (2).csv")
print(df)
print(df.head())
#Summary
print(df.info())
#describe statistics
print(df.describe())

#checking null values
t = df.isnull().sum()
print("Null Values count:",t)
#Replacing null values
print("Total null values:", df.isnull().sum().sum())
print(df['Zonal Office'].isnull().sum())
print(df['Area Office'].isnull().sum())
print(df['Dealer Name'].isnull().sum())
print(df['Inventory Location'].isnull().sum())
print(df['Part Number'].isnull().sum())
print(df['Part Description'].isnull().sum())
print(df['Stock QTY'].isnull().sum())
print(df['RATE'].isnull().sum())
print(df['Amount'].isnull().sum())
print(df.columns.tolist())

if 'Stock QTY' in df.columns:
    print(df['Stock QTY'] == df['Stock QTY'].fillna(0))  
    print(df['Stock QTY'])                               
else:
    print(" 'Stock QTY' column not found!")

# Show missing value summary
print("\nMissing values per column:\n", df.isnull().sum())
print("\nAny missing values at all?:", df.isnull().values.any())
df['Zonal Office']=df['Zonal Office'].fillna('Unknown')
print(df['Zonal Office'])
print(df.isnull().sum())        
print(df.isnull().values.any())
df['Area Office']=df['Area Office'].fillna('Unknown')
print(df['Area Office'])
print(df.isnull().sum())        
print(df.isnull().values.any())
df['Dealer Name']=df['Dealer Name'].fillna('Unknown')
print(df['Dealer Name'])
print(df.isnull().sum())       
print(df.isnull().values.any())
df['Inventory Location']=df['Inventory Location'].fillna('Unknown')
print(df['Inventory Location'])
print(df.isnull().sum())      
print(df.isnull().values.any())
df['Part Number']=df['Part Number'].fillna(0)
print(df['Part Number'])
print(df.isnull().sum())        
print(df.isnull().values.any())
df['Part Description']=df['Part Description'].fillna('Unknown')
print(df['Part Description'])
print(df.isnull().sum())        
print(df.isnull().values.any())
df['RATE']=df['RATE'].fillna(0)
print(df['RATE'])
print(df.isnull().sum())       
print(df.isnull().values.any())
df['Amount']=df['Amount'].fillna(0)
print(df['Amount'])
print(df.isnull().values.any())
print(df.isnull().sum())        
print(df.isnull().values.any())
#Objective 1:Visualize the top 10 parts by their inventory value (sum of "Amount") in a horizontal bar chart.
top_parts = df.groupby("Part Number", as_index=False)["Amount"].sum()
top_parts = top_parts.nlargest(10, "Amount").sort_values("Amount")
plt.figure(figsize=(7, 4))
sn.barplot(data=top_parts, x="Part Number", y="Amount", color='darkgreen')
plt.title("Top 10 Part Numbers by Inventory Value")
plt.xlabel("Part Number")
plt.ylabel("Inventory Value (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Objective 2:To identify which zones (represented by the top 10 dealers) hold more expensive inventory by analyzing the inventory value using a box plot.
top_dealers = df.groupby('Dealer Name')['Amount'].sum().nlargest(10).index
df_top = df[df['Dealer Name'].isin(top_dealers)]
plt.figure(figsize=(7, 5))
sn.boxplot(data=df_top, x='Dealer Name', y='Amount', palette='husl',legend=False,hue='Dealer Name')
plt.title('Distribution of Inventory Value (Amount) for Top 10 Dealers')
plt.xlabel('Dealer Name')
plt.ylabel('Inventory Value (Amount)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
#Objective 3:To visualize and analyze the unit rates of the top 20 most frequently occurring part descriptions in the dataset using a line plot.
plt.figure(figsize=(7, 5))
top_parts = df["Part Description"].value_counts().head(20).index
filtered_df = df[df["Part Description"].isin(top_parts)]
sn.lineplot(data=filtered_df, x="Part Description", y="RATE", marker="*", linewidth=2)
plt.xticks(rotation=90)
plt.title("Rate by Part Description")
plt.xlabel("Part Description")
plt.ylabel("Rate (Unit Price)")
plt.tight_layout()
plt.grid(True)
plt.show()
#Objective 4:To analyze the relationship between Stock Quantity and Rate of parts across dealers by visualizing their correlation using a heatmap
corr_matrix = df[["Stock QTY", "RATE", ]].corr()
plt.figure(figsize=(6, 5))
sn.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap: Stock QTY, RATE")
plt.show()
#Objective 5:To visualize the distribution and frequency of stock quantities across all parts using a histogram.
plt.figure(figsize=(6, 5))
plt.hist(data=df, x="Stock QTY", bins=30,  color="blue")
plt.title("Histogram of Stock Quantity")
plt.show()

