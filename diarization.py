from pyannote.audio import Pipeline
import json

pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")

audio_file = "test.wav"
rttm_file = "test.rttm"
json_file = "test.json"

# Run diarization
diarization = pipeline(audio_file)

# Print to console
for turn, _, speaker in diarization.itertracks(yield_label=True):
    print(f"{turn.start:.1f}s - {turn.end:.1f}s : {speaker}")

# Save RTTM
with open(rttm_file, "w") as f:
    diarization.write_rttm(f)

# Save JSON
segments = []
for turn, _, speaker in diarization.itertracks(yield_label=True):
    segments.append({
        "speaker": speaker,
        "start": round(turn.start, 2),
        "end": round(turn.end, 2),
        "duration": round(turn.end - turn.start, 2)
    })

with open(json_file, "w") as f:
    json.dump(segments, f, indent=4)

print("\nFiles generated:")
print("RTTM:", rttm_file)
print("JSON:", json_file)
