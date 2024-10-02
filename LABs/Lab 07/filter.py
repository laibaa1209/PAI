import pandas as pd

df  = pd.read_csv("dataset.csv")

filtered_df = df[df["cp"]==2]
print(filtered_df)

total_cp_2 = filtered_df =(df["cp"]==2).sum()
print("Total num of rows of cp = 2", total_cp_2)

# 4 categories of applying groupby
# single group single column analysis
# single group multiple columns analysis
# multiple group single column analysis
# multiple group multiple column analysis

#single group
cp_group = df.groupby("cp")

#single group single column anaylsis
print(cp_group['age'].mean())

#single group multiple column
print(cp_group[['age', 'ca']].mean())


#multiple group
cp_group2 = df.groupby(['cp', 'ca'])

#multiple group single column
print(cp_group2['age'].mean())

#multiple group multiple column
print(cp_group2[['age', 'ca']].mean())


df = df.groupby("cp")
print(df.get_group(2))
print(df.get_group(1))

# print("1 to MALE and 0 to FEMALE.")
df = df.rename(columns={'sex': 'gender'})
# df_1['gender'][df_1['gender'] == 0] = 'Female'
# df_1['gender'][df_1['gender'] == 1] = 'Male'
# print(df_1)

male_records = df[df['gender'] == 'M']
female_records = df[df['gender'] == 'F']
print("Male records:", male_records)
print("Female records:", female_records)


df['trestbps'].unique()
bp_filtered_df = df[df['trestbps'].between(120, 140)]
print("Filtered DataFrame where 'trestbps' is between 120 and 140:")
print(bp_filtered_df)

print("\nMale records: ")
print(male_records.describe())
print("\nFemale records: ")
print(female_records.describe())

#single g
df1 = df.groupby('gender')
#single c
print(df1['chol'].max(), end = '\n\n')
print(df1['chol'].median(), end = '\n\n')
print(df1['chol'].mean(), end = '\n\n')
#multi c
print(df1[['restecg', 'oldpeak', 'chol']].max(), end = '\n\n')
print(df1[['restecg', 'oldpeak', 'chol']].median(), end = '\n\n')
print(df1[['restecg', 'oldpeak', 'chol']].mean(), end = '\n\n')

