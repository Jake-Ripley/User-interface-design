import matplotlib.pyplot as plt

# Function to convert time strings to seconds
def time_to_seconds(time_str):
    minutes, seconds = 0, 0
    if 'm' in time_str:
        parts = time_str.split('m')
        minutes = int(parts[0]) if parts[0] else 0
        seconds = int(parts[1].replace('s', '')) if parts[1] else 0
    else:
        seconds = int(time_str.replace('s', ''))
    return minutes * 60 + seconds

# Data from the image
data = {
    "JC": ["44s", "11s", "35s", "1m 8s", "1m 45s", "2m 8s", "32s", "35s", "41s", "29s"],
    "JM": ["40s", "10s", "30s", "57s", "1m", "1m 30s", "25s", "33s", "32s", "35s"],
    "AO": ["32s", "8s", "10s", "51s", "36s", "1m 2s", "23s", "31s", "40s", "27s"],
    "KJ": ["1m 32s", "23s", "55s", "1m 19s", "1m 30s", "2m 59s", "42s", "50s", "58s", "45s"],
    "ZW": ["1m 2s", "15s", "46s", "1m 10s", "1m 7s", "2m 13s", "37s", "46s", "45s", "42s"]
}

# Convert all times to seconds
converted_data = {participant: [time_to_seconds(time) for time in times] for participant, times in data.items()}

# Transpose data to get times per task across all participants
task_times = list(zip(*converted_data.values()))

# Calculate mean and standard deviation for each task
task_statistics = []
for task in task_times:
    mean_time = sum(task) / len(task)
    std_dev = (sum((time - mean_time) ** 2 for time in task) / len(task)) ** 0.5
    task_statistics.append((mean_time, std_dev))

# Output the results for each task
task_labels = ["Create Account", "Log in", "Manage Access", "App Tutorial", "Manage Insurance", 
               "Manage Medical", "Book Appointment", "Refill Prescription", "Pay Bills", "Access Consultation"]

# Create lists for means and standard deviations for plotting
means = [stat[0] for stat in task_statistics]
std_devs = [stat[1] for stat in task_statistics]

# Plotting the data
plt.figure(figsize=(14, 7))

# Plot means with standard deviation error bars
plt.errorbar(task_labels, means, yerr=std_devs, fmt='o', capsize=5, linestyle='-', ecolor='red', color='blue', label='Mean Times')

# Adding labels and title
plt.xlabel('Tasks')
plt.ylabel('Time to Complete (seconds)')
plt.title('Mean Time to Complete Tasks with Standard Deviation')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()  # Adjusts plot to ensure everything fits without overlap
plt.grid(True)

# Show the plot
plt.show()

# Print the mean and standard deviation for each task
for i, (mean, std) in enumerate(task_statistics):
    print(f"Task '{task_labels[i]}': Mean Time = {mean} seconds, Standard Deviation = {std}")
