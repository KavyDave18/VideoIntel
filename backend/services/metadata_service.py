import cv2

def extract_video_metadata(video_path):
    video = cv2.VideoCapture(video_path)
    
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)

    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

    duration = frame_count / fps

    resolution = f"{int(width)}x{int(height)}"

    video.release()

    return {
        "fps": fps,
        "duration": duration,
        "resolution": resolution
        }
