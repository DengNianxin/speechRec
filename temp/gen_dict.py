import re
import pypinyin
from pypinyin import pinyin, Style

# 输入文件路径
uttrans_info_file = 'data_cy_dialect11/UTTRANSINFO.txt'
train_file = 'data_cy_dialect12/train.txt'
dev_file = 'data_cy_dialect12/dev.txt'
# 输出字典文件路径
output_dict_file = 'syllabel_dict.txt'

# 定义一个函数，用于去除字母、数字、【】内的内容和标点符号，仅保留汉字
def clean_text(text):
    # 去除字母和数字
    text = re.sub(r'[a-zA-Z0-9]', '', text)
    # 去除【】内的内容
    text = re.sub(r'【.*?】', '', text)
    # 去除标点符号
    text = re.sub(r'[^\u4e00-\u9fa5]', '', text)
    return text

# 定义一个函数，将汉字转换为拼音
def text_to_pinyin(text):
    # 使用 pypinyin 转换为拼音
    pinyin_list = pinyin(text, style=Style.TONE3, heteronym=False)

    # 处理轻声和连续的“了”
    processed_pinyin_list = []
    i = 0
    while i < len(pinyin_list):
        item = pinyin_list[i]
        # 检查是否为轻声
        if not re.search(r'[0-5]$', item[0]):
            processed_pinyin_list.append(item[0] + '5')
        else:
            processed_pinyin_list.append(item[0])

        # 处理连续的“了”
        if i < len(pinyin_list) - 1 and text[i] == '了' and text[i + 1] == '了':
            processed_pinyin_list[-1] = 'liao3'
            processed_pinyin_list.append('le5')
            i += 1  # 跳过下一个“了”
        i += 1

    # 将拼音列表转换为字符串
    pinyin_str = ' '.join(processed_pinyin_list)
    return pinyin_str

# 创建一个字典来存储拼音和对应的汉字
syllable_dict = {}

# 处理 UTTRANSINFO.txt 文件
with open(uttrans_info_file, 'r', encoding='utf-8') as infile:
    # 跳过第一行（标题行）
    next(infile)

    # 遍历每一行
    for line in infile:
        # 去除行首行尾的空白字符并按制表符分割
        columns = line.strip().split('\t')
        if len(columns) < 5:
            continue  # 跳过格式不正确的行

        # 获取最后一列（TRANSCRIPTION）
        transcription = columns[4]

        # 清洗文本，仅保留汉字
        cleaned_text = clean_text(transcription)

        # 将汉字转换为拼音
        pinyin_text = text_to_pinyin(cleaned_text)

        # 更新拼音字典
        pinyin_list = pinyin_text.split()
        for char, syllable in zip(cleaned_text, pinyin_list):
            if syllable not in syllable_dict:
                syllable_dict[syllable] = set()
            syllable_dict[syllable].add(char)

# 处理 train.txt 和 dev.txt 文件
for file_path in [train_file, dev_file]:
    with open(file_path, 'r', encoding='utf-8') as infile:
        # 遍历每一行
        for line in infile:
            # 去除行首行尾的空白字符并按制表符分割
            columns = line.strip().split('\t')
            if len(columns) < 2:
                continue  # 跳过格式不正确的行

            # 获取最后一列（文本内容）
            transcription = columns[1]

            # 清洗文本，仅保留汉字
            cleaned_text = clean_text(transcription)

            # 将汉字转换为拼音
            pinyin_text = text_to_pinyin(cleaned_text)

            # 更新拼音字典
            pinyin_list = pinyin_text.split()
            for char, syllable in zip(cleaned_text, pinyin_list):
                if syllable not in syllable_dict:
                    syllable_dict[syllable] = set()
                syllable_dict[syllable].add(char)

# 将拼音字典写入文件
with open(output_dict_file, 'w', encoding='utf-8') as dictfile:
    for syllable in sorted(syllable_dict):
        characters = ''.join(sorted(syllable_dict[syllable]))  # 汉字用制表符分隔
        dictfile.write(f"{syllable}\t{characters}\n")

print(f"生成的拼音字典已保存到 {output_dict_file}")