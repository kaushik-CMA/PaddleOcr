from pathlib import Path

from config.settings import (
    INPUT_FOLDER,
    OUTPUT_FOLDER,
)

from core.engine import create_engine
from core.file_utils import get_images
from core.ocr_service import paddleOCRService


engine = create_engine()

service = paddleOCRService(engine)

images = get_images(INPUT_FOLDER)

for image in images:

    txt_output = (
        Path(OUTPUT_FOLDER)
        / f"{image.stem}.txt"
    )

    csv_output = (
        Path(OUTPUT_FOLDER)
        / f"{image.stem}.csv"
    )

    service.process_image(
        image,
        txt_output,
        csv_output,
    )

    print(f"Processed {image.name}")

print("Done")