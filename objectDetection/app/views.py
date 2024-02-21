from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import ImageUploadForm
from .forms import ImageUploadForm
from .models import Image
from . import utils
# Create your views here.

def index(request):
    return render(request, 'index.html')


@csrf_exempt
def image_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            redirect_url = reverse('image_info', args=[image_instance.id])
            return JsonResponse({'status': 'success', 'message': 'Image uploaded successfully', 'redirect_url': redirect_url})
        else:
            return JsonResponse({'status': 'error', 'message': 'Image upload failed'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def image_info(request, image_id):
    detected_objects, processed_image_id = utils.processed_image(image_id)
    original_image = Image.objects.get(id=image_id)
    processed_image = Image.objects.get(id=processed_image_id) 

    context = {
        'original_image': original_image,
        'processed_image': processed_image,
        'detected_objects': detected_objects,
    }
    return render(request, 'image_info.html', context)