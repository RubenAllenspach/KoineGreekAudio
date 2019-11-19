from pydub import AudioSegment
import os


audio_cuts = {
    "mat06g.mp3": [
        10270,
        22303,
        38046,
        44585,
        51266,
        67734,
        80506,
        89910,
        97194,
        104753,
        111102,
        114773,
        120207,
        125966,
        132674,
        139518,
        154409,
        159921,
        169544,
        178607,
        187806,
        192218,
        200496,
        209985,
        222762,
        236743,
        249339,
        254663,
        264123,
        269882,
        279253,
        285996,
        293993,
        300905,
        309373
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
