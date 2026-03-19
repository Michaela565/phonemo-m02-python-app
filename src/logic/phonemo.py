import serial
from typing import Optional

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
        if self.is_connected():
            self.serial.close()
            self.serial = None
            print("Disconnected printer.")

    def is_connected(self) -> bool:
        return self.serial and self.serial.is_open

    def get_firmaware_verion(self) -> None:
        if not self.is_connected():
            raise RuntimeError("Not connected to printer")
        
        self.serial.write(bytes([0x1f, 0x11, 0x07]))

        response = self.serial.read(5)
        if response and len(response) >= 5:
            return f"{response[4]}.{response[3]}.{response[2]}"
        raise RuntimeError("Failed to read firmware version.")
        

    def get_battery_level(self) -> None:
        if not self.is_connected():
            raise RuntimeError("Not connected to printer")
        
        self.serial.write(bytes([0x1f, 0x11, 0x08]))
        
        response = self.serial.read(3)

        if response and len(response) >= 3:
            return response[2]
        raise RuntimeError("Failed to read battery level.")

    def get_serial_number(self) -> None:
        pass

    def get_paper_state(self) -> None:
        pass

    def initialize(self) -> None:
        pass

    def reset(self) -> None:
        pass

    def alignCenter(self) -> None:
        pass

    def print_image(self) -> None:
        pass

    def print_feed_lines(self) -> None:
        pass

    @staticmethod
    def list_available_ports() -> list[str]:
        import serial.tools.list_ports
        ports = [port.device for port in serial.tools.list_ports.comports()]
        return ports
    