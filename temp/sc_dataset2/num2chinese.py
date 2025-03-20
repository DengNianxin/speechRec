import re
import os

# 数字转换为汉字的函数
def number_to_chinese(num):
    units = ['', '十', '百', '千', '万', '亿']
    nums = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    result = []

    if num == 0:
        return nums[0]

    while num > 0:
        digit = num % 10
        if digit != 0:
            result.append(nums[digit] + units[len(result)])
        else:
            result.append(nums[digit])
        num //= 10

    # 去掉多余的零
    while len(result) > 1 and result[-1] == '零':
        result.pop()

    # 处理连续的零
    result = [result[i] if result[i] != '零' or (i == len(result) - 1 or result[i + 1] == '零') else '' for i in range(len(result))]

    return ''.join(reversed(result))

# 小数转换为汉字的函数
def decimal_to_chinese(decimal):
    integer_part, decimal_part = decimal.split('.')
    integer_part = number_to_chinese(int(integer_part))
    decimal_part = ''.join([number_to_chinese(int(digit)) for digit in decimal_part])
    return f"{integer_part}点{decimal_part}"

# 处理文本内容的函数
def process_text(text):
    # 去除汉字间的空格
    text = re.sub(r'(?<=\u4e00-\u9fff)\s+(?=\u4e00-\u9fff)', '', text)

    # 转换百分比
    text = re.sub(r'(\d+)%', lambda m: f"百分之{number_to_chinese(int(m.group(1)))}", text)

    # 转换范围
    text = re.sub(r'(\d+)-(\d+)', lambda m: f"{number_to_chinese(int(m.group(1)))}至{number_to_chinese(int(m.group(2)))}", text)

    # 转换小数
    text = re.sub(r'(\d+\.\d+)', lambda m: decimal_to_chinese(m.group(1)), text)

    # 只保留汉字
    text = re.sub(r'[^\u4e00-\u9fff]', '', text)

    return text

# 处理文件内容的函数
def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # 分割文件路径和文本内容
            parts = line.strip().split('\t')
            if len(parts) == 2:
                file_path, content = parts
                # 处理文本内容
                processed_content = process_text(content)
                # 保留文件路径，只替换文本内容
                outfile.write(f"{file_path}\t{processed_content}\n")
            else:
                outfile.write(line)  # 保留原始行

# 示例文件路径
input_file = "list_dev.txt"
output_file = "list_dev_processed.txt"

# 调用函数处理文件
process_file(input_file, output_file)
print(f"文件已处理并保存到 {output_file}")