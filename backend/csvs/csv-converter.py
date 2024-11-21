import csv
import os

# This script is used to convert the FAA Airports database found at https://adds-faa.opendata.arcgis.com/datasets/faa::airports-1/explore 
# into a format we can use with our existing GeoUtilities

# Get the directory of the script
script_dir = os.path.dirname(__file__)

# Construct file paths relative to the script directory
input_file = os.path.join(script_dir, 'Airports.csv')
output_file = os.path.join(script_dir, 'output.csv')

# Function to transform the input data
def transform_csv(input_file, output_file):
    with open(input_file, mode='r', encoding='utf-8-sig') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ['iata', 'icao', 'faa', 'latitude', 'longitude']  # Desired output columns
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        # Write the header for the output CSV
        writer.writeheader()
        
        # Iterate through rows in the input CSV
        for row in reader:
            # Extract latitude and longitude
            latitude = row.get('Y', '').strip()  # Latitude from Y column
            longitude = row.get('X', '').strip()  # Longitude from X column
            
            # Extract airport identifiers
            ident = row.get('IDENT', '').strip()  # Identifier (could be IATA or FAA)
            icao_id = row.get('ICAO_ID', '').strip()  # ICAO code

            iata = ''  # Default IATA code
            faa = ''   # Default FAA code
            icao = ''  # Default ICAO code

            # Check if IDENT is IATA
            if len(ident) == 3 and ident.isalpha():  # Check if IDENT is all letters and 3 characters
                iata = ident  # Assign as IATA code
            else:
                faa = ident  # Assign as FAA code

            # Assign ICAO if valid
            if len(icao_id) == 4:  # ICAO codes are always 4 characters
                icao = icao_id

            transformed_row = {
                'iata': iata,  
                'icao': icao,  
                'faa': faa,  
                'latitude': latitude,  
                'longitude': longitude 
            }
            
            # Write the transformed row to the output CSV
            writer.writerow(transformed_row)

# Call the function to transform the data
if __name__ == "__main__":
    transform_csv(input_file, output_file)
    print(f"Transformed data has been saved to {output_file}")
