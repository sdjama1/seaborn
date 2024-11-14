'''
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"S:\downloads\HW 2\Exercise_Data.csv"
exercise_data = pd.read_csv(file_path)

#print(exercise_data.head())
plt.figure(figsize=(8, 6))
sns.heatmap(exercise_data[["1 min", "15 min", "30 min"]].corr(), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap of Heart Rate Data (1 min, 15 min, 30 min)")
plt.show()


plt.figure(figsize=(12, 8))
sns.catplot(data=exercise_data.melt(id_vars=["diet", "kind"], value_vars=["1 min", "15 min", "30 min"],
                                    var_name="Time", value_name="Heart Rate"),
            x="diet", y="Heart Rate", hue="kind", col="Time", kind="bar", height=5, aspect=0.8)
plt.suptitle("Heart Rate by Diet and Exercise Type at Different Time Points", y=1.05)
plt.xlabel("Diet Type")
plt.ylabel("Heart Rate")
plt.show()

"Different diets like low fat vs no fat and the exercise type lead to different heart rates. The exercise intensity like running lead to higher rates than resting, wich is essential for staying healthy"



*remove lines 30 and 1 if you want to test above codes
'''
import seaborn as sns
import matplotlib.pyplot as plt
planets_data = sns.load_dataset("planets")
sns.set(style="whitegrid")

#1 relational plots

# Scatter Plot// Orbital Period vs. Mass
plt.figure(figsize=(10, 6))
sns.scatterplot(data=planets_data, x="mass", y="orbital_period", hue="method", palette="viridis", alpha=0.7)
plt.title("prbital period vs. mass of exoplanets")
plt.xlabel("Mass (Jupiter Mass)")
plt.ylabel("Orbital Period (days)")
plt.legend(title="Detection Method")
plt.show()

# Line Plot/Year vs. Count of Discoveries
plt.figure(figsize=(10, 6))
sns.lineplot(data=planets_data, x="year", y="distance", hue="method", ci=None, palette="muted")
plt.title("Average distance of exoplanet discoveries over time")
plt.xlabel("Year")
plt.ylabel("Distance (Parsecs)")
plt.legend(title="Detection Method")
plt.show()

#2 distributional plots

# histogram/distribution of Mass
plt.figure(figsize=(10, 6))
sns.histplot(planets_data["mass"].dropna(), bins=30, kde=True, color="teal")
plt.title("Distribution of Exoplanet Masses")
plt.xlabel("Mass (Jupiter Mass)")
plt.ylabel("Frequency")
plt.show()

# Box plot/ mass by Method
plt.figure(figsize=(12, 6))
sns.boxplot(data=planets_data, x="method", y="mass", palette="coolwarm")
plt.title("Mass of Exoplanets by Detection Method")
plt.xlabel("Detection Method")
plt.ylabel("Mass (Jupiter Mass)")
plt.xticks(rotation=45)
plt.show()

# 3 Categorical Plots

# count plot/ number of discoveries by Detection Method
plt.figure(figsize=(12, 6))
sns.countplot(data=planets_data, y="method", palette="Spectral")
plt.title("Number of exoplanet discoveries by detection method")
plt.xlabel("Count")
plt.ylabel("Detection Method")
plt.show()

# bar plot/ average orbital period by Detection Method
plt.figure(figsize=(12, 6))
sns.barplot(data=planets_data, x="method", y="orbital_period", estimator="mean", palette="rocket")
plt.title("Average orbitsl period by detection Method")
plt.xlabel("Detection Method")
plt.ylabel("Average Orbital Period (days)")
plt.xticks(rotation=45)
plt.show()
