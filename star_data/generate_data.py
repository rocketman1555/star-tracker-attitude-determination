import pandas as pd

# Load data from the Hipparcos csv file
file_path = 'star_data\\archive\\hipparcos-voidmain.csv'
df = pd.read_csv(file_path)

# Filter the columns to only include Declination (deg.), Right Ascension (deg.), and Magnitude (Johnson System)
columns_of_interest = ['RAdeg', 'DEdeg', 'Vmag']
filtered_df = df[columns_of_interest]

# Randomly sample the dataset to contain n_samples entries
n_samples = 1500    # n samples
rs = 55             # random seed, keep it the same for reproducibility
sampled_df = filtered_df.sample(n = n_samples, random_state = rs)

# Output the sub-samples data to a csv
output_filename = f"star_data\\subarchives\\hipparcos-voidman_subsample_n{n_samples}_seed{rs}.csv"
sampled_df.to_csv(output_filename, index=False)

# Print the first few rows of the subsample as a sanity check
print(sampled_df.head())
