from backend.services.audio_service import extract_audio

video_path = "dataset/cricket/Virat Kohli's Match Winning Century ｜ India Tour Of Sri Lanka 2017 [LHWaEiBGsFI].mp4"

audio_path = extract_audio(video_path)
print(f"Extracted audio saved at: {audio_path}")