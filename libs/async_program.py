import asyncio
import libs.devices
import aioconsole
import random
import datetime as dt

from dataclasses import dataclass

@dataclass
class ServoPosition:
    pitch: int
    roll: int
    yaw: int
    engaged: bool = False
    ready: bool = False


@dataclass
class FlightDevice:
    xsense: devices.XSense
    rtk: devices.RTK
    pitch_rudder: devices.Ruder
    yaw_rudder: devices.Ruder
    roll_rudder: devices.Ruder


@dataclass
class FlightData:
    time: str
    gyroData: str
    rtkData: str
    rudderData: str
    user_input: int


future = asyncio.Future


class FlightSystem:
    def __init__(self):
        self.fDevices = FlightDevice(
            devices.XSense(),
            devices.RTK(),
            devices.Ruder(),
            devices.Ruder(),
            devices.Ruder())

        self.fData = FlightData("", "", "", "", 0)
        self.sPosition = ServoPosition(0, 0, 0)
        self.blackbox = None
        self.loop = asyncio.get_event_loop()

    async def __init_blackBox(self):
        self.blackbox = open('BLACKBOX.csv', 'w')
        self.blackbox.write("Время; ЛинX; ЛинY; ЛинZ; УглX; УглY; УглZ; Крен; Тангаж; Рыск; Север; Восток; Высота; "
                            "СигналGPS; RPitch, RRoll, RYaw \n")

    async def wait_user_input(self):
        while True:
            # command = await self.loop.run_in_executor(None, input)
            # self.fData.user_input = command
            self.fData.user_input = random.randint(0, 6000)

            await asyncio.sleep(0.0001)

    async def get_rudder_data(self):
        while True:
            self.fData.rudderData = f'{self.fDevices.pitch_rudder.get_data(self.fData.user_input)};' \
                                    f'{self.fDevices.yaw_rudder.get_data(self.fData.user_input)};' \
                                    f'{self.fDevices.roll_rudder.get_data(self.fData.user_input)}'
            await asyncio.sleep(0.0001)

    async def get_gyroData(self):
        while True:
            self.fData.gyroData = self.fDevices.xsense.get_data()
            await asyncio.sleep(0.0001)

    async def get_RTKData(self):
        while True:
            self.fData.time = await self.get_time()
            self.fData.rtkData = self.fDevices.rtk.get_data()
            await asyncio.sleep(0.0001)

    async def get_time(self):
        return str(dt.datetime.now())

    async def display_data(self):
        while True:
            print(f'USERINPUT {self.fData.user_input} ;{self.fData.time};{self.fData.gyroData}{self.fData.rtkData}'
                  f'{self.fData.rudderData}')
            await asyncio.sleep(0.0001)

    def start(self):

        task_io = self.loop.create_task(self.wait_user_input())
        task1 = self.loop.create_task(self.get_gyroData())
        task2 = self.loop.create_task(self.get_RTKData())
        task3 = self.loop.create_task(self.get_rudder_data())
        task4 = self.loop.create_task(self.display_data())

        self.loop.run_until_complete(asyncio.gather(task_io, task1, task2, task3, task4))
        self.loop.run_forever()


if __name__ == '__main__':
    app = FlightSystem()
    app.start()



