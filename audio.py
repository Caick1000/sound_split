from glob import glob
from os import chdir
from pydub import AudioSegment
from sys import argv,  exc_info
import argparse

audio_array = []
audios = []
audio_extensions = ['.wav','.ogg', 'mp3']


parser = argparse.ArgumentParser(description='Concatenate audios')
parser.add_argument('-p','--path', help='Path of folder containing the audios', required=True)
parser.add_argument('-n','--name', help='Name of the concatenated audio file', required=True)
args = parser.parse_args()


def path_validation(dir_path):
    if dir_path[-1:] is not '/':
        dir_path = dir_path + '/'

    return dir_path

def filename_validation(file_name):
    if file_name[-3:] not in audio_extensions:
        file_name = file_name + '.wav'

    return file_name

def concatenate():

    try:

        sound_dir = args.path
        output_name = args.name

        print('Running...')
        chdir(sound_dir)
        sound_dir = path_validation(sound_dir)
        output_name = filename_validation(output_name)
        sound_file = glob('*.wav')
        for file in sound_file:
            audio_array.append(file)

        for i in range(0, len(audio_array)):
            audios.append(AudioSegment.from_wav(sound_dir + audio_array[i]))
        #print('Audios -->', audios)

        audios_concat = sum(audios)

        audios_concat.export(sound_dir + output_name, format='wav')
        print('Exported successfully!')

    except OSError as err:
        print("OS error: {}".format(err))
    except ValueError:
        print("Wrong type. Did you type anything else other than a String?")
    except:
        print("Unexpected error:", exc_info()[0])
        raise


if __name__ == '__main__':
    concatenate()
