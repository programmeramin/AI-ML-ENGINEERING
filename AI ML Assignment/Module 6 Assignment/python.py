"""
Module 06 Assignment: Exploratory Data Analysis (EDA) on the Titanic Dataset
"""
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLOT_DIR = os.path.join(BASE_DIR, "plots")
os.makedirs(PLOT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 20)


def save_plot(filename):
    """Save the current figure into the plots folder and show it."""
    plt.tight_layout()
    plt.savefig(os.path.join(PLOT_DIR, filename), dpi=120)
    plt.show()
    plt.close()


def section(title):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


# ======================================================================
# Task 1: Data Loading and Initial Inspection
# ======================================================================
section("Task 1: Data Loading and Initial Inspection")

df = pd.read_csv(os.path.join(BASE_DIR, "titanic.csv"))

print("\nFirst 5 rows:")
print(df.head())

print("\nData types / info:")
df.info()

print("\nDescriptive statistics (numerical columns):")
print(df.describe())

print("\nMissing values per column:")
print(df.isnull().sum())


# ======================================================================
# Task 2: Handling Missing Values
# ======================================================================
section("Task 2: Handling Missing Values")

# --- Cabin ---
cabin_missing_pct = df["Cabin"].isnull().mean() * 100
print(f"\nCabin missing values: {cabin_missing_pct:.2f}%")
print(
    "Decision: Drop the Cabin column. About 77% of its values are missing, so\n"
    "imputing it would mostly be guessing and could introduce heavy bias. With\n"
    "so little real information, it is not reliable for this analysis."
)
df = df.drop(columns=["Cabin"])

# --- Embarked ---
embarked_mode = df["Embarked"].mode()[0]
print(f"\nMost frequent port of embarkation (mode): {embarked_mode}")
df["Embarked"] = df["Embarked"].fillna(embarked_mode)

# --- Age ---
age_median = df["Age"].median()
print(f"Median age used for imputation: {age_median}")
df["Age"] = df["Age"].fillna(age_median)

print("\nMissing values after handling:")
print(df.isnull().sum())


# ======================================================================
# Task 3: Univariate Analysis
# ======================================================================
section("Task 3: Univariate Analysis")

# --- Survival Rate ---
survival_rate = df["Survived"].mean() * 100
print(f"\nOverall survival rate: {survival_rate:.2f}%")
print(df["Survived"].value_counts().rename({0: "Did not survive", 1: "Survived"}))

plt.figure(figsize=(6, 4))
ax = sns.countplot(x="Survived", data=df, hue="Survived", palette="Set2", legend=False)
ax.set_xticks([0, 1], ["Did not survive (0)", "Survived (1)"])
ax.set_title("Distribution of Survival")
ax.set_ylabel("Number of passengers")
for container in ax.containers:
    ax.bar_label(container)
save_plot("1_survived_count.png")

# --- Passenger Class ---
pclass_counts = df["Pclass"].value_counts().sort_index()
print("\nPassengers per class:")
print(pclass_counts)
print(f"Class with the most passengers: {pclass_counts.idxmax()} "
      f"({pclass_counts.max()} passengers)")

plt.figure(figsize=(6, 4))
ax = sns.countplot(x="Pclass", data=df, hue="Pclass", palette="Set2", legend=False)
ax.set_title("Distribution of Passenger Class")
ax.set_xlabel("Passenger class")
ax.set_ylabel("Number of passengers")
for container in ax.containers:
    ax.bar_label(container)
save_plot("2_pclass_count.png")

# --- Age Distribution ---
plt.figure(figsize=(8, 4))
sns.histplot(df["Age"], bins=30, kde=True, color="steelblue")
plt.title("Age Distribution (after median imputation)")
plt.xlabel("Age")
plt.ylabel("Number of passengers")
save_plot("3_age_histogram.png")
print("\nNote: the tall spike near 28 comes from filling missing ages with the median.")


# ======================================================================
# Task 4: Bivariate and Multivariate Analysis
# ======================================================================
section("Task 4: Bivariate and Multivariate Analysis")

# --- Survival by Sex ---
sex_crosstab = pd.crosstab(df["Sex"], df["Survived"])
sex_crosstab.columns = ["Did not survive", "Survived"]
print("\nSurvival count by Sex:")
print(sex_crosstab)

sex_survival_rate = df.groupby("Sex")["Survived"].mean() * 100
print("\nSurvival rate by Sex (%):")
print(sex_survival_rate.round(2))

ax = sex_crosstab.plot(kind="bar", stacked=True, figsize=(6, 4), color=["#e76f51", "#2a9d8f"])
ax.set_title("Survival by Sex")
ax.set_xlabel("Sex")
ax.set_ylabel("Number of passengers")
ax.tick_params(axis="x", rotation=0)
save_plot("4_survival_by_sex.png")

