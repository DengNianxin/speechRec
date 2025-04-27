import os
from speech_model import ModelSpeech
from models.DCNN import DCNN
from data_loader import DataLoader
from speech_features import Spectrogram

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

AUDIO_LENGTH = 900
AUDIO_FEATURE_LENGTH = 200
CHANNELS = 1
OUTPUT_SIZE = 1087

dcnn = DCNN(
    input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
    output_size=OUTPUT_SIZE
)
feat = Spectrogram()
evalue_data = DataLoader('dev')
ms = ModelSpeech(dcnn, feat, max_label_length=64)

ms.load_model('save_models/save_models3/' + dcnn.get_model_name() + '.model.h5')
ms.evaluate_model(data_loader=evalue_data, data_count=-1,
                  out_report=True, show_ratio=True, show_per_step=100)
