# **What is Speaker Diarization?** 

Speaker Diarization is the process of identifying who spoke and when in an audio recording.
It segments an audio file into time intervals and assigns a speaker label to each segment.

In simple terms, speaker diarization answers the question:

### **“Who spoke when?”**

For example, in a conversation with three people, diarization will divide the audio like:

- Speaker 1 → 0.0s – 12.4s

- Speaker 2 → 12.4s – 25.1s

- Speaker 3 → 25.1s – 40.0s

without knowing the actual names of the speakers.


## Why Speaker Diarization?

Speaker diarization is useful in many real-world applications:

- 🎙 Meeting recordings – identify different participants

- 📞 Call center analysis – separate agent and customer speech

- 🧠 Speech recognition pipelines – improve transcription accuracy

- 📺 Interviews / podcasts – segment speakers automatically

- ⚖️ Forensics & investigations – analyze multi-speaker audio

- 🤖 AI voice assistants – handle multi-speaker conversations

It is often used before or along with transcription to get structured, speaker-aware results.





## Speaker Diarization

This project performs speaker diarization on WAV audio files using Python and generates RTTM and JSON outputs for each audio file.




**Project Structure**

DIARIZATION/
- .git/
- .venv/
- .gitignore
- diarization.py
- requirements.txt
- test.wav
- test.rttm
- test.json
- test3.wav
- test3.rttm
- test3.json
- test4.wav
- test4.rttm
- test4.json
- test5.wav
- test5.rttm
- test5.json




### Prerequisites

- pyenv

- Python 3.10.13

- pip

- Linux / WSL / macOS recommended



### Python Setup (pyenv)

**Set Python version globally:**

- pyenv global 3.10.13


**Verify Python version:**

- python --version


## Virtual Environment Setup

**Create virtual environment:**

- python -m venv .venv


**Activate virtual environment:**

- source .venv/bin/activate


**Verify Python version inside venv:**

- python --version

**Install Dependencies**

- pip install -r requirements.txt

**Run Speaker Diarization**
- python diarization.py

## Output

**For each .wav file, the script generates:**

- .rttm – speaker diarization segments

- .json – speaker labels with start and end timestamps




[
  {
    "speaker": "SPEAKER_00",
    "start": 0.57,
    "end": 2.76,
    "duration": 2.19
  },
  {
    "speaker": "SPEAKER_01",
    "start": 10.03,
    "end": 25.36,
    "duration": 15.33
  },
  {
    "speaker": "SPEAKER_01",
    "start": 25.46,
    "end": 36.04,
    "duration": 10.58
  },
  {
    "speaker": "SPEAKER_01",
    "start": 36.85,
    "end": 96.17,
    "duration": 59.32
  },
  {
    "speaker": "SPEAKER_01",
    "start": 96.24,
    "end": 162.88,
    "duration": 66.64
  },
  {
    "speaker": "SPEAKER_01",
    "start": 162.95,
    "end": 163.64,
    "duration": 0.70
  },
  {
    "speaker": "SPEAKER_01",
    "start": 163.78,
    "end": 219.89,
    "duration": 56.11
  },
  {
    "speaker": "SPEAKER_01",
    "start": 220.52,
    "end": 223.73,
    "duration": 3.21
  },
  {
    "speaker": "SPEAKER_01",
    "start": 224.12,
    "end": 241.16,
    "duration": 17.05
  },
  {
    "speaker": "SPEAKER_01",
    "start": 241.23,
    "end": 250.89,
    "duration": 9.66
  },
  {
    "speaker": "SPEAKER_01",
    "start": 251.21,
    "end": 268.43,
    "duration": 17.22
  },
  {
    "speaker": "SPEAKER_00",
    "start": 275.75,
    "end": 287.60,
    "duration": 11.85
  }
]
