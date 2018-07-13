from pydub import AudioSegment, silence
from sys import argv
from os import path, getcwd

#command1 = argv[1]

audios = []
audio_chunks = []



def name_validation(path_name, file_name):
    
    current_path = getcwd()
    
    if path_name is not None:
        
        if path.exists(path_name):
            print("Valid path")

        else:
            print("Invalid path")
            path_name = getcwd()
            print(path_name)


    if file_name is not None:
        
        if path.exists(file_name):
            print("Valid output file path")

        else:
            print("Invalid output file path")
            file_name = (current_path + "\File")
            print(file_name)



def slice_audio(sound_dir, output_path):
    
    name_validation(sound_dir, output_path)

    sound = AudioSegment.from_wav(sound_dir)
    sliced = silence.split_on_silence(sound, min_silence_len=100, silence_thresh=-16)

    for i, chunks in enumerate(sliced):
        print("-->", i, chunks)
        audio_chunks.append(chunks)
        chunks.export(output_path + str(i) + '.wav', format='wav')
        


slice_audio("C:/sample_test/numeros.wav", "C:/sample_test/test")

    

#if __name__ == '__main__':
    #slice_audio()
