from pathlib import Path
import csv


def export_txt(records, output_file):

    output_path = Path(output_file)

    with output_path.open("w", encoding="utf-8") as file:

        for record in records:
            file.write(record.text + "\n")

            


def export_csv(records, output_file):

    output_path = Path(output_file)

    with output_path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Text",
                "Confidence",
                "Box"
            ]
        )

        for record in records:

            writer.writerow(
                [
                    record.text,
                    record.confidence,
                    record.box
                ]
            )