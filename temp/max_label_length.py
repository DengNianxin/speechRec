def calculate_label_lengths(input_file_path, output_file_path):
    """
    从指定的txt文件中读取数据，计算拼音标签的长度，输出最大长度和超过64的比例，
    并将标签长度超过64的ID写入到指定的输出文件中。
    :param input_file_path: 包含拼音标签的txt文件路径
    :param output_file_path: 输出超过64长度的ID的txt文件路径
    """
    # 初始化变量
    lengths = []  # 用于存储每个标签的长度
    over_64_ids = []  # 用于存储标签长度超过64的ID

    # 读取文件
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去掉行首行尾的空白字符，并分割成单词列表
            parts = line.strip().split()
            # 第一列是ID，后面的才是拼音标签
            if len(parts) > 1:
                label_length = len(parts) - 1  # 减去ID部分
                lengths.append(label_length)
                # 如果长度超过64，记录ID
                if label_length > 64:
                    over_64_ids.append(parts[0])

    # 计算最大长度
    max_length = max(lengths) if lengths else 0

    # 计算超过64的比例
    over_64_count = sum(1 for length in lengths if length > 64)
    over_64_ratio = over_64_count / len(lengths) if lengths else 0

    # 输出结果
    print(f"最大长度: {max_length}")
    print(f"超过64的比例: {over_64_ratio:.2%}")

    # 将超过64长度的ID写入到输出文件
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for id in over_64_ids:
            output_file.write(id + '\n')

    print(f"标签长度超过64的ID已写入到文件: {output_file_path}")


# 示例用法
input_file_path = '../dataset/sc_dataset2/list/train.syllabel.txt'  # 替换为你的输入txt文件路径
output_file_path = 'over_64_ids_train.txt'  # 替换为你希望输出的文件路径
calculate_label_lengths(input_file_path, output_file_path)