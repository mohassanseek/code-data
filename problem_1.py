import csv


def anonymize_customer_data(input_file, output_file):
    # Open input CSV file and read the data
    with open(input_file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        customer_data = list(csv_reader)

    # Write the data with only required columns to a new CSV file
    with open(output_file, "w", newline="") as csv_file:
        fieldnames = ["first_name", "last_name", "address", "date_of_birth"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for customer in customer_data:
            csv_writer.writerow(customer)

    # Open the anonymized data CSV file and overwrite the first name, last name and address columns with '***'
    with open(output_file, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        anonymized_data = list(csv_reader)

    for customer in anonymized_data:
        customer["first_name"] = "***"
        customer["last_name"] = "***"
        customer["address"] = "***"

    # Write the anonymized data to a new CSV file
    with open("anonymized_data.csv", "w", newline="") as csv_file:
        fieldnames = ["first_name", "last_name", "address", "date_of_birth"]
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for customer in anonymized_data:
            csv_writer.writerow(customer)
