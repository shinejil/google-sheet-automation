#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import gspread
import pandas as pd



cred_file="tolet-388713-348dde0333b8.json"
gc=gspread.service_account(cred_file)
gc

spreadsheet=gc.open("rental_properties")


sheet=spreadsheet.worksheet('MainSheet')


data = pd.DataFrame(sheet.get_all_records())

for index, property_data in data.iterrows():
    places = property_data['place']
    try:
        # Check if a sub-sheet with the place name already exists
        sub_sheet = spreadsheet.worksheet(places)
         # Get the headers and data values
        values = property_data.tolist()
        existing_values = sub_sheet.get_all_values()
        if values not in existing_values:
            # Append the headers and values to the sub-shee
            sub_sheet.append_row(values)
    except gspread.WorksheetNotFound:
        # If the sub-sheet doesn't exist, create a new one
        sub_sheet = spreadsheet.add_worksheet(title=places, rows="100", cols="20")
        headers = property_data.index.tolist()
        values = property_data.tolist()

        # Append the headers and values to the sub-sheet
        sub_sheet.append_row(headers)
        sub_sheet.append_row(values)
        #print(values)
        print("Data has been copied to  new sub-sheets successfully.")
   

print("Data has been copied to sub-sheets successfully.")

