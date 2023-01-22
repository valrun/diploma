from doctr.models import ocr_predictor
from doctr.io import DocumentFile

doctr_ocr = ocr_predictor(det_arch='db_resnet50', reco_arch='crnn_vgg16_bn', pretrained=True)