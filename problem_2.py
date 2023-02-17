import json
import csv


def generate_fixed_width_file(spec_path, output_file_path):
    with open(spec_path) as f:
        spec = json.load(f)
        offsets = [int(offset) for offset in spec["Offsets"]]

        with open(
            output_file_path, mode="w", encoding=spec["FixedWidthEncoding"]
        ) as file:
            for i, name in enumerate(spec["ColumnNames"]):
                if i > 0:
                    file.write(spec["DelimitedEncoding"] + ",")
                file.write(name)
            file.write("\n")

            with open("data.txt") as data_file:
                for line in data_file:
                    row = []
                    for offset in offsets:
                        row.append(line[:offset].strip())
                        line = line[offset:]
                    file.write(spec["DelimitedEncoding"].join(row) + "\n")


def convert_fixed_width_to_csv(input_file_path, output_file_path, spec):
    with open(input_file_path, "r", encoding="windows-1252") as fixed_width_file:
        with open(output_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)

            for line in fixed_width_file:
                fields = []
                spec_offsets = [int(offset) for offset in spec["Offsets"]]
                for i in range(len(spec_offsets)):
                    fields.append(line[: spec_offsets[i]].strip())
                    line = line[spec_offsets[i] :]
                writer.writerow(fields)
