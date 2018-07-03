from pydub import AudioSegment, silence
from sys import argv

#command1 = argv[1]

def slice_audio(sound_dir, output_path):

    sound = AudioSegment.from_wav(sound_dir)
    loudness = sound.dBFS
    print(loudness)

    #sliced_test = silence.detect_silence(sound, min_silence_len=1000, silence_thresh=loudness + 1.7)

    sliced = silence.split_on_silence(sound, min_silence_len=500, silence_thresh=loudness, keep_silence=300)

    for i, chunks in enumerate(sliced):
        chunk_name = output_path + str(i) + ".wav"

        print("Exporting {}".format(chunk_name))
        chunks.export(chunk_name, format="wav")

slice_audio("C:/sample_test/tudo.wav", "C:/sample_test/test")
#if __name__ == '__main__':
    #slice_audio()
