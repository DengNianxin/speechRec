import os
from tensorflow.keras.optimizers import Adam

from speech_model import ModelSpeech
from models.DCNN import DCNN
from data_loader import DataLoader
from speech_features import SpecAugment

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

AUDIO_LENGTH = 900
AUDIO_FEATURE_LENGTH = 200
CHANNELS = 1
OUTPUT_SIZE = 1174

dcnn = DCNN(
    input_shape=(AUDIO_LENGTH, AUDIO_FEATURE_LENGTH, CHANNELS),
    output_size=OUTPUT_SIZE
)
feat = SpecAugment() # 数据增强
train_data = DataLoader('train') # 加载数据
opt = Adam(learning_rate=0.0001, beta_1=0.9, beta_2=0.999, decay=0.0, epsilon=10e-8) # 优化器
ms = ModelSpeech(dcnn, feat, max_label_length=64)

ms.train_model(optimizer=opt, data_loader=train_data,
               epochs=1, save_step=1, batch_size=4 , last_epoch=0)
ms.save_model('save_models/' + dcnn.get_model_name())
