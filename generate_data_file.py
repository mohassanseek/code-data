import json

spec_path = "spec.json"
data = [
    [
        "John",
        "Smith",
        "100",
        "01",
        "123-45-6789",
        "1970-01-01",
        "ABC",
        "123-45-6789-12345",
        "test@example.com",
        "111-111-1111",
    ],
    [
        "Jane",
        "Doe",
        "200",
        "02",
        "987-65-4321",
        "1980-01-01",
        "DEF",
        "987-65-4321-54321",
        "example@test.com",
        "222-222-2222",
    ],
    [
        "Bob",
        "Johnson",
        "300",
        "03",
        "456-78-9123",
        "1990-01-01",
        "GHI",
        "456-78-9123-12345",
        "test@example.com",
        "333-333-3333",
    ],
]

with open(spec_path) as f:
    spec = json.load(f)
    offsets = [int(offset) for offset in spec["Offsets"]]

    with open("data.txt", mode="w", encoding=spec["FixedWidthEncoding"]) as file:
        for row in data:
            for i in range(len(row)):
                value = row[i]
                offset = offsets[i]
                fixed_width_value = value.ljust(offset)
                file.write(fixed_width_value)
            file.write("\n")
