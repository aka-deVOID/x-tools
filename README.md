[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# X Tools (no more Twitter)

## What can I do?

- Delete Tweets
- Delete Replies
- Remove Likes
- Remove Followings
- Delete Media Tweet

#### Installation

```sh
git clone https://github.com/aka-deVOID/x-tools.git
cd x-tools
pip install -r requirements.txt
python src/main.py
```

#### TODO

- [ ] Option Builder [Link](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.options)
  and [Link](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.options)
- [x] (Removed) Firefox Profile
  Builder [Link](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.firefox_profile)
- [ ] Extnsion Handler ( for using as VPN, Proxy and stuff )
- [ ] Driver Builder [Link](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.webdriver)
  and [Link](https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.webdriver)
- [x] CLI menu style
- [ ] Add Database for save the deleted datas (pictures, texts, (maybe comments))
- [ ] Login detector ( for now we don't support auto login ) after the user logged in process will be started.
- [ ] Auto extension downloader
- [ ] Fix prints color (using rich and colorama)