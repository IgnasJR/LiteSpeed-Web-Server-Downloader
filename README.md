A python script to download audio files from mp3.hardcore.lt and create .mp4 files of them.

Required depedencies:

- For video making script:
  - moviepy
  - tinytag
- For downloading script:
  - bs4
  - urllib

To install them, run

```
py -m pip install {dependency_name}
```

#### To run the create the videos, open the console and run:

```
py {directory_of_video_making_script} {image_directory} {input_directory} {output_directory}
```

#### To run the download script, open the console and run:

```
py {directory_of_download_script} {url_of_the_download_folder}
```

### You may drag and drop the folders and image files to the console window, to input their directories
