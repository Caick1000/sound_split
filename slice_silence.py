from pydub import AudioSegment, silence
from sys import argv
from os import path, getcwd

#command1 = argv[1]

audios = []



def name_validation(path_name, file_name):
    
    current_path = getcwd()
    
    if path_name is not None:
        
        if path.exists(path_name):
            print('Valid path')

        else:
            print('Invalid path')
            path_name = getcwd()
            print(path_name)


    if file_name is not None:
        
        if path.exists(file_name):
            print('Valid output file path')

        else:
            print('Invalid output file path')
            file_name = (current_path + '\File')
            print(file_name)



def slice_audio(sound_dir, output_path):
    
    name_validation(sound_dir, output_path)
    sound = AudioSegment.from_wav(sound_dir)

    loudness = sound.dBFS
    print(loudness)
    sliced = silence.split_on_silence(sound, min_silence_len=100, silence_thresh=loudness)

    for i, chunks in enumerate(sliced):
        chunk_name = output_path + str(i) + '.wav'

        print('Exporting {}'.format(chunk_name))
        chunks.export(chunk_name, format='wav')
        


slice_audio('C:/sample_test/tudo.wav', 'C:/sample_test/test')

    

#if __name__ == '__main__':
    #slice_audio()