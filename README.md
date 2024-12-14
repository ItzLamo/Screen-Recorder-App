# Simple Screen Recorder

This is an enhanced screen recorder application built using Python and Tkinter. The app allows users to record their screen, capture screenshots, and preview the last recorded video. It also provides a simple, intuitive graphical user interface (GUI) for easy interaction.

## Features

- **Start and Stop Recording**: Allows you to start and stop screen recording easily.
- **FPS Control**: Adjust the frame rate of the recording via a slider.
- **Screenshot Capture**: Take a screenshot during the recording session and save it to a designated folder.
- **Preview Last Recording**: View the last recorded video using the default media player.
- **Theme Toggle**: Switch between dark and light themes to suit your preference.
- **File Path Selection**: Choose the location and name of the output file for your recording.

## Requirements

To run the application, you will need Python installed on your machine along with the following Python libraries:

- `pyscreenrec`: For screen recording functionality.
- `tkinter`: For building the graphical user interface.
- `PIL (Pillow)`: For screenshot functionality.
- `webbrowser`: For opening the preview file.

Install the required dependencies using the following command:

```bash
pip install pyscreenrec Pillow
```

`tkinter` comes pre-installed with Python, so there's no need to install it separately.

## Usage

1. **Browse for File Path**: Click on the "Browse" button to select the file path where you want to save the screen recording.
2. **Adjust FPS**: Use the FPS slider to adjust the frames per second for the recording.
3. **Start Recording**: Click on the "Start Recording" button to begin recording your screen.
4. **Stop Recording**: Click on the "Stop Recording" button to stop the recording session.
5. **Capture Screenshot**: Click on the "Capture Screenshot" button to take a screenshot during the recording.
6. **Preview Last Recording**: Click on the "Preview Last Recording" button to open the last saved recording.
7. **Toggle Theme**: Click on the "Toggle Theme" button to switch between dark and light modes.
