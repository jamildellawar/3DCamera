from PIL import Image

class Images:
    def __init__(self, photoDirectory):
        self.photoDirectory = photoDirectory
        self.photo1 = None
        self.photo2 = None
        self.photo3 = None
        self.photo4 = None

    def separatePictures(self, counter):
        im = Image.open(self.photoDirectory)
        width, height = im.size
        self.photo1 = im.crop((0, 0, width / 2, height / 2))
        self.photo2 = im.crop((0, height/2, width / 2, height))
        self.photo3 = im.crop((width / 2, 0, width, height / 2))
        self.photo4 = im.crop((width / 2, height / 2, width, height))

        self.photo1.save(f'Photos/IMG_00{counter}1', 'JPEG')
        self.photo2.save(f'Photos/IMG_00{counter}2', 'JPEG')
        self.photo3.save(f'Photos/IMG_00{counter}3', 'JPEG')
        self.photo4.save(f'Photos/IMG_00{counter}4', 'JPEG')
