import os
import os
import wave


def get_max_duration(wav_files):
    """
    计算一批 WAV 文件的最大时长（单位：秒）。

    参数:
        wav_files (list): WAV 文件路径的列表。

    返回:
        float: 最大时长（单位：秒）。
    """
    max_duration = 0

    for file in wav_files:
        if not os.path.exists(file):
            print(f"Warning: File {file} does not exist. Skipping...")
            continue

        try:
            with wave.open(file, 'rb') as wav_file:
                # 获取采样率和样本数量
                sample_rate = wav_file.getframerate()
                num_samples = wav_file.getnframes()
                # 计算时长（单位：秒）
                duration = num_samples / sample_rate
                # 更新最大时长
                max_duration = max(max_duration, duration)
        except Exception as e:
            print(f"Error processing file {file}: {e}")

    return max_duration

# 获取文件夹中的所有 WAV 文件
# 7.88 7.03 6.01 5.80 8.66 5.32 6.95 6.67 7.45 5.59 39.47 27.48
wav_folder = "C:\\Users\\dnx\\Desktop\\dataset\\sc_dataset2\\dev"
wav_files = [os.path.join(wav_folder, f) for f in os.listdir(wav_folder) if f.endswith('.wav')]

# 计算最大时长
max_duration = get_max_duration(wav_files)
print(f"The maximum duration of the WAV files is {max_duration:.2f} seconds.")