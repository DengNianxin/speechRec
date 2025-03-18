import re
import pypinyin
from pypinyin import pinyin, Style

# 输入文件路径
input_file = 'UTTRANSINFO.txt'
# 输出文件路径
output_file = 'data.syllabel.txt'


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


# 打开输入文件和输出文件
with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8') as outfile:
    # 跳过第一行（标题行）
    next(infile)

    # 遍历每一行
    for line in infile:
        # 去除行首行尾的空白字符并按制表符分割
        columns = line.strip().split('\t')
        if len(columns) < 4:
            continue  # 跳过格式不正确的行

        # 获取第二列（UTTRANS_ID）和第四列（TRANSCRIPTION）
        uttrans_id = columns[1].split(".")[0]
        transcription = columns[4]

        # 清洗文本，仅保留汉字
        cleaned_text = clean_text(transcription)

        # 将汉字转换为拼音
        pinyin_text = text_to_pinyin(cleaned_text)

        # 写入输出文件
        outfile.write(f"{uttrans_id} {pinyin_text}\n")

print(f"生成的文件已保存到 {output_file}")