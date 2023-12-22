import os
import sys
from moviepy.editor import ImageClip, AudioFileClip
from tinytag import TinyTag

def get_title(audio_file):
    tag = TinyTag.get(audio_file)
    artist = tag.artist if tag.artist else None
    title = tag.title if tag.title else None
    return artist, title

def create_videos(image_path, audio_folder, output_folder):
    for audio_file in os.listdir(audio_folder):
        if audio_file.lower().endswith(('.mp3', '.ogg', '.wav', '.flac')):
            audio_filename = os.path.join(audio_folder, audio_file)
            artist, title = get_title(audio_filename)
            if artist and title:
                output_name = f"{artist} - {title}.mp4"
            else:
                output_name = os.path.splitext(audio_file)[0] + ".mp4"

            audio_clip = AudioFileClip(audio_filename)
            img_clip = ImageClip(image_path).set_duration(audio_clip.duration)
            video_clip = img_clip.set_audio(audio_clip)

            output_file = os.path.join(output_folder, output_name)
            video_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24)

    print("Video creation complete.")

if len(sys.argv) == 4:
    image_location = sys.argv[1]
    input_directory = sys.argv[2]
    output_directory = sys.argv[3]

    create_videos(image_location, input_directory, output_directory)
else:
    print("Please provide the image location, input directory, and output directory as arguments.")
