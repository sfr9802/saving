from os import path
from pydub import AudioSegment

# files                                                                       
src = "Still Got The Blues.mp3"
dst = "test.wav"

# convert wav to mp3                                                            
audSeg = AudioSegment.from_mp3(src)
audSeg.export(dst, format="wav")