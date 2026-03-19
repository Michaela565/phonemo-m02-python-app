from phonemo import PhonemoPrinter


ports = PhonemoPrinter.list_available_ports()
for port in ports: print(port)
print('Select your Phonemo printer')
port = input()
printer = PhonemoPrinter(port=port)

try:
    printer.connect()

except Exception as e:
    print(e)

finally:
    printer.disconnect()

