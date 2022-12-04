from PIL import Image
import os

def resize_image(final_size, image):
    size = image.size
    ratio = float(final_size) / max(size)
    new_image_size = tuple([int(x*ratio) for x in size])
    image = image.resize(new_image_size, Image.ANTIALIAS)
    new_image = Image.new("RGB", (final_size, final_size))
    new_image.paste(image, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
    return new_image

if __name__ == '__main__':
    path = "image_dataset/raw_dataset/"
    dirs = os.listdir(path)
    final_size = 512

    new_path = "image_dataset/cleaned_images/"
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    