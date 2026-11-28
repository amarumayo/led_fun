import glob

class TempSensor:
    def __init__(self):
        
        base_dir = '/sys/bus/w1/devices/'
        device_folders = glob.glob(base_dir + '28*')

        if not device_folders:
            print("Error. Temperature sensor not found. Check wiring.")
            exit(1)

        self.device_file = device_folders[0] + '/w1_slave'

    def read_temp(self, unit='c') -> float:
        with open(self.device_file, 'r') as f:
            temp_dat = f.read()
            is_valid = "YES" in temp_dat
            
            if not is_valid:
                return None

            # celsius
            temp = float(temp_dat.split('t=')[1]) / 1000

            if unit == 'f':
                temp = (temp * 9/5) + 32

            return temp   



