
import pandas as pd  # Library to handle data

# Load the Excel file
file_path = "500713128_submissions-vs-hires-3790691742579723.xlsx"
data = pd.read_excel(file_path)

# Show the first few rows of the dataset
print(data.head())
# Check for missing values
print("Missing Values:")
print(data.isnull().sum())
# Remove rows with missing data
data.dropna(inplace=True)
print("Cleaned Data:")
print(data.head())

# Calculate total submissions
total_submissions = data['# Submissions'].sum()
print(f"Total Submissions: {total_submissions}")

# Group submissions by team
submissions_by_team = data.groupby('User Name')['# Submissions'].sum()
print("\nSubmissions by User Name:")
print(submissions_by_team)


# Import required libraries
import matplotlib.pyplot as plt

# Bar plot of submissions by User Name
plt.figure(figsize=(10, 6))
submissions_by_user = data.groupby('User Name')['# Submissions'].sum()

# Create a bar chart
submissions_by_user.plot(kind='bar', color='skyblue')
plt.title("Submissions by User Name")
plt.xlabel("User Name")
plt.ylabel("Total Submissions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





