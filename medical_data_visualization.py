plt.figure(figsize=(8, 6))

#  Age Distribution
plt.subplot(2, 2, 1)
plt.hist(df['Age'].dropna(), bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")

#  Gender Distribution
plt.subplot(2, 2, 2)
gender_count = df['Gender'].value_counts()
plt.bar(gender_count.index, gender_count.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

#  Smoker Distribution
plt.subplot(2, 2, 3)
smoker_count = df['Smoker'].value_counts()
plt.bar(smoker_count.index, smoker_count.values)
plt.title("Smoker vs Non-Smoker")
plt.xlabel("Smoker")
plt.ylabel("Count")

# BMI Distribution
plt.subplot(2, 2, 4)
plt.boxplot(df['BMI'].dropna())
plt.title("BMI Distribution")
plt.ylabel("BMI")


plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 6))

#  Diagnosis Distribution
plt.subplot(2, 2, 1)
diagnosis_count = df[diag_col].value_counts()
plt.bar(diagnosis_count.index, diagnosis_count.values)
plt.title("Diagnosis Distribution")
plt.xlabel("Diagnosis")
plt.ylabel("Count")
plt.xticks(rotation=30)

#  Cholesterol Distribution
plt.subplot(2, 2, 2)
plt.hist(df[chol_col].dropna(), bins=10)
plt.title("Cholesterol Distribution")
plt.xlabel("Cholesterol")
plt.ylabel("Count")

#  Age vs BMI (Scatter Plot)
plt.subplot(2, 2, 3)
plt.scatter(df[age_col], df[bmi_col])
plt.title("Age vs BMI")
plt.xlabel("Age")
plt.ylabel("BMI")

#  Blood Pressure vs Age (Line Plot)
plt.subplot(2, 2, 4)
sorted_df = df.sort_values(age_col)
plt.plot(sorted_df[age_col], sorted_df[bp_col])
plt.title("Blood Pressure Trend by Age")
plt.xlabel("Age")
plt.ylabel("Blood Pressure")

plt.tight_layout()
plt.show()




