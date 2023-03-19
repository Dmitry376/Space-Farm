import json
import time
import datetime
from main import data_update, session, stop_session

stop_session()


def main():
    while True:
        with open("properties.json", "r") as read_file:
            data = json.load(read_file)
        Time = data['time']
        data_update()
        dt = datetime.datetime.now()
        nowtime = dt.strftime("%H:%M:%S")
        print('>> [' + str(nowtime) + ']' + ' Данные успешно получены!\n>> Следующие будут отправлены через ~' + str(Time) + ' секунд')
        time.sleep(Time)

main()
