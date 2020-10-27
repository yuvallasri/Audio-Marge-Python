from pydub import AudioSegment

sound1 = AudioSegment.from_file("baby.wav")
sound2 = AudioSegment.from_file("beach.wav")

combined = sound1.overlay(sound2)

combined.export("combined.wav", format='wav')