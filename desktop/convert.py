import os
from PIL import Image
import pyheif

folder_path = "/home/owner/Project/Reminiscia/album/"

# for file_name in os.listdir(folder_path):
#     if file_name.endswith(".HEIC"):
#         heif_file = pyheif.read(folder_path + file_name)
#         image = Image.frombytes(
#             heif_file.mode, 
#             heif_file.size, 
#             heif_file.data,
#             "raw",
#             heif_file.mode,
#         )
#         new_file_name = file_name.split(".")[0] + ".jpg"
#         image.save(folder_path + new_file_name, "JPEG")


for i, file in enumerate(os.listdir(folder_path)):
    ext = os.path.splitext(file)[1]
    new_name = "{:03d}{}".format(i+1, ext)
    os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))


print("Conversion complete!")
