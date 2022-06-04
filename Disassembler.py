import dis, os, sys, re
reportfile = open('report.txt','w')
reportfile.write('# Report generated from KryptDis\n')
imports = []
links = []
if 'pyarmor_runtime' in dir(): reportfile.write('# PyArmor detected!\n')
for objectName in dir():
    if objectName in ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '__cached__', '__file__', 'imports', 'links', 'reportfile']: continue
    objectCall = eval(objectName)
    if type(objectCall).__name__ == 'module': imports.append(objectName); continue
    if re.match(r'(http|https|ftp)\://([a-zA-Z0-9\-\.]+\.+[a-zA-Z]{2,3})(:[a-zA-Z0-9]*)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~@]*)',str(objectCall)): links.append(str(objectCall))
    elif type(objectCall).__name__ == 'type':
        for objectName2 in dir(objectCall):
            if objectName2 in ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']: continue
            objectCall2 = eval(objectName2)
            if re.match(r'(http|https|ftp)\://([a-zA-Z0-9\-\.]+\.+[a-zA-Z]{2,3})(:[a-zA-Z0-9]*)?/?([a-zA-Z0-9\-\._\?\,\'/\\\+&amp;%\$#\=~@]*)',str(objectCall2)): links.append(str(objectCall2))
            if type(objectCall2).__name__ == 'function':
                try: assembly = '\n'+dis.Bytecode(objectCall2).dis()
                except Exception: assembly = 'Error disassembling bytecode!'
                reportfile.write(f'Class: {objectName}\nName: {objectName2}\nType: {str(type(objectCall2).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall2),16)}\nAssembly Report: {assembly}\n\n')
                print(f'Class: {objectName}\nName: {objectName2}\nType: {str(type(objectCall2).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall2),16)}\nAssembly Report: {assembly}\n\n')
            else:
                reportfile.write(f'Class: {objectName}\nName: {objectName2}\nType: {str(type(objectCall2).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall2),16)}\nContent: {str(objectCall2)}\n\n')
                print(f'Class: {objectName}\nName: {objectName2}\nType: {str(type(objectCall2).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall2),16)}\nContent: {str(objectCall2)}\n\n')
    if type(objectCall).__name__ == 'function':
        try: assembly = '\n'+dis.Bytecode(objectCall).dis()
        except Exception: assembly = 'Error disassembling bytecode!'
        reportfile.write(f'Class: Main\nName: {objectName}\nType: {str(type(objectCall).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall),16)}\nAssembly Report: {assembly}\n\n')
        print(f'Class: Main\nName: {objectName}\nType: {str(type(objectCall).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall),16)}\nAssembly Report: {assembly}\n\n')
    else:
        reportfile.write(f'Class: Main\nName: {objectName}\nType: {str(type(objectCall).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall),16)}\nContent: {str(objectCall)}\n\n')
        print(f'Class: Main\nName: {objectName}\nType: {str(type(objectCall).__name__).replace("type","class")}\nObject ID: {"0x{0:0{1}X}".format(id(objectCall),16)}\nContent: {str(objectCall)}\n\n')
reportfile.write(f'Imports: {", ".join(imports)}\nLinks: {", ".join(links)}\n')
print(f'Imports: {", ".join(imports)}\nURLs: {", ".join(links)}\n')
reportfile.close()
os.system('start report.txt')
sys.exit()