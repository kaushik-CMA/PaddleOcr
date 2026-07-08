from pathlib import Path
from core.models import OCRRecord
from config.settings import *


def get_first_image(input_folder):
    
    # Return the first supported image found in the input folder.

    supported_extensions = {
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp",
        ".tif",
        ".tiff",
        ".webp"
    }

    input_path = Path(input_folder)

    for file in input_path.iterdir():
        if file.suffix.lower() in supported_extensions:
            return file

    raise FileNotFoundError("No supported image found in input folder.")


def run_ocr(ocr, image_path):
    # Run PaddleOCR on an image.

    result = ocr.predict(str(image_path))
    return extract_results(result)

def extract_results(result):
    
    # Convert PaddleOCR output into a simple Python list.

    page = result[0]

    records = []

    for text, score, box in zip(
        page["rec_texts"],
        page["rec_scores"],
        page["rec_boxes"]
    ):
        if score>= MIN_CONFIDENCE:
            records.append(
                OCRRecord(text=text,
                        confidence=float(score),
                        box=box.tolist())
            )

    return records