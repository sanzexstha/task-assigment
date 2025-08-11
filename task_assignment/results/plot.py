import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Step 1: Load the CSV Files ---
# CSV file for the anomaly-based greedy method ("greedy+outlier")
df_outlier = pd.read_csv("anomaly_based_greedy_res_2468.csv")
# CSV file for the basic greedy method ("greedy")
df_greedy = pd.read_csv("greedy_res_2468.csv")

# =============================================================================
# Graph 1: X-axis as Workers and Y-axis as Normal Worker Ratio
# =============================================================================

# Filter rows for x == 10 and tasks == 2000 so that only workers vary.
workers_filter_greedy = (df_greedy["x"] == 10) & (df_greedy["tasks"] == 2000)
df_greedy_workers = df_greedy[workers_filter_greedy].sort_values(by="workers")

workers_filter_outlier = (df_outlier["x"] == 10) & (df_outlier["tasks"] == 2000)
df_outlier_workers = df_outlier[workers_filter_outlier].sort_values(by="workers")

# Extract the workers values and the corresponding normal_worker_ratio metric.
workers_values = df_greedy_workers["workers"].values  # Assumes both DataFrames have matching workers.
greedy_nwr = df_greedy_workers["normal_worker_ratio"].values
outlier_nwr = df_outlier_workers["normal_worker_ratio"].values

# Set up the grouped bar chart.
x = np.arange(len(workers_values))  # positions on the x-axis
bar_width = 0.35  # width of each bar

fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - bar_width/2, greedy_nwr, bar_width, label="Greedy")
bars2 = ax.bar(x + bar_width/2, outlier_nwr, bar_width, label="Greedy+Outlier")

# Labeling and formatting.
ax.set_xlabel("Workers")
ax.set_ylabel("Normal Worker Ratio")
ax.set_title("Normal Worker Ratio vs. Workers (x=10, tasks=2000)")
ax.set_xticks(x)
ax.set_xticklabels(workers_values)
ax.legend()
ax.grid(True, axis="y")

plt.tight_layout()
plt.show()

# =============================================================================
# Graph 2: X-axis as Tasks and Y-axis as Normal Task Ratio
# =============================================================================

# Filter rows for x == 10 and workers == 2000 so that only tasks vary.
tasks_filter_greedy = (df_greedy["x"] == 10) & (df_greedy["workers"] == 2000)
df_greedy_tasks = df_greedy[tasks_filter_greedy].sort_values(by="tasks")

tasks_filter_outlier = (df_outlier["x"] == 10) & (df_outlier["workers"] == 2000)
df_outlier_tasks = df_outlier[tasks_filter_outlier].sort_values(by="tasks")

# Extract the tasks values and the corresponding normal_task_ratio metric.
tasks_values = df_greedy_tasks["tasks"].values  # Assumes both DataFrames have matching tasks.
greedy_ntr = df_greedy_tasks["normal_task_ratio"].values
outlier_ntr = df_outlier_tasks["normal_task_ratio"].values

# Set up the grouped bar chart for tasks.
x_tasks = np.arange(len(tasks_values))
bar_width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x_tasks - bar_width/2, greedy_ntr, bar_width, label="Greedy")
bars2 = ax.bar(x_tasks + bar_width/2, outlier_ntr, bar_width, label="Greedy+Outlier")

# Labeling and formatting.
ax.set_xlabel("Tasks")
ax.set_ylabel("Normal Task Ratio")
ax.set_title("Normal Task Ratio vs. Tasks (x=10, workers=2000)")
ax.set_xticks(x_tasks)
ax.set_xticklabels(tasks_values)
ax.legend()
ax.grid(True, axis="y")

plt.tight_layout()
plt.show()
