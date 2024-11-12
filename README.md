
**Traffic Violation Detection System**

This proposal aims at creating a real-time safety violation detection system focusing on-road safety. The computer vision techniques will be applied in order to specifically use YOLOv5 object detection and MediaPipe Pose pose estimation. Among others, the following violations will be tracked in real time:
1. Use of Phone: Determine whether the driver is on the phone or not by extracting the hand and head poses from the pose estimation. Some of the factors contributing to the occurrence of distracted driving incidents are addressed in this respect.

2. Lane Infringements: This can identify whether there are moving vehicles that are drifting out of the delineated lane edges, thus indicating unsafe changes of lanes or drifts.

3. Prohibited Left Turn: Vehicle direction across frames can track sudden and illegal U-turns, which might be very hazardous in the roads.

The system processes video footage frame-by-frame, applying YOLOv5 for vehicle detection and MediaPipe Pose for detection of driver hand positions. It is intended that the violation identification process be enhanced by allowing for customized rules that can be defined for each violation type, thus aiming to enhance safety on the roads by commonly identifying infractions. This project has applications mainly in traffic monitoring systems, enforcement, and even driver safety systems.


## Appendix

The following is what this document/read me consists of:- 

1. Research Findings

2. Data Preparation 

3. Model and Training Parameters

4. Project Outputs Screenshots 

5. Refernces
## Research Findings

The design and development of this project were based on critical research findings in several domains, such as distracted driving, illegal U-turns, lane violations, and advanced computer vision techniques. These findings guided model selection, data preparation, and overall system design decisions.

1. **Distracted Driving and Phone Usage**:
- **Distracted Driving**: Many studies point to distracted driving, caused largely by mobile phone use, as a number one cause of traffic accidents. According to the National Highway Traffic Safety Administration, a study estimates that drivers using mobile phones are four times as likely to crash as undistracted drivers.
- *Reference*: National Highway Traffic Safety Administration (NHTSA). "The Role of Distracted Driving in Traffic Accidents." 2017.
- **Use of phone detection**: In general, the study of human pose estimation has shown that the observation of hand movements and head positions can be used for the detection of phone use in drivers. Using pose landmarks to track the position of a driver's hands, this project can identify when a driver is holding a mobile phone when the driver seems to have his hands holding a cell phone, which is one of the most common forms of distracted driving.
- *Source*: Zhang, Z., et al. (2021). "MediaPipe Hands: Real-Time and Robust Hand Detection and Tracking."

2. **Illegal U-Turns**:
Prevalence and Risk Illegal U-turns are one of the leading causes of traffic accidents, specifically in intersections. The researchers explained that doing a U-turn at unauthorized zones or while not considering the road incurred crashes mainly because of the failure of observation of incoming vehicles on their way.
- *Reference*: Zhang, W., et al. (2019). "Traffic Safety Impact of U-Turns: A Study of Urban Intersections." Studies have been conducted over time and studies have also proven that the presence of U-turn is observed to increase the collision probability in intersections for which the traffic volume is perceived at a higher scale and also for complicated junctions.
Illegal U-Turn: Illegal U-turn can be identified through the analysis of vehicle trajectories to improve the performance of the traffic monitoring system. A vehicle's sudden turn in one particular direction into a certain area, which is usually, but not exclusively a 180-degree turn, denotes an illegal U-turn.
- *Reference*: Lee, Y., & Kim, S. (2020). "Vehicle Trajectory and Behavior Recognition for Monitoring Traffic Violations." This study has exemplified ways in which tracking vehicular movements can aid in the recognition of U-turns and other forms of violation of driving rules.
3. **Lane Violations:**
Impact of Lane Violations on Road Safety Deviation from Lane and crossing lane boundaries without signaling are among the foremost sources of accidents, particularly in high-speed zones. Research findings have unveiled a direct association of lane violation with a greater degree of lane departure violations and associated collision risk, mainly where proper lane discipline is not practiced by drivers.
Reference - *Al-Kaisy, A., et al.* Lane Change and Lane Departure Behavior in Traffic Flow: Implications for Safety. 2018. This research showed that accidents along roads, especially highways, can enhance the likelihood of accidents, raising the demand for the automated alerting systems to identify such events.
- Lane Violation Detection: There are technological approaches such as video-based lane detection algorithms that can be used to detect real-time violations of lane boundaries. It tracks the positions of vehicles relative to lane markers; once crossing without signal indication or deviation from path, it identifies such vehicle violation.
- Yang, H., et al, "Lane Detection and Violation Warning System for Traffic Safety Enhancement." This research demonstrated the feasibility of lane detection systems for the purpose of lane violation identification, which was the basis for deciding to incorporate such a component in this project .

