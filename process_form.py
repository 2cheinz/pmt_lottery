#!/usr/bin/env python3

import cgi
import csv

# Get the form data
form = cgi.FieldStorage()
user_number = form.getvalue('user_number')

# Write the form data to a CSV file
with open('user_numbers.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([user_number])

# Print a success message
print('Content-Type: text/html')
print()
print('<html><body>')
print('<h1>Thanks for submitting!</h1>')
print('</body></html>')
