import os

def read_file_names(file_path):
    """
    读取文件中的编号，并返回一个集合
    """
    file_names = set()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # 去掉行首行尾的空白字符，并提取编号
                file_name = line.strip().split()[0]
                file_names.add(file_name)
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到！")
    except Exception as e:
        print(f"读取文件 {file_path} 时出错：{e}")
    return file_names

def remove_files_and_lines(file_names, folder_path, lst_file_paths):
    """
    删除指定文件夹中的.wav文件和对应的行
    """
    # 删除.wav文件
    for file_name in file_names:
        wav_file_path = os.path.join(folder_path, f"{file_name}.wav")
        if os.path.exists(wav_file_path):
            os.remove(wav_file_path)
            print(f"已删除文件：{wav_file_path}")
        else:
            print(f"文件 {wav_file_path} 不存在，跳过删除。")

    # 删除.lst文件中的对应行
    for lst_file_path in lst_file_paths:
        temp_file_path = lst_file_path + ".tmp"
        try:
            with open(lst_file_path, 'r', encoding='utf-8') as lst_file, \
                 open(temp_file_path, 'w', encoding='utf-8') as temp_file:
                for line in lst_file:
                    # 去掉行首行尾的空白字符
                    line = line.strip()
                    if line.split()[0] not in file_names:
                        temp_file.write(line + "\n")
            # 替换原文件
            os.replace(temp_file_path, lst_file_path)
            print(f"已更新文件：{lst_file_path}")
        except FileNotFoundError:
            print(f"文件 {lst_file_path} 未找到！")
        except Exception as e:
            print(f"处理文件 {lst_file_path} 时出错：{e}")

# 主程序
if __name__ == "__main__":
    # 定义文件路径
    dev_txt = "long_wav_files_dev.txt"
    train_txt = "long_wav_files_train.txt"
    dev_folder = "../dataset/sc_dataset2/dev"
    train_folder = "../dataset/sc_dataset2/train"
    dev_lst_files = ["../dataset/sc_dataset2/list/dev.wav.lst", "../dataset/sc_dataset2/list/dev.syllabel.txt"]
    train_lst_files = ["../dataset/sc_dataset2/list/train.wav.lst", "../dataset/sc_dataset2/list/train.syllabel.txt"]

    # 读取需要删除的文件名
    dev_file_names = read_file_names(dev_txt)
    train_file_names = read_file_names(train_txt)

    # 删除文件和对应的行
    print("处理开发集...")
    remove_files_and_lines(dev_file_names, dev_folder, dev_lst_files)
    print("处理训练集...")
    remove_files_and_lines(train_file_names, train_folder, train_lst_files)

    print("操作完成！")