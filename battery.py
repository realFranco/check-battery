import platform


def  performBatteryCheck():
    operativeSystem: str = platform.system()
    if platform.system() == '':
        print('Platform name it is not allowed.')
        return

    if operativeSystem == 'Darwin':
        from checkBattery.mac import Mac
        
        Mac().exposeNotification()

    if operativeSystem == 'ubuntu':
        print('The check battery service it\'s not implemented for Ubuntu yet.')

    if operativeSystem == 'windows':
            print('The check battery service it\'s not implemented for Windows yet.')

    return

if __name__ == '__main__':
    performBatteryCheck()
