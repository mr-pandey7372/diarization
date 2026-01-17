What is Speaker Diarization?

Speaker Diarization is the process of identifying who spoke and when in an audio recording.
It segments an audio file into time intervals and assigns a speaker label to each segment.

In simple terms, speaker diarization answers the question:

“Who spoke when?”

For example, in a conversation with three people, diarization will divide the audio like:

Speaker 1 → 0.0s – 12.4s

Speaker 2 → 12.4s – 25.1s

Speaker 3 → 25.1s – 40.0s

without knowing the actual names of the speakers.


Why Speaker Diarization?

Speaker diarization is useful in many real-world applications:

🎙 Meeting recordings – identify different participants

📞 Call center analysis – separate agent and customer speech

🧠 Speech recognition pipelines – improve transcription accuracy

📺 Interviews / podcasts – segment speakers automatically

⚖️ Forensics & investigations – analyze multi-speaker audio

🤖 AI voice assistants – handle multi-speaker conversations

It is often used before or along with transcription to get structured, speaker-aware results.





Speaker Diarization

This project performs speaker diarization on WAV audio files using Python and generates RTTM and JSON outputs for each audio file.