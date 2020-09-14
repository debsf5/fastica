import librosa
import IPython as ip

y1, sample_rate1 = librosa.load(audio1, mono=True)
y2, sample_rate2 = librosa.load(audio2, mono=True)

# MERGE
librosa.display.waveplot((y1+y2)/2, sr=int((sample_rate1+sample_rate2)/2))

# REPRODUCE
ip.display.Audio((y1+y2)/2, rate=int((sample_rate1+sample_rate2)/2))
