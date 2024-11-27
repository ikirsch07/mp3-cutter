from moviepy import AudioFileClip
import os
import argparse

def time_to_seconds(time_str):
    """Convert a time string (HH:MM:SS or MM:SS) to seconds."""
    parts = time_str.split(':')
    if len(parts) == 2:
        minutes, seconds = parts
        return int(minutes) * 60 + int(seconds)
    elif len(parts) == 3:
        hours, minutes, seconds = parts
        return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
    else:
        raise ValueError("Invalid time format")

def main(audio_file_path, playlist_file_path):
    # Open the MP3 file
    try:
        audio = AudioFileClip(audio_file_path)
    except Exception as e:
        print(f"Error loading audio file: {audio_file_path}.")
        return

    # Read the playlist file
    try:
        with open(playlist_file_path, 'r') as playlist_file:
            lines = playlist_file.readlines()
    except Exception as e:
        print(f"Error loading playlist file: File {playlist_file_path} not found.")
        return

    # Process each line in the playlist
    for i in range(len(lines)):
        start_line = lines[i].strip()
 
        # Parse start time, composer, and title
        start_time_str, composer_title = start_line.split(' ', 1)

        # Convert start time to seconds
        start_time_sec = time_to_seconds(start_time_str)

        # Determine end time
        if i < len(lines) - 1:
            end_line = lines[i + 1].strip()
            end_time_str, _ = end_line.split(' ', 1)
            end_time_sec = time_to_seconds(end_time_str)
        else:
            # If it's the last piece, set the end time to the duration of the audio
            end_time_sec = audio.duration

        # Cut the audio segment
        print(f"cutting from {start_time_sec} to {end_time_sec}")
        extract = audio.subclipped(start_time_sec, end_time_sec)

        # Create a valid filename
        filename = f"{composer_title}.mp3".replace(':', '-').replace('/', '-')

        # Save the extracted segment
        save_path = os.path.join(os.path.dirname(audio_file_path), filename)
        extract.write_audiofile(save_path, codec="mp3")
        print(f"Saved: {save_path}")

    # Close the audio file
    audio.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cut an MP3 file into segments based on a playlist.")
    parser.add_argument("audio_file", help="Path to the MP3 file")
    parser.add_argument("playlist_file", help="Path to the playlist text file")
    args = parser.parse_args()

    main(args.audio_file, args.playlist_file)

