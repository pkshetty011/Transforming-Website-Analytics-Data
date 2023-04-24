import unittest
import pandas as pd

class TestOutputData(unittest.TestCase):
    
    def setUp(self):
        # Read the input_refresh_template sheet
        self.df = pd.read_excel('Insert Path Here/Analytics Template for Exercise.xlsx')

        # Group the data by site
        self.grouped = self.df.groupby('Site')
        
        # Initialize an empty list to store the output data
        self.output_data = []

        # Loop through each site in the grouped data
        for site, data in self.grouped:
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
            self.output_data.append(site_data)

        # Create a DataFrame from the output data
        self.output_df = pd.DataFrame(self.output_data)
        
    def test_output_df_shape(self):
        self.assertEqual(self.output_df.shape, (3, 8))
        
    def test_output_df_columns(self):
        self.assertCountEqual(list(self.output_df.columns), ['Site', 'Start Date', 'End Date', 'Page Views', 'Unique Visitors', 'Total Time Spent', 'Visits', 'Average Time Spent on Site'])
        
    def test_output_df_datatypes(self):
        self.assertTrue(all(self.output_df.dtypes == 'int64') or all(self.output_df.dtypes == 'float64'))
        self.assertTrue(self.output_df['Site'].dtype == 'object')
        self.assertTrue(self.output_df['Start Date'].dtype == 'datetime64[ns]')
        self.assertTrue(self.output_df['End Date'].dtype == 'datetime64[ns]')
        
    def test_output_df_values(self):
        self.assertEqual(self.output_df.iloc[0]['Site'], 'Site 1')
        self.assertEqual(self.output_df.iloc[0]['Page Views'], 980)
        self.assertEqual(self.output_df.iloc[0]['Unique Visitors'], 340)
        self.assertEqual(self.output_df.iloc[0]['Total Time Spent'], 4321)
        self.assertEqual(self.output_df.iloc[0]['Visits'], 332)
        self.assertAlmostEqual(self.output_df.iloc[0]['Average Time Spent on Site'], 14.98, places=2)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
