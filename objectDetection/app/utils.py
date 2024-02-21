import os
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn
from torchvision.transforms import functional as F
from PIL import Image, ImageDraw
from django.conf import settings
from .models import Image as ImageModel

# Assuming you have a directory named 'model_cache' in your BASE_DIR for models
MODEL_DIR = os.path.join(settings.BASE_DIR, 'model_cache')
MODEL_PATH = os.path.join(MODEL_DIR, 'fasterrcnn_resnet50_fpn.pth')

# Example COCO labels for demonstration
COCO_INSTANCE_CATEGORY_NAMES = [
    'background', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
    'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant',
    'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse',
    'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack',
    'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard',
    'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard',
    'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork',
    'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange',
    'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair',
    'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop',
    'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven',
    'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
    'teddy bear', 'hair drier', 'toothbrush', 'plant', 'toy', 'pen', 'pencil'
]

def load_model():
    if not os.path.exists(MODEL_PATH):
        os.makedirs(MODEL_DIR, exist_ok=True)
        model = fasterrcnn_resnet50_fpn(pretrained=True)
        torch.save(model.state_dict(), MODEL_PATH)
    else:
        model = fasterrcnn_resnet50_fpn(weights=None)
        model.load_state_dict(torch.load(MODEL_PATH))
    model.eval()
    return model

def processed_image(image_id):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = load_model().to(device)
    
    # Fetch and open the image
    image_instance = ImageModel.objects.get(id=image_id)
    img = Image.open(image_instance.picture.path).convert("RGB")
    img_tensor = F.to_tensor(img).unsqueeze(0).to(device)
    
    # Inference
    with torch.no_grad():
        prediction = model(img_tensor)
    
    # Drawing setup
    draw = ImageDraw.Draw(img)
    detected_objects = []

    for element, label_id, score in zip(prediction[0]['boxes'], prediction[0]['labels'], prediction[0]['scores']):
        if score > 0.5:  # Confidence threshold
            box = element.cpu().numpy().astype(int)
            # Safely get label names, default to 'unknown' if out of range
            label_name = COCO_INSTANCE_CATEGORY_NAMES[label_id] if label_id < len(COCO_INSTANCE_CATEGORY_NAMES) else 'unknown'
            draw.rectangle([(box[0], box[1]), (box[2], box[3])], outline="red", width=3)
            draw.text((box[0], box[1] - 10), f"{label_name}: {score:.2f}", fill="red")
            detected_objects.append(f"{label_name}: {score:.2f}")


    # Save the processed image
    processed_image_folder = os.path.join(settings.MEDIA_ROOT, 'processed_images')
    os.makedirs(processed_image_folder, exist_ok=True)  # Create the directory if it does not exist

    original_file_name = os.path.basename(image_instance.picture.name)
    processed_image_name = f"processed_{original_file_name}"
    processed_image_path = os.path.join(processed_image_folder, processed_image_name)

    img.save(processed_image_path)  # Save the processed image

    # Update the ImageModel instance
    image_instance.processed_picture.name = os.path.join('processed_images', processed_image_name)
    image_instance.save()

    return detected_objects, image_instance.id
