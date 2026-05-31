from backend.services.transcription_service import transcribe_video

audio_path = "processed/audio/Virat Kohli's Match Winning Century ｜ India Tour Of Sri Lanka 2017 [LHWaEiBGsFI].wav"

result = transcribe_video(audio_path)

for segment in result["segments"]:
    print(segment)