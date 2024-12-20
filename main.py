import os
from big_sleep import Imagine
from utils import parse_poems_file, get_inspiration_images_path

current_directory = os.getcwd()

# ---- Set input inspiration images path
inspirations_path = current_directory + '/artwork_inspiration/'
# ---- Set input poems path
poems_path = './'
# ---- Set ouput images path
dream_path = '/data/arouxel/results_dot/results/'


print('\n ---- Image generation script -----')
# --- Parse poems from txt
poems_list = parse_poems_file(poems_path + 'poems_concat.txt')

# --- Get inspiration images path list
img_path_list = get_inspiration_images_path(inspirations_path)


print("We have : {} poems in our txt file.".format(len(poems_list)))
print(poems_list)
print("We have : {} images in our inspiration folder".format(len(img_path_list)))

def go_dream(text,img_path,dream_path):

    print('\n --------- DREAM -----------')
    print('poem :{}'.format(text))
    print('image path :{}'.format(img_path))

    dream = Imagine(
        text = text,
        lr = 5e-2,
        iteration_stop = 1000,
        gradient_accumulate_every = 1 ,
        image_size = 512,
        # num_cutouts = 32,  Trying new settings
        img = img_path,
        #save_every = 2, #not active for now
        exponential_images_save=True,
        save_progress = True
    )

    print('Printing here :{}'.format(dream_path))
    os.chdir(dream_path)
    dream()

# Looping on inspiration images path
for idx, img_path in enumerate(img_path_list):

        # Creating one directory per inspiration image
        filename = os.path.splitext(os.path.basename(img_path))[0]
        try:
            os.stat(dream_path + filename)
        except:
            os.mkdir(dream_path + filename)

        # Looping on poems string
        for poems in poems_list:
                go_dream(poems, img_path, dream_path + filename)
