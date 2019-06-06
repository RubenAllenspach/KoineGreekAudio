from pydub import AudioSegment
import os


audio_cuts = {
    "joh02g.mp3": [
        10610,
        17749,
        21710,
        27936,
        32847,
        37994,
        46391,
        53092,
        59478,
        72166,
        82419,
        92701,
        101889,
        107150,
        114759,
        126285,
        134161,
        140915,
        147572,
        153832,
        162304,
        165975,
        175411,
        184792,
        190084,
        197688
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
