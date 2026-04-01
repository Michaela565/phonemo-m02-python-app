import serial
from typing import Optional
from printerimage import PrinterImage

class PhonemoPrinter:
    def __init__(self, port: Optional[str] = None, baudrate: int = 9600):
        self.port = port
        self.baudrate = baudrate
        self.serial: Optional[serial.Serial] = None

    def connect(self) -> None:
        if self.serial is not None and self.serial.is_open:
            print("Already connected to printer")
            return
        
        try:
            if self.port is None:
                raise RuntimeError("No port given.")
            self.serial = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=1.0)
            print(f"Connected to printer {self.port}")
        
        except serial.SerialException as e:
            raise RuntimeError(f"Failed to connect to printer: {e}")


    def disconnect(self) -> None:
        self.is_connected()
        self.serial.close()
        self.serial = None
        print("Disconnected printer.")

    def is_connected(self) -> bool:
        if not (self.serial and self.serial.is_open):
            raise RuntimeError("Not connected to printer")
        return True

    def get_firmaware_verion(self) -> None:
        self.is_connected()
        
        self.serial.write(bytes([0x1f, 0x11, 0x07]))

        response = self.serial.read(5)
        if response and len(response) >= 5:
            return f"{response[4]}.{response[3]}.{response[2]}"
        raise RuntimeError("Failed to read firmware version.")
        

    def get_battery_level(self) -> None:
        self.is_connected()
        
        self.serial.write(bytes([0x1f, 0x11, 0x08]))
        
        response = self.serial.read(3)

        if response and len(response) >= 3:
            return response[2]
        raise RuntimeError("Failed to read battery level.")

    def get_serial_number(self) -> None:
        self.is_connected()

        self.serial.write(bytes([0x1f, 0x11, 0x13]))

        response = self.serial.read(3)

        if response and len(response) >= 3:
            return response[2] | (response[1] << 8) | (response[0] << 16)
        raise RuntimeError("Failed to read battery level.")

    def get_paper_state(self) -> None:
        self.is_connected()

        self.serial.write(bytes([0x1f, 0x11, 0x11]))

        response = self.serial.read(3)

        if response and len(response) >= 3:
            return response[2] | (response[1] << 8) | (response[0] << 16)
        raise RuntimeError("Failed to read battery level.")

    def initialize(self) -> None:
        self.is_connected()

        self.serial.write(bytes([0x1b, 0x40]))
        print("Successfully initiated.")


    def alignCenter(self) -> None:
        self.is_connected()

        self.serial.write(bytes([0x1b, 0x61, 0x01]))
        print("Successfully aligned center.")

    def print_image(self, image: PrinterImage) -> None:
        self.is_connected()
        self.initialize()
        self.alignCenter()

        if image.width % 8 != 0:
            raise RuntimeError("Image width must be a multiple of 8.")

        # if len(image.bits) != (image.width/8) * image.height:
        #     raise RuntimeError("Image bits length does not match width and height.")
        mode = 0
        byteWidth = image.width // 8
        height = image.height

        imageData = bytearray([
            0x1d,
            0x76,
            0x30,
            mode,
            byteWidth & 0xff,
            (byteWidth >> 8) & 0xff,
            height & 0xff,
            (height >> 8) & 0xff])

        for line in range(height):
            for byte_num in range(byteWidth):
                byte = 0
                for bit in range(8):
                    pixel = image.bits[line][byte_num * 8 + bit]
                    byte |= (pixel & 0x01) << (7 - bit)

                imageData.append(byte)

        # imageData.extend(image.bits)
        self.serial.write(imageData)

    def print_feed_lines(self, num: int) -> None:
        self.is_connected()
        if num < 0 or num > 255:
            raise RuntimeError("Number of lines must be between 0 and 255.")
        
        self.serial.write(bytes([0x1b, 0x64, num]))

    @staticmethod
    def list_available_ports() -> list[str]:
        import serial.tools.list_ports
        ports = [port.device for port in serial.tools.list_ports.comports()]
        return ports
    