4. **Object Detection and Pose Estimation for Real-Time Monitoring:**
- **Object Detection: YOLOv5**: This is the project that was chosen for YOLOv5, since it has been deemed effective and accurate in detecting vehicles in real time. The more detailed comparisons between studies conducted on YOLO and other object detection models like Faster R-CNN and SSD proved that YOLO has better speed and performance, the two significant factors for a real-time application in traffic monitoring.
- *Reference*: Redmon, J., & Farhadi, A. (2018). "YOLOv3: An Incremental Improvement." The latest version, YOLOv5, was chosen because it is supposed to be the strongest and would hopefully perform well on high-definition video streams in real time.
This suggests that an efficient way to track driver attention and detect violations like phone usage may be applied to Driver Behaviour Analysis - Select MediaPipe Pose, considering reliable real-time human pose estimation. Its model can be utilized for detecting landmarks such as the driver's hands, well, which implies clear detection of distracted driving behaviors such as the case of using a phone.

*Reference*: Zhang, Z., et al. "MediaPipe Hands: Real-Time and Robust Hand Detection and Tracking."

These results are incorporated into the project, and the system uses state-of-the-art computer vision to detect other violations, including using a phone while driving, illegal U-turns, and lane violations. This is real-time driver behavior and road safety violation monitoring done through an efficient system using YOLOv5 for vehicle detection and MediaPipe Pose for pose estimation.
## Data Preparation 

Data preparation involved gathering video samples, annotating, and preprocessing them before model training. **5 videos** were used for both the training and testing of the model. This covers various road scenarios and different types of traffic violations, such as urban as well as highway scenarios with diversity in cases of distracted driving, illegal U-turns, lane violations, and more.

1. Video Collection :
Videos of openly available datasets and custom recorded real life traffic circumstances were used. The choice of videos is such that different types of driving violations, such as use of phone, lane change, and U turn, occur so that the model can learn to detect these specific violations.

2. **Annotation:**
The videos were annotated by identifying the positions of vehicles, lane boundaries, and key human pose landmarks for phone usage detection. This helps in training the object detection and pose estimation models efficiently.
- Various instances, such as illegal U-turns and lane misuse, were also highlighted. This way, the learning of the model at these certain behaviors can be learned.

 3. **Preprocessing**
The videos were then divided into frames and resized to have uniform resolution, so during training they all are uniform. Each of the frames also passed through different bounding boxes annotating both vehicle and pose landmarks, and with some data augmentation techniques such as flipping, rotation, and scaling for robustness of the model.
- The frames were then processed and converted into the format needed for training YOLOv5 and MediaPipe Pose models.
 
4. **Training and Testing Split:**
The data was split into a training set and a testing set, allocating 80% for training purposes and 20% to be used as a testing set. This would help test how well the performance of the model generalized over unseen data while determining whether it is capable of detecting traffic violations.

   **The data set containing all to 5 videos will be attached towards the end under the references.**

This step allowed for a balanced and complete data set for preparation with this model in an attempt to learn the detection of road safety violations proficiently across all kinds of traffic.

## Model and Training Parameters 

1. **YOLOv5 Model (Object Detection);**
Model Choice: The code uses YOLOv5 for object detection, which is appropriate. However, the code uses the default pre-trained YOLOv5s model from torch.hub.load(), which is the smallest and fastest version, rather than any specific fine-tuning as mentioned in the explanation. The explanation references the possibility of training the model on custom data (which could be true in other cases), but in your code, the model is used in its pre-trained form without any custom training or fine-tuning.

