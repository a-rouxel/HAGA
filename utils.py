import glob
import os
import re

def parse_poems_file(text_file_path):

    list_poems = list()

    with open(text_file_path) as f:
        lines = f.readlines()

    # for idx,string in enumerate(lines):
        # if len(string)<5:
        #     lines.pop(idx)

    for idx,line in enumerate(lines):
        if line != '\n' and lines[idx-1] == '\n':

            line = line.replace('\n',"")
            line = re.sub(r"[()\"#/@;:<>{}=~|]", "", line)
            if lines[idx+1] == '\n':
                list_poems.append(line)
            elif lines[idx+1] != '\n' and lines[idx+2] == '\n':
                next_line = lines[idx+1].replace('\n',"")
                list_poems.append(line+ next_line)
            elif lines[idx+1] != '\n' and lines[idx+2] != '\n' and lines[idx+3] == '\n':
                next_line = lines[idx+1].replace('\n',"")
                over_line = lines[idx+1].replace('\n',"")
                list_poems.append(line + next_line + over_line)
            else:
                print('Your poem is too long bro...')

    return list_poems

def get_inspiration_images_path(inspirations_path):

    os.chdir(inspirations_path)


    list_of_frames = [os.getcwd()  + '/'+ f for f in glob.glob('*.jpg')]
    list_of_frames = list_of_frames + [os.getcwd()  + '/'+ f for f in glob.glob('*.png')]
    frames_names = glob.glob('*.jpg') + glob.glob('*.ng')

    return list_of_frames




