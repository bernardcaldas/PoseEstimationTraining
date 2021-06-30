# PoseEstimationTraining
Using a detector, the pipeline first locates the person/pose region-of-interest (ROI) within the frame. The tracker subsequently predicts the pose landmarks within the ROI using the ROI-cropped frame as input. Note that for video use cases the detector is invoked only as needed, i.e., for the very first frame and when the tracker could no longer identify body pose presence in the previous frame. For other frames the pipeline simply derives the ROI from the previous frame’s pose landmarks.

## Results
Pose estimation can be used in a lot applications;
### Boxing Training 
![Screenshot](/results/out.gif)
### Soccer Player
![Screenshot](/results/gifSoccerPlayer.gif)
### Exercices samples
![Screenshot](/results/pose_tracking_example.gif)

## About 
The solution utilizes a two-step detector-tracker ML pipeline, proven to be effective in our MediaPipe Hands and MediaPipe Face Mesh solutions. Using a detector, the pipeline first locates the person/pose region-of-interest (ROI) within the frame. The tracker subsequently predicts the pose landmarks within the ROI using the ROI-cropped frame as input. Note that for video use cases the detector is invoked only as needed, i.e., for the very first frame and when the tracker could no longer identify body pose presence in the previous frame.
  To evaluate the quality of our models against other well-performing publicly available solutions, we use three different validation datasets, representing different verticals: Yoga, Dance and HIIT. Each image contains only a single person located 2-4 meters from the camera. To be consistent with other solutions;
  
  The landmark model in MediaPipe Pose predicts the location of 33 pose landmarks (see figure below).
![Screenshot](/results/pose_tracking_full_body_landmarks.png)  

## Instalation 
```
pip install requirements.txt
```
