from pathlib import Path


def export_txt(records, output_file):

    output_path = Path(output_file)

    with output_path.open("w", encoding="utf-8") as file:

        for record in records:
            file.write(record.text + "\n")