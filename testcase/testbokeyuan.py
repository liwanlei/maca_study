from macaca import WebDriver
import time,ddt,unittest
from data.config import die_arp,server_url,login_data
from busines.login import login
@ddt.ddt
class BokeyuanTest(unittest.TestCase):
    def setUp(self):
        self.deriver=WebDriver(die_arp,server_url)
        self.deriver.init()
        self.deriver.get('https://passport.cnblogs.com/user/signin')
    def tearDown(self):
        self.deriver.quit()
    @ddt.data(*login_data)
    def test_login(self,login_data):
    	login(self.deriver,login_data['username'],login_data['username'])
    	time.sleep(1)
    	self.assertTrue(self.deriver.element_by_id(login_data['id']).text,login_data['assert'])
