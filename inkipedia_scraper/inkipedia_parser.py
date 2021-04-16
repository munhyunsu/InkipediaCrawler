from bs4 import BeautifulSoup
import datetime
import re

FILENAME = 'latest.html'


class InkipediaParser(object):
    def __init__(self, file_name=FILENAME):
        self.file_name = file_name
        with open(self.file_name, 'r') as f:
            self.soup = BeautifulSoup(f.read(), 'html.parser')

#    def get_salmonrun_schedule(self):
#        salmonrun_div = self._get_salmonrun_div()
#        salmontime1 = salmonrun_div[0]
#        print(salmontime1)
#        salmontime1 = salmontime1.find('div',
#                          style=('text-align: center; font-weight: bold;'
##                          background-color: '
##                                 'rgba(255, 255, 255, 0.65); '
##                                 'text-align: center; font-weight: bold;'))
#                                ))
#        salmontime1 = salmontime1.text
#        start_time1 = salmontime1.split('-')[0].strip()
#        end_time1 = salmontime1.split('-')[1].strip()[:-4]
#        salmontime2 = salmonrun_div[1]
#        salmontime2 = salmontime2.find('div',
#                          style=('background-color: '
#                                 'rgba(255, 255, 255, 0.65); '
#                                 'text-align: center; font-weight: bold;'))
#        salmontime2 = salmontime2.text
#        start_time2 = salmontime2.split('-')[0].strip()
#        end_time2 = salmontime2.split('-')[1].strip()[:-4]
#        schedules = [{'start_time': self._get_ktc_iso(start_time1),
#                      'end_time': self._get_ktc_iso(end_time1),
#                      'weapon1': salmonrun_div[0].find_all('a')[3].text,
#                      'weapon2': salmonrun_div[0].find_all('a')[5].text,
#                      'weapon3': salmonrun_div[0].find_all('a')[7].text,
#                      'weapon4': salmonrun_div[0].find_all('a')[9].text,
#                      'stage': salmonrun_div[0].find_all('a')[1].text},
#                     {'start_time': self._get_ktc_iso(start_time2),
#                      'end_time': self._get_ktc_iso(end_time2),
#                      'weapon1': salmonrun_div[1].find_all('a')[3].text,
#                      'weapon2': salmonrun_div[1].find_all('a')[5].text,
#                      'weapon3': salmonrun_div[1].find_all('a')[7].text,
#                      'weapon4': salmonrun_div[1].find_all('a')[9].text,
#                      'stage': salmonrun_div[1].find_all('a')[1].text}]
#        for index in range(0, len(schedules)):
#            for key in schedules[index].keys():
#                schedules[index][key] = schedules[index][key].strip()
#
#        return schedules'''

    @staticmethod
    def _get_ktc_iso(time_str):
        tz_seoul = datetime.timezone(datetime.timedelta(hours=9))
        if time_str.endswith(' UTC'):
            time_str = time_str[:-4]
        time_iso = time_str + ' ' + str(datetime.datetime.now().year)
        time_iso = datetime.datetime.strptime(time_iso, '%b %d %H:%M %Y')
        time_iso = time_iso + datetime.timedelta(hours=9)  # KTC = +9000
        time_iso = time_iso.replace(tzinfo=tz_seoul)

        return time_iso

#    def get_regular_schedule(self):
#        battle_div = self._parse_battle_div()
#        schedules = list()
#        for index in (1, 14):
#            schedule = {'time': battle_div[0 + index],
#                        'rule': battle_div[2 + index],
#                        'stage1': battle_div[3 + index],
#                        'stage2': battle_div[4 + index]}
#            schedules.append(schedule)
#        for index in range(0, len(schedules)):
#            for key in schedules[index].keys():
#                schedules[index][key] = schedules[index][key].split(',')[0].strip()
#        return schedules

#    def get_ranked_schedule(self):
#        battle_div = self._parse_battle_div()
#        schedules = list()
#        for index in (1, 14):
#            schedule = {'time': battle_div[0 + index],
#                        'rule': battle_div[6 + index],
#                        'stage1': battle_div[7 + index],
#                        'stage2': battle_div[8 + index]}
#            schedules.append(schedule)
#        for index in range(0, len(schedules)):
#            for key in schedules[index].keys():
#                schedules[index][key] = schedules[index][key].split(',')[0].strip()
#        return schedules

