import matplotlib.pyplot as plt
import pandas as pd
import zipfile
import os

# Correct path to the uploaded ZIP file
zip_filename = 'all_flights.zip'  # Make sure the file is in the same directory
extracted_dir = 'extracted_flights'

# Step 1: Extract all CSV files from the ZIP archive
if not os.path.exists(extracted_dir):
    os.makedirs(extracted_dir)

with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
    zip_ref.extractall(extracted_dir)

# Step 2: Read all CSV files and plot bird height against frame number
csv_files = [f for f in os.listdir(extracted_dir) if f.endswith(".csv")]

plt.figure(figsize=(10, 6))
for file in csv_files:
    file_path = os.path.join(extracted_dir, file)
    df = pd.read_csv(file_path)
    plt.plot(df['frame'], df['y'], label=file.split(".csv")[0])

# Step 3: Customize the graph
plt.title("Bird Height Over Time Across Multiple Flights")
plt.xlabel("Frame Number")
plt.ylabel("Bird Height (y)")
plt.legend(title="Flight")
plt.grid()
plt.show()