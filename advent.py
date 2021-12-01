import os
import pathlib
import requests
import sqlite3
import http.cookiejar
import browser_cookie3

COOKIELOCFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.cookie_location')

class Advent(object):

    def __init__(self):

        self.session = requests.Session()
        if not os.path.exists(COOKIELOCFILE):
            cookie_loc = input('Which browser are you using? (chrome/firefox): ')
            with open(COOKIELOCFILE, 'w') as f:
                f.write(cookie_loc.rstrip().lower())
        else:
            with open(COOKIELOCFILE, 'r') as f:
                cookie_loc = f.read().rstrip()

        if cookie_loc == 'firefox' or (len(cookie_loc) > 6 and cookie_loc[-6:] == 'sqlite'):
            cj = browser_cookie3.firefox()
        else:
            cj = browser_cookie3.chrome()
        self.session.cookies = cj

        """
        if len(cookie_loc) > 6 and cookie_loc[-6:] == 'sqlite':
            cj = http.cookiejar.CookieJar()

            con = sqlite3.connect(cookie_loc)
            cur = con.cursor()
            cur.execute("SELECT host, path, isSecure, expiry, name, value FROM moz_cookies")
            for item in cur.fetchall():
                c = http.cookiejar.Cookie(0, item[4], item[5],
                    None, False,
                    item[0], item[0].startswith('.'), item[0].startswith('.'),
                    item[1], False,
                    item[2],
                    item[3], item[3]=="",
                    None, None, {})
                cj.set_cookie(c)
            self.session.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                "Accept-Language": "en-US,en"
            }
            self.session.cookies = cj
        else:
            print('no support for chrome right now')
        """

    def get_input(self, dayno):
        inputurl = f'https://adventofcode.com/2021/day/{dayno}/input'
        r = self.session.get(inputurl)

        return r.text

    def submit_answer(self, dayno, starno, answer):
        answerurl = f'https://adventofcode.com/2021/day/{dayno}/answer'
        payload = {'answer': answer, 'level': starno}
        print(f'Submitting answer {answer} for day {dayno}, star {starno}')
        r = self.session.post(answerurl, data=payload)

        if 'the right answer!' in r.text:
            print('YOUR ANSWER IS CORRECT!!!!')
        elif 'Did you already complete it?' in r.text:
            print('You have already submitted an answer to this problem!')
        else:
            print('Your answer is incorrect :<')
            print(r.text)

if __name__ == '__main__':
    pass
