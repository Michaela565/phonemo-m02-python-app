from PIL import Image, ImageOps

class PrinterImage:
    def __init__(self, height: int, width: int, bits: list[bytearray]):
        self.height = height
        self.width = width
        self.bits = bits

class ImageConversionOptions:
    def __init__(self, rotation: int = 0, threshold: int = 128, invert: int = False, algorithm: str = "bayer",
                 contrast: float = 1.0, exposure: float = 1.0, heightPercentage: int = 100, widthPercentage: int = 100,
                 paperThickness: str = "none", preprocessFilter: str = "none", filterOrder: str = "before-resize",
                 imageSmoothingEnabled: bool = True, imageSmoothingQuality: str = 'high', resizeAlgorithm: str = 'canvas',
                 sharpenBeforeResize: str = 'none', sharpenAfterResize:str = 'none', autoLevels: bool = False,
                 autoContrast: bool = False, autoExposure: bool = False):
        self.rotation = rotation
        self.threshold = threshold
        self.invert = invert
        self.algorithm = algorithm
        self.contrast = contrast
        self.exposure = exposure
        self.heightPercentage = heightPercentage
        self.widthPercentage = widthPercentage
        self.paperThickness = paperThickness
        self.preprocessFilter = preprocessFilter
        self.filterOrder = filterOrder
        self.imageSmoothingEnabled = imageSmoothingEnabled
        self.imageSmoothingQuality = imageSmoothingQuality
        self.resizeAlgorithm = resizeAlgorithm
        self.sharpenBeforeResize = sharpenBeforeResize
        self.sharpenAfterResize = sharpenAfterResize
        self.autoLevels = autoLevels
        self.autoContrast = autoContrast
        self.autoExposure = autoExposure
