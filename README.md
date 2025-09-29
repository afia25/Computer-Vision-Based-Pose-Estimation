## Computer-Vision-Based-Pose-Estimation

This work demonstrates real-time human pose estimation using Python. This is done by capturing frames from videos, calculate FPS, and run MediaPipe’s pose estimation model. Landmarks (33 body keypoints) are detected in real time, drawn on the frame with connections (skeleton), and tested across multiple videos. <br>

### Models and libraries used
**Libraries: <br>
OpenCV (cv2)**: for video capture, image processing, drawing text, shapes, and showing output. <br>
**MediaPipe:** for the pose estimation model and utilities to draw landmarks and connections. <br>
**time:** to calculate frames per second (FPS). 

**Model: <br>
MediaPipe Pose**: a lightweight deep learning model capable of detecting 33 landmarks on the human body. The model works with both detection and tracking modes for efficiency. Detection mode finds new poses. Tracking mode follows existing ones, saving computation.

### Methodology
1. Frame Capture & FPS Calculationcv2.VideoCapture() is used to read video frames. cv2.imshow() displayed frames. FPS is tracked using time difference between frames.
2. Pose Detection PipelineAt first BGR frames were converted into RGB. These RGB frames were passed  through mp.solutions.pose.Pose().process() in order to get 33 landmarks with (x, y, z, visibility) values. Then normalized coordinates were scaled into pixel coordinates (using image width and height).

3. Drawing Landmarks mp.solutions.drawing_utils.draw_landmarks() was used to overlay joints and skeleton lines.
4. Object-Oriented Module CreationI used the pipeline in a PoseDetector class with parameters for mode, upper body, smoothing, detection confidence, and tracking confidence. Methods like findPose() encapsulated the detection logic. The class was reused across test videos to streamline future projects.

Result
The final result of this model is the detection of 33 pose landmarks (joints such as nose, eyes, ears, shoulders, elbows, hips, knees, ankles, etc.) in real-time video at ~24 FPS on CPU.Skeleton connections drawn between the landmarks.This model can do smooth tracking of body joints across frames.The FPS counter shows performance, proving it runs efficiently on CPU without GPU acceleration.The modular class (PoseDetector) makes it simple to reuse the code for future projects like gesture recognition, fitness tracking, or AR applications.


