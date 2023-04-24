# Transforming-Website-Analytics-Data
Converting Wide Format to Long Format"

This code reads in a CSV file containing data on website page views and unique visitors for each day of the month, and then transforms the data into a new format.

The original data is in a wide format where each date is represented by a separate column. The transformed data is in a long format, where each row represents a single observation (page view, unique visitor, etc.) for a particular date and website.

The code achieves this transformation by using the pandas melt function to unpivot the data from the original wide format to a long format, and then performing some additional data cleaning and manipulation to get it into the desired format. The resulting long format data is then saved to a new CSV file.

