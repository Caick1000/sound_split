from glob import glob
from os import chdir
from pydub import AudioSegment
from sys import argv

audio_array = []

audios = []

command1 = argv[1]
command2 = argv[2]


def path_validation(dir_path):
    if dir_path[-1:] is not '/':
        dir_path = dir_path + '/'
        print(dir_path)
    return dir_path


def concatenate(sound_dir=command1, output_name=command2):

    chdir(sound_dir)
    sound_dir = path_validation(sound_dir)
    sound_file = glob('*.wav')
    for file in sound_file:
        audio_array.append(file)

    for i in range(0, len(audio_array)):
        audios.append(AudioSegment.from_wav(sound_dir + audio_array[i]))
    print('Audios -->', audios)

    audios_concat = sum(audios)

    audios_concat.export(sound_dir + output_name, format='wav')


if __name__ == '__main__':
    concatenate()
