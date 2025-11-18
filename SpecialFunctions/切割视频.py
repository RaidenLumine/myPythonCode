import os
import subprocess

def split_video_ffmpeg(video_path, output_dir, segment_time=10):
    """
    通过调用FFmpeg分割视频
    """
    video_basename = os.path.basename(video_path)
    video_name, video_ext = os.path.splitext(video_basename)
    segment_folder = os.path.join(output_dir, f"{video_name}_segments")
    os.makedirs(segment_folder, exist_ok=True)

    # 构建FFmpeg命令
    # 关键参数说明：
    # -c copy: 直接复制流而不重新编码，速度极快，质量无损。
    # -segment_time: 每个切片的时长。
    # -f segment: 指定分段格式。
    output_template = os.path.join(segment_folder, f"segment_%03d{video_ext}")

    ffmpeg_command = [
        'ffmpeg',
        '-i', video_path,
        '-c', 'copy',  # 复制流，不重新编码
        '-segment_time', str(segment_time),
        '-f', 'segment',
        '-reset_timestamps', '1',  # 重置每个片段的时间戳
        output_template
    ]

    try:
        subprocess.run(ffmpeg_command, check=True)
        print(f"视频分割完成！片段保存在: {segment_folder}")
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg 处理出错: {e}")
    except FileNotFoundError:
        print("错误：未找到 ffmpeg 可执行文件，请确保已正确安装并配置环境变量。")

# 使用方法示例
if __name__ == "__main__":
    # 请替换为您的视频实际路径
    input_video = "D:\Resource\师范生作业\见习观摩\第二次\视频2.mp4"
    
    # 请替换为您希望保存片段的目录
    output_folder = "D:\Resource\师范生作业\见习观摩\第二次"
    
    # 每段指定秒数
    split_video_ffmpeg(input_video, output_folder, segment_time=180)