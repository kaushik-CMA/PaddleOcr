from pathlib import Path

from core.inference import run_ocr
from core.exporter import export_txt, export_csv


class paddleOCRService:

    def __init__(self, engine):
        self.engine = engine

    def process_image(
        self,
        image_path: Path,
        txt_output: Path,
        csv_output: Path,
    ):
        """
        Process one image and export the results.
        """

        records = run_ocr(
            self.engine,
            image_path,
        )

        export_txt(
            records,
            txt_output,
        )

        export_csv(
            records,
            csv_output,
        )

        return {
            "filename": image_path.name,
            "records": records,
            "count": len(records),
        }