
from datetime import datetime, timezone
from time import sleep

from temp_sensor import TempSensor
from temperature_repository import TemperatureRepository, TemperatureModel

if __name__ == '__main__':

    repo = TemperatureRepository()
    sensor = TempSensor()

    while True: 
        sleep(5)
        temp_c = sensor.read_temp()

        if temp_c is not None:
            timestamp = datetime.now(timezone.utc)
            repo.post(TemperatureModel(timestamp=timestamp, temp_c=temp_c))
        else:
            print("Invalid reading skipping")
