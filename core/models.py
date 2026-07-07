from dataclasses import dataclass


@dataclass
class OCRRecord:
    text: str
    confidence: float
    box: list[int]