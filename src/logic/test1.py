from phonemo import PhonemoPrinter


ports = PhonemoPrinter.list_available_ports()
for port in ports: print(port)
print('Select your Phonemo printer')
port = input()
printer = PhonemoPrinter(port=port)

try:
    printer.connect()
    fv = printer.get_firmaware_verion()
    print(fv)
    bl = printer.get_battery_level()
    print(bl)
    sn = printer.get_serial_number()
    print(sn)
    ps = printer.get_paper_state()
    print(ps)

except Exception as e:
    print(e)

finally:
    printer.disconnect()

