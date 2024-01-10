import pandas as pd
import requests
from datetime import datetime
import os

breed_list = [
    "Persian", "Maine Coon", "Ragdoll", "Siamese", "British Shorthair",
    "Labrador Retriever", "German Shepherd", "Golden Retriever", "French Bulldog", "Bulldog"
]

#need to expand to handle (1) all dog/cat breeds, and (2) cat_breed_list and dog_breed_list and ensure if dog selected, only dog breeds, and cat selected, only cat beeds etc. 

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False

def is_valid_name(string):
    return all(x.isalpha() or x.isspace() for x in string)

def download_image(url, download_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(download_path, 'wb') as file:
                file.write(response.content)
            return True
        else:
            return False
    except:
        return False

def validate_csv_and_save_errors_txt(file_path, error_file_path):
    errors = []

    try:
        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            row_errors = []

            #Date format validation
            if not pd.isna(row['Birthday']) and not is_valid_date(row['Birthday']):
                row_errors.append("Invalid date format in 'Birthday'.")

            #Alphabet characters validation
            for field in ['Name', 'Gender', 'Species']:
                if not pd.isna(row[field]) and not is_valid_name(row[field]):
                    row_errors.append(f"Field '{field}' should contain only alphabet characters and spaces.")

            #Breed validation
            if not pd.isna(row['Breed']) and (row['Breed'] not in breed_list or not is_valid_name(row['Breed'])):
                row_errors.append("Breed not recognised or invalid characters.")

            #Species and Gender validation
            if row['Species'] not in ['Dog', 'Cat']:
                row_errors.append("Species must be either 'Dog' or 'Cat'.")
            if row['Gender'] not in ['Male', 'Female']:
                row_errors.append("Gender must be either 'Male' or 'Female'.")

            #Boolean fields validation
            for field in ['Pure Breed', 'Mixed Breed', 'Desexed', 'Microchipped']:
                if row[field] not in [True, False]:
                    row_errors.append(f"Field '{field}' must be either TRUE or FALSE.")

            #Pure Breed and Mixed Breed consistency check
            if row['Pure Breed'] == row['Mixed Breed']:
                row_errors.append("Pure Breed and Mixed Breed cannot be both true or both false.")

            #Photo/Icon URL download and validation
            if not pd.isna(row['Photo/Icon']):
                download_path = f"C:\\PYTHONPROGRAMS\\DRAFT\\COMPETIBLE\\CSV_UPLOAD\\row_{index+1}.jpg"
                if not download_image(row['Photo/Icon'], download_path):
                    row_errors.append(f"Failed to download or access image from URL in 'Photo/Icon'.")

            if row_errors:
                errors.append(f"Row {index + 1}: " + "; ".join(row_errors))
    
    except Exception as e:
        errors.append(f"Error: {str(e)}")

    #Saving errors to a text file
    if errors:
        with open(error_file_path, 'w') as file:
            for error in errors:
                file.write(error + "\n\n")

    return errors

#File path for validation and error file path
file_path = "C:\\PYTHONPROGRAMS\\DRAFT\\COMPETIBLE\\CSV_UPLOAD\\pet_records_template.csv"
error_file_path = "C:\\PYTHONPROGRAMS\\DRAFT\\COMPETIBLE\\CSV_UPLOAD\\validation_errors.txt"

#Validate the CSV file and save errors to a text file
validation_errors_v2 = validate_csv_and_save_errors_txt(file_path, error_file_path)

#If you want to print the errors
print(validation_errors_v2)
