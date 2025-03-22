import os
import wave

def get_wav_duration(file_path):
    """
    获取.wav文件的时长（单位：秒）
    """
    try:
        with wave.open(file_path, 'rb') as wav_file:
            frames = wav_file.getnframes()  # 获取总帧数
            rate = wav_file.getframerate()  # 获取采样率
            duration = frames / float(rate)  # 计算时长
        return duration
    except Exception as e:
        print(f"无法读取文件 {file_path} 的时长：{e}")
        return None

def count_wav_files(folder_path, threshold=9):
    """
    统计文件夹下.wav文件时长超过指定阈值的数量和占比
    """
    total_wav_files = 0
    long_wav_files = 0
    long_wav_file_names = []  # 用于存储时长超过阈值的文件名（去掉.wav后缀）

    # 遍历文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.wav'):  # 检查是否为.wav文件
                total_wav_files += 1
                file_path = os.path.join(root, file)
                duration = get_wav_duration(file_path)
                if duration is not None and duration > threshold:
                    long_wav_files += 1
                    # 去掉.wav后缀并保存文件名
                    file_name_without_extension = os.path.splitext(file)[0]
                    long_wav_file_names.append(file_name_without_extension)

    # 计算占比
    if total_wav_files > 0:
        long_wav_percentage = (long_wav_files / total_wav_files) * 100
    else:
        long_wav_percentage = 0

    return total_wav_files, long_wav_files, long_wav_percentage, long_wav_file_names

# 主程序
if __name__ == "__main__":
    folder_path = "D:\\PycharmProjects\\asrt1\\dataset\\sc_dataset2\\dev"
    if not os.path.isdir(folder_path):
        print("指定的路径不是一个有效的文件夹！")
    else:
        total_wav_files, long_wav_files, long_wav_percentage, long_wav_file_names = count_wav_files(folder_path)
        print(f"总.wav文件数量：{total_wav_files}")
        print(f"时长超过16秒的.wav文件数量：{long_wav_files}")
        print(f"占比：{long_wav_percentage:.2f}%")

        # 将时长超过16秒的文件名保存到当前工作目录的文本文件中
        output_file_path = os.path.join(os.getcwd(), "long_wav_files_dev.txt")  # 使用当前工作目录
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            for file_name in long_wav_file_names:
                output_file.write(file_name + "\n")

        print(f"时长超过16秒的.wav文件名已保存到 {output_file_path}")