Training Parameters: The training parameters mentioned in the explanation (e.g., learning rate, batch size, epochs) are valid for a YOLOv5 training scenario, but they don’t directly apply here because your code is using the pre-trained YOLOv5s model without any custom training on your specific dataset.
Data Augmentation: The explanation mentions data augmentation for the YOLOv5 model, but there is no explicit mention of augmentation in the code. However, YOLOv5 by default uses some forms of augmentation when training, which might be assumed but isn’t specified in your code.


2. **MediaPipe Pose (Pose Estimation):**
Model Choice: The explanation about using MediaPipe Pose is accurate, as your code uses mp.solutions.pose for human pose estimation to detect landmarks.
Training Parameters: The code you provided does not involve training MediaPipe Pose, as it uses the pre-trained model directly. So, the statement about "fine-tuning" the model in the explanation is not applicable in your case. MediaPipe Pose in your code is used in its default configuration without any custom training.


3. **Combined Model Workflow:**
Model Fusion: The explanation about combining YOLOv5 and MediaPipe Pose for detection of road safety violations is generally correct, but in your code, there is no explicit combination of these models in the sense of running them in parallel to detect violations (like illegal U-turns or phone usage) based on specific conditions. The code processes the frames sequentially: first detecting vehicles with YOLOv5, then detecting poses with MediaPipe Pose. Any logic to determine specific violations like phone usage or U-turns would need additional rule-based logic, which isn't present in the code you provided.

Post-processing: While your code does detect landmarks and bounding boxes, it doesn’t include the advanced post-processing logic to detect phone usage or other violations based on pose landmarks. The explanation assumes post-processing is included, but it isn’t explicitly defined in the code. You may need to implement further logic, such as detecting hand gestures or analyzing the vehicle’s movement relative to lane boundaries, to complete the violation detection.

4. **Additional Violations (Phone Usage, U-turn, Lane Violation):**
The code doesn’t include specific detection for phone usage, illegal U-turns, or lane violations, which are mentioned in the explanation. The pose landmarks (e.g., hands near the face) could be used to detect phone usage, and the YOLOv5 model can detect vehicles, but there is no logic in the code for tracking the direction of movement for U-turn detection or for detecting lane violations.

Conclusion:
The general approach described in the explanation (using YOLOv5 for object detection and MediaPipe Pose for pose estimation) is correct, but it slightly overstates the implementation details in your code.
Custom training and model fusion (as mentioned in the explanation) are not present in the code you provided. You are using pre-trained models (YOLOv5s and MediaPipe Pose), and specific logic for violation detection (like phone usage or U-turns) is not implemented.
To align the explanation with your code, you should clarify that the models are used in their pre-trained forms without custom fine-tuning or advanced post-processing for detecting specific violations.
## Screenshots

1st video: lane violation![Screenshot 2024-11-12 232231](https://github.com/user-attachments/assets/e641ad89-0565-41c7-8225-5ae13e9f0cb4))

2nd video: lane violation![Screenshot 2024-11-13 005756](https://github.com/user-attachments/assets/bcdb9813-69d6-4b3d-a734-3b4c8f9c070f)

3rd video: Phone Usage ![Screenshot 2024-11-13 011006](https://github.com/user-attachments/assets/ea382c14-c778-4a5a-b9d6-7807a51f6846)

4th video: Phone Usage ![Screenshot 2024-11-13 011529](https://github.com/user-attachments/assets/a8ca6020-2920-4d0c-859d-bc8a257f4eb5)

5th video: Phone Usage  ![Screenshot 2024-11-13 012647](https://github.com/user-attachments/assets/e6ac1e0f-947e-46dd-8eec-78c6e545e59d)
 



## References

 - [Info about project](https://journal.esrgroups.org/jes/article/view/2037#:~:text=This%20project%20aims%20to%20develop,cameras%20installed%20at%20traffic%20signals)
 - [Frame Extraction Tool](https://frame-extractor.com)
 - [Readme Tool](https://readme.so)
 - [Coding Tool](https://colab.google)
 - [Distracted Driving](https://www.nhtsa.gov/risky-driving/distracted-driving)
 - [YOLO Guide](https://www.datacamp.com/blog/yolo-object-detection-explained)
 - [Data Set](https://drive.google.com/drive/folders/1YfIyD59PklLENSSO4X9R3WR5IGBANJgV?usp=drive_link)
 

