# Driver Drowsiness Alarm

## Overview

This Python script utilizes computer vision and facial landmarks detection to determine the drowsiness level of a person in a real-time video stream. The system analyzes eye blink patterns to identify whether the person is awake, sleepy, or drowsy. It employs the dlib library for face detection and shape prediction, OpenCV for image processing, NumPy for numerical operations, and Pygame for sound playback.

## Requirements

Make sure you have the following libraries installed with the specified versions. You can install them using the provided `requirements.txt` file:

```
pip install -r requirements.txt
```
## Libraries and Versions
* `numpy==1.26.1`
* `opencv-python==4.8.1`
* `dlib==19.24.2`
* `imutils==0.5.4`
* `pygame==2.0.2`
## Uasge
1. Clone the repository or download the script.
2. Install the required libraries using the provided requirements.txt.
3. Download the `shape_predictor_68_face_landmarks.dat' file from dlib's official website and place it in the project directory.
4. Run the Script
   ```
   python main.py
   ```
5. Press `q` to exit.
## Sound Files
The script uses sound files for alerting the user. Ensure that the sound files `drowsy.mp3` and `sleepy.mp3` are present in the "media" directory.
