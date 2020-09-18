from pydub import AudioSegment

sound1 = AudioSegment.from_file("/path/to/ac.mp3")
sound2 = AudioSegment.from_file("/path/to/heartsound.wav")

combined = sound1.overlay(sound2)

combined.export("/path/to/combined.wav", format='wav')
