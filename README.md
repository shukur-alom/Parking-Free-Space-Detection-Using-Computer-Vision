# Parking Space Monitoring

This project utilizes the custom object detection model to monitor parking spaces in a video feed. It identifies vehicles in the video and overlays polygons representing parking spaces on the frames. The program then calculates the number of occupied and free parking spaces based on the detected vehicles and the predefined parking space polygons.

![System view](https://github.com/shukur-alom/parking-counter/blob/master/Media/system%20view.png)

## Requirements

- Python 3.x

## Setup

1. Install our module dependencies:

```pip
pip install kawarizmi
``` 

## Usage

1. Run the Code.

```python
import kawarizmi

kawarizmi.parking_space_counter(video_path="your_video_path")

```

if you don't put any path. the code automatically chooses your camera source.

- Click on the video feed to define the parking space polygons.
- Press 'S' to save the defined polygons.
- Press 'R' to remove the last saved polygon.
- Press 'Q' to quit the program.


## Additional Notes

- Ensure that the video feed contains clear and distinguishable parking spaces for accurate detection.
- You can adjust the object detection thresholds and other parameters in the code according to your requirements.


## Contributors

- [Shukur Alam](https://github.com/shukur-alom)