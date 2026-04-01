from phonemo import PhonemoPrinter
from printerimage import *
from imageprocessing import *

ports = PhonemoPrinter.list_available_ports()
for port in ports: print(port)
print('Select your Phonemo printer')
port = input()
printer = PhonemoPrinter(port=port)

def basic_test():
    printer.connect()
    fv = printer.get_firmaware_verion()
    print(fv)
    bl = printer.get_battery_level()
    print(bl)
    sn = printer.get_serial_number()
    print(sn)
    ps = printer.get_paper_state()
    print(ps)
    printer.initialize()
    printer.alignCenter()

def image_test():
    image = ImageConverter.load_from_file("G:\pain in programming\phonemo-m02-python-app\src\logic\miku.jpg")
    print(image.height)
    print(image.width)
    print(image.bits)

def print_test():
    printer.connect()
    fv = printer.get_firmaware_verion()
    print(fv)
    bl = printer.get_battery_level()
    print(bl)
    sn = printer.get_serial_number()
    print(sn)
    ps = printer.get_paper_state()
    print(ps)
    image = ImageConverter.load_from_file("G:\pain in programming\phonemo-m02-python-app\src\logic\miku1.jpg")
    printer.print_image(image)

try:
    print_test()

    

except Exception as e:
    print(e)

finally:
    printer.disconnect()

