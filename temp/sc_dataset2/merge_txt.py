import os


def merge_files(input_files, output_file):
    """
    将多个文件的内容合并到一个文件中。

    :param input_files: 输入文件列表
    :param output_file: 输出文件路径
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file_name in input_files:
            if os.path.exists(file_name):
                with open(file_name, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write("\n")  # 在每个文件内容后添加换行符
            else:
                print(f"文件 {file_name} 不存在，跳过。")


# 定义输入文件列表
input_files = [f"sc_datasets2_list/list{i}.txt" for i in range(1, 48)]  # 生成 list1.txt 到 list47.txt 的文件名列表

# 定义输出文件
output_file = "list_train.txt"

# 调用函数合并文件
merge_files(input_files, output_file)
print(f"所有文件已合并到 {output_file}")