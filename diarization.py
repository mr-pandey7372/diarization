from pyannote.audio import Pipeline
import json
import torch

# Make results more stable
torch.manual_seed(0)

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1")

audio_file = "test5.wav"
rttm_file = "test5.rttm"
json_file = "test5.json"

# Run diarization (FIXED: number of speakers)
diarization = pipeline(audio_file, num_speakers=2)

MIN_DURATION = 0.5  # seconds (removes interruptions)

# Print to console
for turn, _, speaker in diarization.itertracks(yield_label=True):
    if (turn.end - turn.start) >= MIN_DURATION:
        print(f"{turn.start:.1f}s - {turn.end:.1f}s : {speaker}")

# Save RTTM
with open(rttm_file, "w") as f:
    diarization.write_rttm(f)

# Save JSON
segments = []
for turn, _, speaker in diarization.itertracks(yield_label=True):
    duration = turn.end - turn.start
    if duration >= MIN_DURATION:
        segments.append({
            "speaker": speaker,
            "start": round(turn.start, 2),
            "end": round(turn.end, 2),
            "duration": round(duration, 2)
        })

with open(json_file, "w") as f:
    json.dump(segments, f, indent=4)

print("\nFiles generated:")
print("RTTM:", rttm_file)
print("JSON:", json_file)
