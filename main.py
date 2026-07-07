from core.engine import create_engine
from core.inference import extract_results
from core.exporter import export_txt

ocr = create_engine()

result = ocr.predict("input/morning quote2.jpg")

records = extract_results(result)

for record in records:
    print(record)

export_txt(records, "output/result.txt")