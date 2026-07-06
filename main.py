from core.engine import create_engine
from core.inference import extract_results

ocr = create_engine()

result = ocr.predict("input/morning quote2.jpg")

data = extract_results(result)

for item in data:
    print(item)