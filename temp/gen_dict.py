import re

# 输入文件路径列表
input_files = ['train.syllabel.txt', 'dev.syllabel.txt', 'train.syllabel2.txt', 'dev.syllabel2.txt']
# 输出字典文件路径
output_dict_file = 'syllabel_dict.txt'

# 创建一个集合来存储所有拼音
syllable_set = set()

# 遍历每个输入文件
for input_file in input_files:
    with open(input_file, 'r', encoding='utf-8') as infile:
        # 遍历每一行
        for line in infile:
            # 去除行首行尾的空白字符并按制表符分割
            columns = line.strip().split()
            if len(columns) < 2:
                continue  # 跳过格式不正确的行

            # 提取拼音部分
            pinyin_part = ' '.join(columns[1:])  # 从第二个元素开始的所有内容
            # 使用正则表达式提取所有拼音
            pinyin_list = re.findall(r'\b\w+\d+\b', pinyin_part)
            # 将拼音添加到集合中
            syllable_set.update(pinyin_list)

# 将拼音字典写入文件
with open(output_dict_file, 'w', encoding='utf-8') as dictfile:
    # 按拼音排序
    for syllable in sorted(syllable_set):
        dictfile.write(f"{syllable}\n")

print(f"生成的拼音字典已保存到 {output_dict_file}")