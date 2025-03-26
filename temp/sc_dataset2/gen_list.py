import re

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # 去掉行尾的换行符并分割列
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                file_path = parts[0]  # 第一列是文件路径
                # 提取编号（假设编号是文件名的一部分）
                match = re.search(r'SCC\d+', file_path)
                if match:
                    id = match.group(0)  # 提取编号
                    # new_path = f"sc_dataset2/train/{id}.wav"  # 构造新的路径
                    new_path = f"sc_dataset2/dev/{id}.wav"  # 构造新的路径
                    outfile.write(f"{id} {new_path}\n")  # 写入新格式的行

# 示例文件路径
input_file = "list_dev_processed.txt"
output_file = "dev.wav.lst"

# 调用函数处理文件
process_file(input_file, output_file)
print(f"文件已处理并保存到 {output_file}")