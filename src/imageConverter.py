from PIL import Image

class ImageConverter:

    def convert(oldFile, fmt, newFile):
        if(fmt != 'png'):
            im = Image.open(oldFile)
            rgb_im = im.convert('RGB')
            rgb_im.save(newFile)
