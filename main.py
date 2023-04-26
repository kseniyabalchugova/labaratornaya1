import parsfacul
import re
if __name__=='__main__':
    parsfacul.parser()
    with open('file1.txt') as f:
        lines = f.readlines()
    str = ' С составом и структурой факультетов Вы можете ознакомиться, используя левое меню. '
    pattern = re.compile(re.escape(str))
    with open('file1.txt', 'w') as f:
        for line in lines:
            result = pattern.search(line)
            if result is None:
                f.write(line)
#бальчугова ксения ивт221