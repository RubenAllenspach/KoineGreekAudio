from pydub import AudioSegment


song = AudioSegment.from_mp3("1jo01/1jo01g.mp3")

cuts = [
    9400,
    20740,
    31000,
    44700,
    49000,
    59500,
    68400,
    79000,
    86200,
    96400,
    1037000
]

last_cut = 0
counter = 0

for cut in cuts:
    verse = song[last_cut:cut]
    verse.export("verse_" + str(counter) + ".mp3", format="mp3")

    counter = counter + 1
    last_cut = cut
