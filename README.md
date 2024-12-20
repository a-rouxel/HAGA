# HAGA : Poems to GIF
![HAGA Example](./gif.gif)


This repository provides a workflow for generating visual art from textual poems and inspiration images, ultimately composing them into animated GIFs. By combining the poetic language of written verse with guiding "inspiration images," this project leverages neural text-to-image generation to produce a series of images and then transforms these sequences into a final animated piece.

## Overview

The core idea of this workflow is to blend the semantic content of poems with an initial visual prompt image. For each line (or poem) taken from a text file, and for each inspiration image in a specified folder, the script generates a series of images that evolve over time. These images can then be compiled into GIFs, providing a dynamic, multimodal art experience.

**Key steps:**
1. **Inspiration Images:** Provide a set of starting images that will serve as a visual anchor.
2. **Poems Input:** Provide a text file containing poems or lines of poetry.
3. **Neural Generation:** For each poem and inspiration image pair, the script uses [The Big Sleep](https://github.com/lucidrains/big-sleep) or a similar text-to-image model to create an image series guided by the poem and the inspiration image.
4. **Output:** Generated images are stored per poem-image combination, making it easy to later convert the result into an animated GIF.

## Dependencies & Installation

**Main Requirements:**
- Python 3.7+
- [The Big Sleep](https://github.com/lucidrains/big-sleep) library (for text-to-image generation)
- Other Python dependencies such as `torch`, `PIL`, etc., as required by The Big Sleep

**Installing Dependencies:**
```bash
pip install -r requirements.txt
```

*(Make sure to include a `requirements.txt` with all needed dependencies or adapt this step to your environment.)*

## Repository Structure

- **main.py**: The main script that reads poems, iterates over inspiration images, and generates image sequences.
- **poems_concat.txt**: A text file containing concatenated poems or lines of text, one per line.
- **artwork_inspiration/**: A folder containing the input inspiration images. Each image in this folder will be used as a visual seed.
- **utils.py**: Contains helper functions for parsing poems and retrieving inspiration image paths.
- **/data/arouxel/results_dot/results/**: Default output directory where generated images are stored. Each poem-image pair will create its own subdirectory of results.

## How to Use

1. **Prepare the Input Files:**
   - Ensure `poems_concat.txt` contains your desired poems or text lines.
   - Place your inspiration images in `artwork_inspiration/`.

2. **Adjust the Paths (if necessary):**
   - In `main.py`, you may update:
     - `inspirations_path` (input image directory)
     - `poems_path` (poems file directory)
     - `dream_path` (output directory for generated images)
   
3. **Run the Script:**
   ```bash
   python main.py
   ```
   
   The script will:
   - Parse the poems from `poems_concat.txt`.
   - Retrieve all images in `artwork_inspiration/`.
   - Generate image sequences using The Big Sleep for each poem-image pair.
   
   Outputs will be saved under `dream_path` in a structured manner, one folder per inspiration image, containing subfolders/images for each poem.

4. **Post-Processing (Optional):**
   After generation is complete, you may want to:
   - Convert the generated image sequences into GIFs using ImageMagick or any GIF creation tool:
     ```bash
     # Example: converting a sequence of PNG images into a GIF
     convert -delay 10 -loop 0 *.png output.gif
     ```
   
   Adjust the delay parameter and file order as needed.

## Customization

- **Hyperparameters:** 
  Within `main.py`, the `go_dream` function initializes the `Imagine` class with parameters like `lr` (learning rate), `iteration_stop`, `image_size`, and so forth. Adjusting these can influence the quality, style, and speed of the generated imagery.
  
- **Model Parameters:**
  You can experiment with different text prompts or even different underlying models (if The Big Sleep is replaced or extended with another text-to-image framework).

## Troubleshooting

- **Memory Issues:** Large image sizes and high iteration counts can be demanding on GPU memory. Reduce `image_size` or the number of iterations if you encounter memory problems.
- **File Structure:** Ensure that the directory structure is correct and that `poems_concat.txt` and `artwork_inspiration/` exist and contain the expected files.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the code, add new features, or enhance documentation.
