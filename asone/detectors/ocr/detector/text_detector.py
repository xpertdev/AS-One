import easyocr
import numpy as np


class TextDetector:
    def __init__(self, use_cuda=True):
        self.use_cuda = use_cuda

    def detect(self, image: list, filter_classes=None) -> list:
        reader = easyocr.Reader(['en'], gpu=self.use_cuda)
        extracted_text = reader.readtext(image)
        img_info = {"widh" : image.shape[0], "height" : image.shape[1]}
        
        if extracted_text == []:
            return np.empty((0, 6)), img_info
        filtered_text = []
        for text in extracted_text:
            filtered_text.append([text[0][0][0], text[0][0][1], text[0][2][0], text[0][2][1], text[2], 80])
        return np.array(filtered_text), img_info