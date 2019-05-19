from pydub import AudioSegment
import os


audio_cuts = {
    "1jo03g.mp3": [
        10957,
        22316,
        34924,
        41461,
        47556,
        54526,
        62729,
        70988,
        83264,
        93521,
        104781,
        111221,
        125331,
        129682,
        139362,
        149461,
        159913,
        170703,
        176983,
        183442,
        190663,
        196398,
        204108,
        214431,
        224978
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
