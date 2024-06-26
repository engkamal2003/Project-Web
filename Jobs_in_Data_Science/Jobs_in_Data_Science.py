import pandas as pd

# Load the dataset
df = pd.read_csv('/Users/kamal.reesh/Documents/Project Web/Jobs_in_Data_Science/Jobs_in_Data_Science.csv')



# Drop irrelevant columns
columns_to_drop = ['company_size', 'work_year', 'salary_currency', 'work_setting', 'salary']
df.drop(columns=columns_to_drop, inplace=True)



# Rename columns to shorter names
df.rename(columns={
    'employee_residence': 'residence',
    'salary_in_usd': 'salary_usd',
    'company_location': 'location',
    'experience_level': 'experience'
}, inplace=True)



# Count duplicates before dropping
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate records: {duplicate_count}")

# Drop duplicate records
df.drop_duplicates(inplace=True)


# Number of employees working as Data Scientists
data_scientist_count = df[df['job_title'] == 'Data Scientist'].shape[0]
print(f"Number of Data Scientists: {data_scientist_count}")



# Count for each job title
job_title_counts = df['job_title'].value_counts()
print(job_title_counts)



# Data Scientist with the highest salary
highest_paid_ds = df[df['job_title'] == 'Data Scientist'].sort_values(by='salary_usd', ascending=False).iloc[0]
print("Highest paid Data Scientist:")
print(highest_paid_ds)

# Data Scientist with the lowest salary
lowest_paid_ds = df[df['job_title'] == 'Data Scientist'].sort_values(by='salary_usd', ascending=True).iloc[0]
print("Lowest paid Data Scientist:")
print(lowest_paid_ds)




# Statistical metrics for 'salary_usd'
salary_stats = {
    'mean': df['salary_usd'].mean(),
    'median': df['salary_usd'].median(),
    'min': df['salary_usd'].min(),
    'max': df['salary_usd'].max(),
    'range': df['salary_usd'].max() - df['salary_usd'].min(),
    'variance': df['salary_usd'].var(),
    'std_dev': df['salary_usd'].std(),
    'iqr': df['salary_usd'].quantile(0.75) - df['salary_usd'].quantile(0.25),
    'skewness': df['salary_usd'].skew(),
    'kurtosis': df['salary_usd'].kurt()
}
print(salary_stats)


import matplotlib.pyplot as plt

# Bar chart for top 20 job titles
top_20_job_titles = job_title_counts.head(20)
plt.figure(figsize=(10, 8))
top_20_job_titles.plot(kind='bar')
plt.title('Top 20 Job Titles')
plt.xlabel('Job Title')
plt.ylabel('Count')
plt.show()

# Pie chart for top 10 job titles
top_10_job_titles = job_title_counts.head(10)
plt.figure(figsize=(10, 8))
top_10_job_titles.plot(kind='pie', autopct='%1.1f%%')
plt.title('Top 10 Job Titles')
plt.ylabel('')
plt.show()






