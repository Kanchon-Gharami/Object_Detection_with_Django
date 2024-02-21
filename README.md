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
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

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
