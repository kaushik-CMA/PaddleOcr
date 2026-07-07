from pathlib import Path

from config.settings import (
    INPUT_FOLDER,
    OUTPUT_FOLDER
)

from core.engine import create_engine
from core.inference import run_ocr
from core.exporter import export_txt
from core.exporter import export_csv
from core.file_utils import get_images


ocr = create_engine()

images = get_images(INPUT_FOLDER)

for image in images:

    records = run_ocr(
        ocr,
        image
    )

    txt_file = (
        Path(OUTPUT_FOLDER)
        / f"{image.stem}.txt"
    )

    csv_file = (
        Path(OUTPUT_FOLDER)
        / f"{image.stem}.csv"
    )

    export_txt(records, txt_file)

    export_csv(records, csv_file)

    print(f"Processed: {image.name}")

print("Done")