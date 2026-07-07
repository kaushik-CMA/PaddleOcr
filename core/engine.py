from paddleocr import PaddleOCR


def create_engine():
    return PaddleOCR(
        enable_mkldnn=False,
        use_doc_orientation_classify=False,
        use_doc_unwarping=False,
        use_textline_orientation=False,
    )