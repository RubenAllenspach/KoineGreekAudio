from pydub import AudioSegment
import os


"""
"1jo01g.mp3": [
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
],
"""

audio_cuts = {
    "1jo02g.mp3": [
        9970,
        22360,
        30764,
        37127,
        45797,
        55557,
        62157,
        73815,
        84708,
        92648,
        99065,
        110756,
        117226
    ]
}

last_cut = 0
counter = 0

for audio, cuts in audio_cuts.items():
    song = AudioSegment.from_mp3("audio/" + audio)
    path = "cuts/" + audio

    if not os.path.exists(path):
        os.mkdir(path)

    for cut in cuts:
        verse = song[int(last_cut):int(cut)]
        verse.export(path + "/verse_" + str(counter) + ".mp3", format="mp3")

        counter = counter + 1
        last_cut = cut