#    def get_league_schedule(self):
#        battle_div = self._parse_battle_div()
#        schedules = list()
#        for index in (1, 14):
#            schedule = {'time': battle_div[0 + index],
#                        'rule': battle_div[10 + index],
#                        'stage1': battle_div[11 + index],
#                        'stage2': battle_div[12 + index]}
#            schedules.append(schedule)
#        for index in range(0, len(schedules)):
#            for key in schedules[index].keys():
#                schedules[index][key] = schedules[index][key].split(',')[0].strip()
#        return schedules

    def _parse_battle_table(self):
        soup = self.soup
        tables = soup.find_all('table',
                               style=('width: 100%; border-spacing: 0px; '
                                      'overflow: hidden; table-layout: fixed; '
                                      'overflow-x: auto;'))[0]
        battle_table = re.findall(r'^[\w\d:,.\-\' ]+$', tables.text, re.MULTILINE)
        return battle_table

    def _parse_battle_div(self):
        soup = self.soup
        div = soup.find_all('div',
                               style=('box-shadow: 0px 0px 15px #ffffff inset; '
                                      'border-width: 10px 1px 10px 1px; border-style: solid; '
                                      'border-color: rgb(240, 60, 120); border-radius: 10px; '
                                      'padding: 15px; margin: 4px;'))[0]
        battle_text = re.findall(r'^[\w\d:,.\-\' ]+$', div.text, re.MULTILINE)
        return battle_text

    def _parse_salmonrun_table(self):
        soup = self.soup
        tables = soup.find_all('table',
                               style=('width: 100%; border-spacing: 0px; '
                                      'overflow: hidden; table-layout: fixed;'))[1]
        salmonrun_table = re.findall(r'^[\w\d:,.\-\' ]+$', tables.text, re.MULTILINE)
        return salmonrun_table

    def _get_salmonrun_div(self):
        soup = self.soup
        divs = soup.find_all('div',
                             style=('box-shadow: 0px 0px 15px #ffffff inset; border-width: 10px 1px 10px 1px; border-style: solid; border-color: rgb(240, 60, 120); border-radius: 10px; padding: 15px; margin: 4px; min-width: 250px;'
                                    ))
