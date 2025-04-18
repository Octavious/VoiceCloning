import os
import pysrt
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# Paths
video_dir = "videos"
output_dir = "output"
wavs_dir = os.path.join(output_dir, "wavs")
os.makedirs(wavs_dir, exist_ok=True)

metadata_path = os.path.join(output_dir, "metadata.csv")

def convert_video_to_audio(video_path, output_wav_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_wav_path, fps=22050, nbytes=2, codec='pcm_s16le')
    return output_wav_path

def extract_audio_segments(audio_path, srt_path, prefix):
    subs = pysrt.open(srt_path)
    full_audio = AudioSegment.from_wav(audio_path)
    entries = []

    for i, sub in enumerate(subs):
        start_ms = sub.start.ordinal
        end_ms = sub.end.ordinal
        clip_audio = full_audio[start_ms:end_ms]
        clip_filename = f"{prefix}_{i}.wav"
        clip_path = os.path.join(wavs_dir, clip_filename)
        clip_audio.export(clip_path, format="wav", parameters=["-ac", "1", "-ar", "22050"])
        text = sub.text.replace('\n', ' ').strip()
        if text:
            entries.append(f"{clip_filename}|{text}")
    return entries

all_entries = []

for file in os.listdir(video_dir):
    if file.endswith(".mp4"):
        basename = os.path.splitext(file)[0]
        video_path = os.path.join(video_dir, file)
        srt_path = os.path.join(video_dir, f"{basename}.srt")
        wav_path = os.path.join(output_dir, f"{basename}.wav")

        print(f"Processing {file}...")
        convert_video_to_audio(video_path, wav_path)
        entries = extract_audio_segments(wav_path, srt_path, basename)
        all_entries.extend(entries)

# Save metadata
with open(metadata_path, "w", encoding="utf-8") as f:
    for entry in all_entries:
        f.write(entry + "\n")

print(f"\n✅ Done. Your dataset is ready in '{output_dir}'")
