import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# LOAD DATASET
# ============================================================

df = pd.read_csv("dataset.csv")


# ============================================================
# BASIC INFORMATION
# ============================================================

print(df.head())
print(df.shape)
print(df.columns)


# ============================================================
# DEPARTMENT ANALYSIS
# ============================================================

print("\nDepartment analysis:")
print(df["Department"].value_counts())


# ============================================================
# SALARY ANALYSIS
# ============================================================

print("\nOverall average salary:")
print(df["Salary_USD"].mean())

print("\nAverage salary by department:")
print(df.groupby("Department")["Salary_USD"].mean())


# ============================================================
# EXPERIENCE ANALYSIS
# ============================================================

print("\nAverage years of experience:")
print(df["Years_of_Experience"].mean())

print("\nExperience and salary:")
print(df[["Years_of_Experience", "Salary_USD"]].head(10))

correlation = df["Years_of_Experience"].corr(df["Salary_USD"])

print("\nCorrelation between experience and salary:", correlation)

if correlation > 0:
    print("There is a positive relationship between experience and salary.")
elif correlation < 0:
    print("There is a negative relationship between experience and salary.")
else:
    print("There is no linear relationship between experience and salary.")


# ============================================================
# PERFORMANCE ANALYSIS
# ============================================================

print("\nPerformance rating distribution:")
print(df["Performance_Rating"].value_counts())

print("\nPerformance rating percentage:")
print(df["Performance_Rating"].value_counts(normalize=True) * 100)

print("\nAverage salary by performance rating:")
print(df.groupby("Performance_Rating")["Salary_USD"].mean())


# ============================================================
# EMPLOYEE STATUS ANALYSIS
# ============================================================

print("\nEmployee status:")
print(df["Status"].value_counts())


# ============================================================
# WORK MODE ANALYSIS
# ============================================================

work_mode_count = df["Work_Mode"].value_counts()

print("\nWork mode:")
print(work_mode_count)

most_common_work_mode = work_mode_count.idxmax()
most_common_work_mode_count = work_mode_count.max()

print("Most common work mode:", most_common_work_mode)
print("Number of employees:", most_common_work_mode_count)


# ============================================================
# EDUCATION ANALYSIS
# ============================================================

print("\nEducation level:")
print(df["Education_Level"].value_counts())

print("\nAverage salary by education level:")
print(df.groupby("Education_Level")["Salary_USD"].mean())


# ============================================================
# DATA CLEANING
# ============================================================

print("\nMissing values in each column:")
print(df.isnull().sum())

duplicate_count = df.duplicated().sum()

print("\nNumber of duplicate rows:", duplicate_count)




df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    format="mixed",
    errors="coerce"
)

print("\nUpdated data types:")
print(df.dtypes)

print("\nInvalid dates found:")
print(df["Joining_Date"].isnull().sum())




invalid_dates = df[df["Joining_Date"].isna()]

print("\nEmployees with invalid joining dates:")
print(invalid_dates[["Employee_ID", "Name", "Joining_Date"]])

print("\nNumber of valid joining dates:",
      df["Joining_Date"].notna().sum())

print("Number of invalid joining dates:",
      df["Joining_Date"].isna().sum())


# ============================================================
# KEY FINDINGS
# ============================================================

department_salary = df.groupby("Department")["Salary_USD"].mean()

highest_salary_department = department_salary.idxmax()
highest_salary = department_salary.max()

lowest_salary_department = department_salary.idxmin()
lowest_salary = department_salary.min()

education_salary = df.groupby("Education_Level")["Salary_USD"].mean()

highest_education = education_salary.idxmax()
highest_education_salary = education_salary.max()

print("\n========== KEY FINDINGS ==========")

print("Department with highest average salary:",
      highest_salary_department)

print("Highest average salary:",
      highest_salary)

print("Department with lowest average salary:",
      lowest_salary_department)

print("Lowest average salary:",
      lowest_salary)

print("Education level with highest average salary:",
      highest_education)

print("Highest average salary by education:",
      highest_education_salary)

print("Most common work mode:",
      most_common_work_mode)

print("Employees in most common work mode:",
      most_common_work_mode_count)


# ============================================================
# VISUALIZATIONS
# ============================================================


avg_salary_education = df.groupby(
    "Education_Level"
)["Salary_USD"].mean()

avg_salary_education.plot(kind="bar")

plt.title("Average Salary by Education Level")
plt.xlabel("Education Level")
plt.ylabel("Average Salary (USD)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()




avg_salary_department = df.groupby(
    "Department"
)["Salary_USD"].mean()

avg_salary_department.plot(kind="bar")

plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




plt.scatter(
    df["Years_of_Experience"],
    df["Salary_USD"]
)

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary (USD)")
plt.tight_layout()
plt.show()


performance_count = df["Performance_Rating"].value_counts()

performance_count.plot(kind="bar")

plt.title("Employee Performance Rating Distribution")
plt.xlabel("Performance Rating")
plt.ylabel("Number of Employees")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()




status_count = df["Status"].value_counts()

status_count.plot(kind="bar")

plt.title("Employee Status Distribution")
plt.xlabel("Status")
plt.ylabel("Number of Employees")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


print("\n========== PROJECT ANALYSIS COMPLETE ==========")