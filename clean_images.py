from PIL import Image
import os

def resize_image(final_size, image):
    '''A function that resizes the images in the image dataset
    
    Args:

    Returns:
        new_image (image): image resized to desired pixel size (512)
    '''
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
    final_size = 512 # resizes image to 512 x 512 pixels

    new_path = "image_dataset/cleaned_images/"
    if not os.path.exists(new_path):
        os.mkdir(new_path)

    for item in enumerate(dirs[:5], 1): # index has to be changed to limit/increase number of processed images
        try:
            image = Image.open(path + item)
            new_image = resize_image(final_size, image)
            new_image.save(f'{new_path}{item}_resized.jpg')
        except:
            print(f'Resizing failed for {item}.')
            continue