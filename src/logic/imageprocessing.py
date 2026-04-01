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
        threshold = 127
        # pixels = image.tobytes()
        bits = [
        bytearray(
            [
                1 if image.getpixel((x, y)) > threshold else 0
                for x in range(width)
            ]
        )
        for y in range(height)
    ]

        return PrinterImage(width=width, height=height, bits=bits)