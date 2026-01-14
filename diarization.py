from pyannote.audio import Pipeline
import torch

AUDIO_FILE = "test.wav"
RTTM_OUTPUT = "output.rttm"

def main():
    print("Loading diarization model...")
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization-3.1")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    pipeline.to(device)

    print("Processing audio:", AUDIO_FILE)
    diarization = pipeline(AUDIO_FILE)

    with open(RTTM_OUTPUT, "w") as f:
        diarization.write_rttm(f)

    print("Diarization completed.")
    print("RTTM file saved as:", RTTM_OUTPUT)

    # Print speaker segments
    print("\nSpeaker Segments:")
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        print(f"{speaker}: {turn.start:.2f}s --> {turn.end:.2f}s")

if __name__ == "__main__":
    main()
