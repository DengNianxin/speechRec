import re
import pypinyin
from pypinyin import pinyin, Style

# 输入文件路径
input_file = 'list_dev_processed.txt'
# 输出文件路径
output_file = 'dev.syllabel2.txt'

# 定义一个函数，用于去除非汉字字符
def clean_text(text):
    # 仅保留汉字
    text = re.sub(r'[^\u4e00-\u9fff]', '', text)
    return text

# 定义一个函数，将汉字转换为拼音
def text_to_pinyin(text):
    # 使用 pypinyin 转换为拼音
    pinyin_list = pinyin(text, style=Style.TONE3, heteronym=False)

    # 处理轻声和连续的“了”
    processed_pinyin_list = []
    for item in pinyin_list:
        # 检查是否为轻声
        if not re.search(r'[0-5]$', item[0]):
            processed_pinyin_list.append(item[0] + '5')  # 轻声标记为5
        else:
            processed_pinyin_list.append(item[0])

    # 将拼音列表转换为字符串
    pinyin_str = ' '.join(processed_pinyin_list)
    return pinyin_str

# 打开输入文件和输出文件
with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8') as outfile:

    # 遍历每一行
    for line in infile:
        # 去除行首行尾的空白字符并按制表符分割
        columns = line.strip().split('\t')
        if len(columns) < 2:
            continue  # 跳过格式不正确的行

        file_path = columns[0]
        transcription = columns[1]

        # 提取编号
        match = re.search(r'SCC(\d+)', file_path)
        if match:
            id = match.group(0)  # 提取完整的编号，包括前缀
            # 构造新的编号格式
            uttrans_id = id

            # 清洗文本，仅保留汉字
            cleaned_text = clean_text(transcription)

            # 将汉字转换为拼音
            pinyin_text = text_to_pinyin(cleaned_text)

            # 写入拼音文件
            outfile.write(f"{uttrans_id} {pinyin_text}\n")

print(f"生成的拼音文件已保存到 {output_file}")