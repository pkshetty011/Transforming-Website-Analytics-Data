import pandas as pd

# Read the input_refresh_template sheet
df = pd.read_excel('Insert Path Here/Analytics Template for Exercise.xlsx', sheet_name='input_refresh_template')

# Group the data by site
grouped = df.groupby('Site')

# Initialize an empty list to store the output data
output_data = []

# Loop through each site in the grouped data
for site, data in grouped:
    # Calculate the metrics for the site
    page_views = data['Page Views'].sum()
    unique_visitors = data['Unique Visitors'].sum()
    total_time_spent = data['Total Time Spent'].sum()
    visits = data['Visits'].sum()
    avg_time_spent = data['Average Time Spent on Site'].mean()

    # Get the start and end dates from the input data
    start_date = data.iloc[0]['Start Date']
    end_date = data.iloc[0]['End Date']

    # Create a dictionary to store the output data for the site
    site_data = {
        'Site': site,
        'Start Date': start_date,
        'End Date': end_date,
        'Page Views': page_views,
        'Unique Visitors': unique_visitors,
        'Total Time Spent': total_time_spent,
        'Visits': visits,
        'Average Time Spent on Site': avg_time_spent
    }

    # Append the site data to the output data list
    output_data.append(site_data)

# Create a DataFrame from the output data
output_df = pd.DataFrame(output_data)

# Write the output to a new Excel file
output_df.to_excel('output.xlsx', sheet_name='output_31_days_report', index=False)
