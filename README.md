# Object Detection Web Application

This Object Detection Web Application allows users to capture images via their webcam and utilizes a pre-trained machine learning model to detect and highlight objects within those images. Built with Django and leveraging advanced object detection models (such as YOLO or Faster R-CNN), this project demonstrates how to integrate cutting-edge AI technologies into a user-friendly web interface.

## Features

- **Webcam Image Capture**: Directly capture images from your webcam through the web interface.
- **Real-time Object Detection**: Utilize pre-trained object detection models to identify and label objects in the captured images.
- **Results Visualization**: Display the original and processed images side by side, with detected objects highlighted and labeled.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or newer
- Django 3.2 or newer
- Additional Python packages as listed in `requirements.txt`

### Installation

```bash
# Clone the Repository
git clone https://github.com/Kanchon-Gharami/Object_Detection_with_Django
cd objectDetection

# Set Up a Virtual Environment (optional but recommended)
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate

# Install Required Packages
pip install -r requirements.txt

# Migrate the Database
python manage.py migrate

# Run the Development Server
python manage.py runserver

# Visit http://127.0.0.1:8000/ in your web browser to view the application
```

### Usage
1. Navigate to the main page of the web application.
2. Click the "Capture Image" button to take a photo with your webcam.
3. View the processed image with detected objects and their labels displayed next to the original image.
4. Detected objects will be listed, providing insights into what the AI model has recognized in your image.


### Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

