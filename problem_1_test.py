import csv
import unittest

from problem_1 import anonymize_customer_data


class TestAnonymizeCustomerData(unittest.TestCase):
    def test_anonymize_customer_data(self):
        input_file = "customer_data.csv"
        output_file = "required_columns.csv"

        anonymize_customer_data(input_file, output_file)

        with open(output_file, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            required_columns_data = list(csv_reader)

        with open("anonymized_data.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            anonymized_data = list(csv_reader)

        # check if the columns are properly anonymized based on fields in output_file
        for idx, customer in enumerate(anonymized_data):
            self.assertEqual(customer["first_name"], "***")
            self.assertEqual(customer["last_name"], "***")
            self.assertEqual(customer["address"], "***")

            # check birth date is same as in input file
            self.assertEqual(
                customer["date_of_birth"], required_columns_data[idx]["date_of_birth"]
            )


if __name__ == "__main__":
    unittest.main()
