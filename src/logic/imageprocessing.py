from printerimage import *

class ImageConverter:

    @staticmethod
    def load_from_file(filepath: str) -> PrinterImage:
        image = Image.open(filepath)
        image = ImageOps.grayscale(image)
        return ImageConverter._image_to_printer_format(image)

    @staticmethod
    def _image_to_printer_format(image: Image.Image) -> PrinterImage:
        width, height = image.size

        pixels = image.tobytes()
        bits = bytearray(pixels)

        return PrinterImage(width=width, height=height, bits=bits)