import os
from PIL import Image
import clip
import torch

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
print(clip.available_models())
model, preprocess = clip.load('ViT-B/16', device)

# Load the album
album = os.getcwd() + "/album"
image_size = len(os.listdir(album))
print(f"Found {image_size} images")
batch_size = 16
images_input = torch.zeros([batch_size,3,224,224]).to(device)
final_image_features = []
i = 0
for filename in os.listdir(album):
    # Open the image file using PIL
    image_path = os.path.join(album, filename)
    image = Image.open(image_path)
    images_input[i%16] = preprocess(image).to(device)
    i = i + 1
    if i % batch_size == 0 or i == image_size:
        with torch.no_grad():
            final_image_features += model.encode_image(images_input) # [B, 512]
        print("Finished one batch")
        images_input = torch.zeros([min(batch_size,image_size-i),3,224,224]).to(device)
# final_image_features = torch.cat(final_image_features)

# save the tensor to a file
torch.save(torch.stack(final_image_features), 'image_features.pt') # [N, 512]