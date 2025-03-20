import os

# 输入文件路径
input_file = 'UTTRANSINFO.txt'  # 假设数据存储在 data.csv 文件中
# 输出文件路径
output_file = 'data.wav.lst'


# 打开输入文件和输出文件
with open(input_file, 'r', encoding='utf-8') as infile, \
        open(output_file, 'w', encoding='utf-8') as outfile:
    # 跳过第一行（标题行）
    next(infile)

    # 遍历每一行
    for line in infile:
        # 去除行首行尾的空白字符并按制表符分割
        columns = line.strip().split('\t')
        if len(columns) < 2:
            continue  # 跳过格式不正确的行

        # 获取第二列（UTTRANS_ID）
        uttrans_id = columns[1].split('.')[0]


        # 构造输出路径
        output_path = f"{uttrans_id} data_cy_dialect11/train/{uttrans_id}.wav"

        # 写入输出文件
        outfile.write(output_path + '\n')

print(f"生成的文件已保存到 {output_file}")