# MP3 Cutter

This script allows you to cut an MP3 file into individual segments based on a playlist file. Each segment is saved as a separate MP3 file, labeled by the composer and title.

## Features

- Cuts an MP3 file into segments based on start times specified in a playlist.
- Saves each segment with a filename based on the composer and title.
- Uses `moviepy` for audio processing.

## Requirements

- Python 3.x
- `moviepy` library
- `ffmpeg` installed and accessible from the command line

## Installation

1. **Clone the Repository**:
```bash 
git clone https://github.com/yourusername/mp3-cutter.git
```

2. **Install Dependencies**:
   Ensure you have `moviepy` installed:
```bash 
pip install moviepy
```

3. **Install `ffmpeg`**:
   - **macOS**: Use Homebrew:
     ```bash
     brew install ffmpeg
     ```
   - **Windows**: Download from the [official website](https://ffmpeg.org/download.html) and add to PATH.
   - **Linux**: Use your package manager:
     ```bash
     sudo apt install ffmpeg
     ```

## Usage

1. **Prepare Your Files**:
   - Ensure you have an MP3 file and a playlist text file. The playlist should have lines formatted as `HH:MM:SS Composer - Title`.

2. **Run the Script**:
   Use the command line to run the script, providing the paths to the audio file and the playlist file as arguments:
bash python mp3_cutter.py path/to/audio.mp3 path/to/playlist.txt

   Example:
   ```bash 
   python mp3_cutter.py examples/vivaldi.mp3 examples/playlist.txt
   ```

3. **Output**:
   - The script will save each segment as an MP3 file in the same directory as the original audio file.

## Example Playlist Format
0:00:00 Bach - Cantata BWV 147: Jesu, Joy of Man's Desiring 0:04:17 Grieg - Peer Gynt Suite: Morning Mood 0:07:38 Rachmaninoff - Rhapsody on a Theme of Paganini: Var. XVIII …

## Troubleshooting

- **Error Loading Audio File**: Ensure `ffmpeg` is installed and the audio file is not corrupted.
- **Invalid Time Format**: Ensure the playlist times are formatted correctly as `HH:MM:SS` or `MM:SS`.

## License

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
