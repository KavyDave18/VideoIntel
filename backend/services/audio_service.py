import os
import subprocess

def extract_audio(video_path, output_dir="processed/audio"):

    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_dir, f"{filename}.wav")

    command = [
        "ffmpeg",
        "-i", video_path,
        "-ar",
        "16000",
        "-ac",
        "1",
        output_path,
        "-y"
    ]

    subprocess.run(command)
    return output_path

