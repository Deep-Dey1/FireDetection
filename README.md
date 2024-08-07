# Real-Time Fire Detection via UAV with Edge Computing

I am thrilled to share a project I've been working on that combines the power of machine learning, UAV (Unmanned Aerial Vehicle) technology, and edge computing to create a real-time alert generation system for fire detection and potentially other natural disasters.

## Project Overview

Using the UAV fire datasets from Kaggle and the YOLOv8 model, I trained a fire detection model on Google Colab. The training process involved fine-tuning the model with a custom dataset to accurately detect fire in various conditions. The model was then integrated into a script that processes video frames in real-time and sends an immediate SMS alert if fire is detected.

## Main Motive

The primary motivation behind this project is to tackle the problem of efficiently responding to natural disasters through UAV technology. My goal was to implement a system capable of real-time alert generation via UAV surveys, sending immediate notifications to ground laboratories upon detecting fires or other natural disasters using edge computing.

## Small-Scale Demonstration

To demonstrate this concept, I created a small-scale version of the system:

- **Processing:** Utilized my laptop for processing instead of an edge microcontroller.
- **Data:** Used publicly available UAV datasets from Kaggle instead of a UAV’s real-time camera.
- **Alert:** Configured the system to send alerts to my Android device instead of a ground laboratory.

## Key Features

- **Real-Time Detection:** The model processes video frames in real-time to detect fires.
- **Immediate Alerts:** Upon detecting a fire, the system sends an immediate SMS alert using Twilio’s API.
- **Versatility:** The system can be adapted for various natural disasters and integrated with other edge devices for broader applications.

## Code Overview

The script captures video frames, processes them through the YOLO model to detect fire, and draws bounding boxes around detected areas. If fire is detected with high confidence, the script sends an SMS alert using Twilio's API, ensuring the alert is sent only once per detection session.

This project showcases the potential of integrating advanced technologies for disaster management and mitigation. It’s a step towards building more resilient and responsive systems to protect our communities and environment.

I look forward to any feedback or suggestions 🌟
