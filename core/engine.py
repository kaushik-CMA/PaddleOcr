from paddleocr import PaddleOCR
from config.settings import *


def create_engine():
    return PaddleOCR(
    enable_mkldnn=ENABLE_MKLDNN,
    use_doc_orientation_classify=USE_DOC_ORIENTATION,
    use_doc_unwarping=USE_DOC_UNWARPING,
    use_textline_orientation=USE_TEXTLINE_ORIENTATION,
)