import os
import clip
import torch
import time
import sys

query = "A photo of New York skyline"
if len(sys.argv) != 2:
    print("Usage: python my_script.py <argument>")
else:
    query = sys.argv[1]

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
print(clip.available_models())
model, preprocess = clip.load('ViT-B/16', device)

start_time = time.time()
text_input = clip.tokenize(query).to(device)
# Calculate features
with torch.no_grad():
    text_feature = model.encode_text(text_input) # [1,512]
end_time = time.time()
print(f"\nText Encoding took: {(end_time-start_time):.3f} seconds")

# Load image features
image_features = torch.load('./image_features.pt').to(device)

start_time = time.time()
# Pick the top 5 most similar images for the query
image_features /= image_features.norm(dim=-1, keepdim=True) # [N,512]
text_feature /= text_feature.norm(dim=-1, keepdim=True) # [1,512]
similarity = (100.0 * image_features @ text_feature.T).softmax(dim=0) # [N,1]
values, indices = similarity.T[0].topk(5)
end_time = time.time()
print(f"Index Searching took: {(end_time-start_time):.3f} seconds")

# Print the result
print(f"\n{query}:")
for value, index in zip(values, indices):
    print(f"{(index+1):03d}: {100 * value.item():.2f}%")