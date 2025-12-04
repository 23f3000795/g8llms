import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Quarterly data
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "SatisfactionScore": [0.74, 4.99, 8.18, 5.74]
}

df = pd.DataFrame(data)

# Calculate average
average_score = df["SatisfactionScore"].mean()
print("Average Satisfaction Score:", average_score)

# Benchmark
industry_target = 4.5

# Visualization
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.lineplot(x="Quarter", y="SatisfactionScore", data=df, marker="o", label="Patient Score")
plt.axhline(industry_target, color="red", linestyle="--", label="Industry Target (4.5)")
plt.title("2024 Quarterly Patient Satisfaction Trend")
plt.xlabel("Quarter")
plt.ylabel("Satisfaction Score")
plt.legend()
plt.tight_layout()

# Save plot
plt.savefig("patient_satisfaction_trend.png")
