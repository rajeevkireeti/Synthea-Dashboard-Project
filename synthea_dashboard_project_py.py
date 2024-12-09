# -*- coding: utf-8 -*-
"""synthea_dashboard_project.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Xaehu6H8rXDDA3cxoJQxeh5uOW2fVflO
"""

import pandas as pd
import matplotlib.pyplot as plt

# Prepare hypothetical datasets
age_group_counts = pd.Series({'19–64': 8, '0–10': 1, '65+': 1})
phq9_counts = pd.Series({'Patient Health Questionnaire 9 item (PHQ-9) total score [Reported]': 15})
treatment_analysis = pd.Series({True: 20, False: 14})
cpt_df = pd.DataFrame({
    "CPT_Code": ["90834", "99213", "96127", "90837", "90791"],
    "Description": [
        "Psychotherapy, 45 minutes",
        "Office/outpatient visit",
        "Brief emotional/behavioral assessment",
        "Psychotherapy, 60 minutes",
        "Psychiatric diagnostic evaluation",
    ],
    "Frequency": [150, 120, 100, 80, 50],
})

# Visualize Age Group Distribution
plt.figure(figsize=(8, 5))
age_group_counts.plot(kind='bar')
plt.title('Age Group Distribution')
plt.xlabel('Age Groups')
plt.ylabel('Number of Patients')
plt.xticks(rotation=0)
plt.show()

# Visualize PHQ-9 Scores
plt.figure(figsize=(8, 5))
phq9_counts.plot(kind='bar')
plt.title('Distribution of PHQ-9 Scores')
plt.xlabel('PHQ-9 Score Categories')
plt.ylabel('Number of Patients')
plt.xticks(rotation=45)
plt.show()

# Visualize Depression Treatment Analysis
plt.figure(figsize=(8, 5))
treatment_analysis.plot(kind="bar", color=["green", "red"])
plt.title("Depression Treatment Within 90 Days")
plt.xlabel("Treatment Received")
plt.ylabel("Number of Patients")
plt.xticks(ticks=[0, 1], labels=["Yes", "No"], rotation=0)
plt.show()

# Visualize CPT Code Utilization
plt.figure(figsize=(8, 5))
plt.barh(cpt_df["Description"], cpt_df["Frequency"], color="blue")
plt.title("CPT Code Utilization for Psychiatric Cases")
plt.xlabel("Frequency")
plt.ylabel("CPT Codes")
plt.gca().invert_yaxis()  # Reverse order for better readability
plt.show()

# Dashboard summary
dashboard_summary = {
    "Age Distribution": age_group_counts,
    "PHQ-9 Scores": phq9_counts,
    "Depression Treatment Analysis": treatment_analysis,
    "CPT Code Utilization": cpt_df,
}