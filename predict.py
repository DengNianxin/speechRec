import os

from speech_model import ModelSpeech
from models.DCNN import DCNN
from speech_features import Spectrogram
from N_gram import ModelLanguage

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

AUDIO_LENGTH = 1600
AUDIO_FEATURE_LENGTH = 200
CHANNELS = 1
OUTPUT_SIZE = 1024

dcnn = DCNN(
    input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
    output_size=OUTPUT_SIZE
)
feat = Spectrogram()
ms = ModelSpeech(dcnn, feat, max_label_length=64)

ms.load_model('save_models/asrt_models/SpeechModel251bn.model.h5')
res = ms.recognize_speech_from_file('predict_file/SP1_0102.wav')
print('*[提示] 声学模型语音识别结果：\n', res)

ml = ModelLanguage('')
ml.load_model()
str_pinyin = res
res = ml.pinyin_to_text(str_pinyin)
print('语音识别最终结果：\n', res)
