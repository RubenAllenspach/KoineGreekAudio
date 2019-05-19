from pydub import AudioSegment
import os


audio_cuts = {
    "1jo05g.mp3": [
        11018,
        21090,
        29880,
        37969,
        47929,
        54277,
        68930,
        71725,
        77239,
        89088,
        104558,
        112452,
        119643,
        128734,
        137422,
        146136,
        162424,
        167939,
        178597,
        183866,
        199965,
        204154
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
