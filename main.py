from core.engine import create_engine
from core.inference import run_ocr
from core.exporter import (export_txt,export_csv)
from config.settings import (INPUT_IMAGE, OUTPUT_TXT, OUTPUT_CSV)

ocr = create_engine()

records = run_ocr(ocr, INPUT_IMAGE)

export_txt(records, OUTPUT_TXT)

export_csv(records,OUTPUT_CSV)

print("Done")