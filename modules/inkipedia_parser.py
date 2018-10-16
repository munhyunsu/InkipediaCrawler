from bs4 import BeautifulSoup
import datetime
import re

FILENAME = 'latest.html'


class InkipediaParser(object):
    def __init__(self, file_name=FILENAME):
        self.file_name = file_name
        with open(self.file_name, 'r') as f:
            self.soup = BeautifulSoup(f.read(), 'html.parser')

    def get_salmonrun_schedule(self):
        salmonrun_table = self._parse_salmonrun_table()
        start_time1 = salmonrun_table[1].split('-')[0].strip()
        end_time1 = salmonrun_table[1].split('-')[1].strip()[:-4]
        start_time2 = salmonrun_table[2].split('-')[0].strip()
        end_time2 = salmonrun_table[2].split('-')[1].strip()[:-4]
        schedules = [{'start_time': self._get_ktc_iso(start_time1),
                      'end_time': self._get_ktc_iso(end_time1),
                      'weapon1': salmonrun_table[3],
                      'weapon2': salmonrun_table[4],
                      'weapon3': salmonrun_table[5],
                      'weapon4': salmonrun_table[6],
                      'stage': salmonrun_table[11]},
                     {'start_time': self._get_ktc_iso(start_time2),
                      'end_time': self._get_ktc_iso(end_time2),
                      'weapon1': salmonrun_table[7],
                      'weapon2': salmonrun_table[8],
                      'weapon3': salmonrun_table[9],
                      'weapon4': salmonrun_table[10],
                      'stage': salmonrun_table[12]}]
        for index in range(0, len(schedules)):
            for key in schedules[index].keys():
                schedules[index][key] = schedules[index][key].strip()

        return schedules

    @staticmethod
    def _get_ktc_iso(time_str):
        tz_seoul = datetime.timezone(datetime.timedelta(hours=9))
        time_iso = time_str.split('-')[0].strip() + ' ' + str(datetime.datetime.now().year)
        time_iso = datetime.datetime.strptime(time_iso, '%b %d %H:%M %Y')
        time_iso = time_iso + datetime.timedelta(hours=9)  # KTC = +9000
        time_iso = time_iso.replace(tzinfo=tz_seoul)

        return time_iso.isoformat()

    def get_regular_schedule(self):
        battle_table = self._parse_battle_table()
        schedules = list()
        for index in (1, 14):
            schedule = {'time': battle_table[0 + index].strip(),
                        'rule': battle_table[4 + index].strip(),
                        'stage1': battle_table[7 + index].strip(),
                        'stage2': battle_table[8 + index].strip()}
            schedules.append(schedule)
        for index in range(0, len(schedules)):
            for key in schedules[index].keys():
                schedules[index][key] = schedules[index][key].split(',')[0].strip()
        return schedules

    def get_ranked_schedule(self):
        battle_table = self._parse_battle_table()
        schedules = list()
        for index in (1, 14):
            schedule = {'time': battle_table[0 + index],
                        'rule': battle_table[5 + index],
                        'stage1': battle_table[9 + index],
                        'stage2': battle_table[10 + index]}
            schedules.append(schedule)
        for index in range(0, len(schedules)):
            for key in schedules[index].keys():
                schedules[index][key] = schedules[index][key].split(',')[0].strip()
        return schedules

    def get_league_schedule(self):
        battle_table = self._parse_battle_table()
        schedules = list()
        for index in (1, 14):
            schedule = {'time': battle_table[0 + index],
                        'rule': battle_table[6 + index],
                        'stage1': battle_table[11 + index],
                        'stage2': battle_table[12 + index]}
            schedules.append(schedule)
        for index in range(0, len(schedules)):
            for key in schedules[index].keys():
                schedules[index][key] = schedules[index][key].split(',')[0].strip()
        return schedules

    def _parse_battle_table(self):
        soup = self.soup
        tables = soup.find_all('table',
                               style=('width: 100%; border-spacing: 0px; '
                                      'overflow: hidden; table-layout: fixed;'))[0]
        battle_table = re.findall(r'^[\w\d:\-,\' ]+$', tables.text, re.MULTILINE)
        return battle_table

    def _parse_salmonrun_table(self):
        soup = self.soup
        tables = soup.find_all('table',
                               style=('width: 100%; border-spacing: 0px; '
                                      'overflow: hidden; table-layout: fixed;'))[1]
        salmonrun_table = re.findall(r'^[\w\d:\-,\' ]+$', tables.text, re.MULTILINE)
        return salmonrun_table


def main():
    parser = InkipediaParser('tests/inkipedia_parser_tests.html')
    # print(parser.get_regular_schedule())
    print(parser._parse_salmonrun_table())


if __name__ == '__main__':
    main()