#                             style=('border: 2px solid #ffffff; '
#                                    'border-radius: 8px; min-width: 300px; '
#                                    'margin: 1px; flex-grow: 1;'))
        return divs

    def get_salmonrun_schedule(self):
        divs = self._get_bubbleboxbg_div()
        div = divs[3] # 4 is Salmon Run Schedule
        ## Start and End time
        salmonrun_time1 = div.find('div',
                                   {'id': 'salmon1'}).text
        start_time1 = salmonrun_time1.split('-')[0].strip()
        start_time1 = self._get_ktc_iso(start_time1)
        end_time1 = salmonrun_time1.split('-')[1].strip()
        end_time1 = self._get_ktc_iso(end_time1)
        if start_time1.month == 12 and end_time1.month == 1:
            end_time1 = end_time1.replace(year=end_time1.year+1)
        salmonrun_time2 = div.find('div',
                                   {'id': 'salmon2'}).text
        start_time2 = salmonrun_time2.split('-')[0].strip()
        start_time2 = self._get_ktc_iso(start_time2)
        end_time2 = salmonrun_time2.split('-')[1].strip()
        end_time2 = self._get_ktc_iso(end_time2)
        if start_time2.month == 12 and end_time2.month == 1:
            end_time2 = end_time2.replace(year=end_time2.year+1)
        boxes = div.find_all('div',
                             class_='bubbleboxbg-darker')
        ## Weapons
        weapon1 = [boxes[1].find_all('a')[1].text.strip(),
                   boxes[1].find_all('a')[3].text.strip(),
                   boxes[1].find_all('a')[5].text.strip(),
                   boxes[1].find_all('a')[7].text.strip(),
                  ]
        weapon2 = [boxes[4].find_all('a')[1].text.strip(),
                   boxes[4].find_all('a')[3].text.strip(),
                   boxes[4].find_all('a')[5].text.strip(),
                   boxes[4].find_all('a')[7].text.strip(),
                  ]
        ## States
        stage1 = boxes[0].text.strip()
        stage2 = boxes[3].text.strip()
        ## Rewards
        reward1 = boxes[2].text.strip()
        reward2 = boxes[5].text.strip()

        schedules = [{'start_time': start_time1.isoformat(),
                      'end_time': end_time1.isoformat(),
                      'weapon1': weapon1[0],
                      'weapon2': weapon1[1],
                      'weapon3': weapon1[2],
                      'weapon4': weapon1[3],
                      'stage': stage1,
                      'reward': reward1,
                     },
                     {'start_time': start_time2.isoformat(),
                      'end_time': end_time2.isoformat(),
                      'weapon1': weapon2[0],
                      'weapon2': weapon2[1],
                      'weapon3': weapon2[2],
                      'weapon4': weapon2[3],
                      'stage': stage2,
                      'reward': reward2,
                     }]

        return schedules

    def get_regular_schedule(self):
        divs = self._get_bubbleboxbg_div()
        div = divs[1] # 1 is battle schedule
        light_boxes = div.find_all('div',
                                   class_='bubbleboxbg-lighter')
        dark_boxes = div.find_all('div',
                                  class_='bubbleboxbg-darker')
        rule1 = light_boxes[3].find_all('a')[0].text.strip()
        stage11 = dark_boxes[0].find_all('a')[1].text.strip()
        stage12 = dark_boxes[0].find_all('a')[3].text.strip()
        rule2 = light_boxes[4].find_all('a')[0].text.strip()
        stage21 = dark_boxes[1].find_all('a')[1].text.strip()
        stage22 = dark_boxes[1].find_all('a')[3].text.strip()

        schedules = [{'rule': rule1,
                      'stage1': stage11,
                      'stage2': stage12,
                     },
                     {'rule': rule2,
                      'stage1': stage21,
                      'stage2': stage22,
                     }]
        return schedules

    def get_ranked_schedule(self):
        divs = self._get_bubbleboxbg_div()
        div = divs[1] # 1 is battle schedule
        light_boxes = div.find_all('div',
                                   class_='bubbleboxbg-lighter')
        dark_boxes = div.find_all('div',
                                  class_='bubbleboxbg-darker')
        rule1 = light_boxes[5].find_all('a')[1].text.strip()
        stage11 = dark_boxes[2].find_all('a')[1].text.strip()
        stage12 = dark_boxes[2].find_all('a')[3].text.strip()
        rule2 = light_boxes[6].find_all('a')[1].text.strip()
        stage21 = dark_boxes[3].find_all('a')[1].text.strip()
        stage22 = dark_boxes[3].find_all('a')[3].text.strip()

        schedules = [{'rule': rule1,
                      'stage1': stage11,
                      'stage2': stage12,
                     },
                     {'rule': rule2,
                      'stage1': stage21,
                      'stage2': stage22,
                     }]
        return schedules

    def get_league_schedule(self):
        divs = self._get_bubbleboxbg_div()
        div = divs[1] # 1 is battle schedule
        light_boxes = div.find_all('div',
                                   class_='bubbleboxbg-lighter')
        dark_boxes = div.find_all('div',
                                  class_='bubbleboxbg-darker')
        rule1 = light_boxes[7].find_all('a')[1].text.strip()
        stage11 = dark_boxes[4].find_all('a')[1].text.strip()
        stage12 = dark_boxes[4].find_all('a')[3].text.strip()
        rule2 = light_boxes[8].find_all('a')[1].text.strip()
        stage21 = dark_boxes[5].find_all('a')[1].text.strip()
        stage22 = dark_boxes[5].find_all('a')[3].text.strip()

        schedules = [{'rule': rule1,
                      'stage1': stage11,
                      'stage2': stage12,
                     },
                     {'rule': rule2,
                      'stage1': stage21,
                      'stage2': stage22,
                     }]
        return schedules

    def _get_bubbleboxbg_div(self):
        soup = self.soup
        divs = soup.find_all('div',
                             class_='bubbleboxbg')
        return divs


def main():
    parser = InkipediaParser('tests/inkipedia_parser_tests.html')
    print(parser.get_salmonrun_schedule())
    print(parser.get_regular_schedule())
    print(parser.get_ranked_schedule())
    print(parser.get_league_schedule())

if __name__ == '__main__':
    main()
