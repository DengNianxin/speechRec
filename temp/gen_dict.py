# 输入文件路径
input_file = 'data.syllabel.txt'  # 假设文件名为 train.syllabel.txt

# 输出字典文件路径
output_dict_file = 'syllable_dict.txt'  # 输出的拼音字典文件

# 打开输入文件和输出文件
with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_dict_file, 'w', encoding='utf-8') as outfile:
    # 创建一个集合来存储唯一的拼音
    syllable_set = set()

    # 遍历每一行
    for line in infile:
        # 去除行首行尾的空白字符并按制表符分割
        parts = line.strip().split(' ')
        parts = parts[1:]
        if len(parts) < 2:
            continue  # 跳过格式不正确的行

        # 提取拼音部分
        syllable_set.update(parts)

    # 将拼音字典写入文件
    for syllable in sorted(syllable_set):
        outfile.write(syllable + '\n')

print(f"生成的拼音字典已保存到 {output_dict_file}")