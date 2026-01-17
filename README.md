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
├── .git/
├── .venv/
├── .gitignore
├── diarization.py
├── requirements.txt
├── test.wav
├── test.rttm
├── test.json
├── test3.wav
├── test3.rttm
├── test3.json
├── test4.wav
├── test4.rttm
├── test4.json
├── test5.wav
├── test5.rttm
├── test5.json




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