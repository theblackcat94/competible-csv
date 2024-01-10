# CSV Validation for Pet Records

This Python script is designed to validate CSV files containing pet records. It ensures the integrity of data related to pet listings for adoption.

## Features

- Validates date formats in the 'Birthday' field.
- Checks for alphabetical and space characters in 'Name', 'Gender', and 'Species' fields.
- Confirms that breeds are from a predefined list and checks for valid characters in the 'Breed' field.
- Validates 'Species' and 'Gender' fields for acceptable values.
- Ensures boolean fields 'Pure Breed', 'Mixed Breed', 'Desexed', and 'Microchipped' contain either TRUE or FALSE.
- Checks for consistency between 'Pure Breed' and 'Mixed Breed' fields.
- Attempts to download and validate images from URLs provided in the 'Photo/Icon' field.
- Validates 'Listing Type' to ensure it matches "For Adoption".
- Limits the 'Description' field to 200 words.
- Ensures 'Price' is a whole number and does not exceed 1000.
- Validates 'Location' to ensure it is a full, non-empty address string.

## Usage

Before running the script, ensure that the following Python libraries are installed:
- `pandas`
- `requests`
