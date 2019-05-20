from pydub import AudioSegment
import os


audio_cuts = {
    "joh01g.mp3":[
        9509,
        15435,
        18075,
        23281,
        27422,
        32042,
        37059,
        44941,
        49473,
        55302,
        61811,
        66450,
        74702,
        84174,
        96701,
        107655,
        114066,
        120823,
        129289,
        140529,
        146398,
        155738,
        162635,
        171252,
        174515,
        183331,
        191209,
        197542,
        204230,
        213855,
        221471,
        228309,
        236985,
        249872,
        255348,
        259994,
        265467,
        270283,
        282573,
        292662,
        300783,
        310657,
        321088,
        328774,
        333218,
        344435,
        351934,
        360027,
        370237,
        377167,
        385613,
        397513
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
