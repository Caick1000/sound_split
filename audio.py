from glob import glob
from os import chdir, getcwd, path
from pydub import AudioSegment
from sys import exc_info
import argparse
from time import sleep

audio_array = []
audios = []
audio_extensions = ['.wav','.ogg', 'mp3']

current_path = getcwd()


parser = argparse.ArgumentParser(description='Concatenate audios')
parser.add_argument('-p','--path', help='Path of folder containing the audios.\nDefault=Current folder', required=False, default=current_path)
parser.add_argument('-n','--name', help='Name of the concatenated audio file.\nDefault="file"', required=False, default='File')
args = parser.parse_args()


def path_validation(path_name):
        
    if path.exists(path_name):
        print('Valid path: ', path_name )
        sleep(1)    

    else:
        print('Invalid path =>', path_name)
        path_name = getcwd()
        print('Changing path to: ', path_name)
        sleep(1)

    if path_name[-1:] is not '/':
        path_name = path_name + '/'

    return path_name

def filename_validation(file_name):
    if file_name[-3:] not in audio_extensions:
        file_name = file_name + '.wav'

    return file_name

def concatenate():
    try:

        sound_dir = args.path
        output_name = args.name

        print('Running...')
        sleep(1)
        sound_dir = path_validation(sound_dir)
        chdir(sound_dir)
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