print(
    f"\nAnswer: Females had a much higher survival rate "
    f"({sex_survival_rate['female']:.1f}%) than males "
    f"({sex_survival_rate['male']:.1f}%)."
)

# --- Survival by Pclass ---
class_survival_rate = df.groupby("Pclass")["Survived"].mean() * 100
print("\nSurvival rate by Pclass (%):")
print(class_survival_rate.round(2))

plt.figure(figsize=(6, 4))
ax = sns.barplot(x=class_survival_rate.index, y=class_survival_rate.values,
                 hue=class_survival_rate.index, palette="Set2", legend=False)
ax.set_title("Survival Rate by Passenger Class")
ax.set_xlabel("Passenger class")
ax.set_ylabel("Survival rate (%)")
for container in ax.containers:
    ax.bar_label(container, fmt="%.1f%%")
save_plot("5_survival_by_pclass.png")

print(
    "\nAnswer: Yes. There is a clear correlation - the higher the class, the higher\n"
    "the survival chance (1st > 2nd > 3rd). Correlation between Pclass and Survived: "
    f"{df['Pclass'].corr(df['Survived']):.3f} (negative because class 1 is the 'best')."
)

# --- Survival by Age ---
plt.figure(figsize=(9, 4))
sns.histplot(data=df, x="Age", hue="Survived", bins=30, kde=True,
             element="step", stat="density", common_norm=False,
             palette={0: "#e76f51", 1: "#2a9d8f"})
plt.title("Age Distribution: Survivors vs Non-survivors")
plt.xlabel("Age")
save_plot("6_age_by_survival.png")

plt.figure(figsize=(6, 4))
sns.boxplot(x="Survived", y="Age", data=df, hue="Survived",
            palette={0: "#e76f51", 1: "#2a9d8f"}, legend=False)
plt.xticks([0, 1], ["Did not survive", "Survived"])
plt.title("Age by Survival")
save_plot("7_age_boxplot_by_survival.png")

age_groups = pd.cut(df["Age"], bins=[0, 12, 18, 35, 60, 80],
                    labels=["Child (0-12)", "Teen (13-18)", "Young adult (19-35)",
                            "Adult (36-60)", "Elderly (61-80)"])
age_group_survival = df.groupby(age_groups, observed=True)["Survived"].agg(["count", "mean"])
age_group_survival["mean"] = (age_group_survival["mean"] * 100).round(2)
age_group_survival.columns = ["Passengers", "Survival rate (%)"]
print("\nSurvival rate by age group:")
print(age_group_survival)
print(
    "\nObservation: Children (especially under ~10) had a noticeably higher survival\n"
    "chance - the survivor curve has a bump at young ages ('women and children first').\n"
    "The elderly (60+) had the lowest survival chance of all age groups."
)

# --- Survival by Embarked ---
embarked_survival_rate = df.groupby("Embarked")["Survived"].mean() * 100
print("\nSurvival rate by port of embarkation (%):")
print(embarked_survival_rate.round(2))

port_names = {"C": "Cherbourg (C)", "Q": "Queenstown (Q)", "S": "Southampton (S)"}
plt.figure(figsize=(6, 4))
ax = sns.barplot(x=embarked_survival_rate.index.map(port_names),
                 y=embarked_survival_rate.values,
                 hue=embarked_survival_rate.index, palette="Set2", legend=False)
ax.set_title("Survival Rate by Port of Embarkation")
ax.set_xlabel("Port")
ax.set_ylabel("Survival rate (%)")
for container in ax.containers:
    ax.bar_label(container, fmt="%.1f%%")
save_plot("8_survival_by_embarked.png")

print("\nPclass distribution within each port (shows why Cherbourg did better):")
print(pd.crosstab(df["Embarked"], df["Pclass"], normalize="index").round(2))


# ======================================================================
# Task 5: Conclusion and Insights
# ======================================================================
section("Task 5: Conclusion and Insights")

print(
    "Only about 38% of passengers survived, and survival was far from random.\n"
    "Sex was the strongest predictor: about 74% of women survived compared with\n"
    "only about 19% of men, reflecting the 'women and children first' policy.\n"
    "Passenger class was the second strongest factor - 1st class passengers\n"
    "survived at roughly 63%, versus about 47% in 2nd and only 24% in 3rd class.\n"
    "Age also mattered: young children had better odds while the elderly had the\n"
    "worst. Port of embarkation showed differences too (Cherbourg highest), but\n"
    "that is largely explained by Cherbourg having more 1st class passengers.\n"
    "Top predictors of survival: 1) Sex, 2) Pclass, 3) Age."
)

print(f"\nAll plots saved in: {PLOT_DIR}")
