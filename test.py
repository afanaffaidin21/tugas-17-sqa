import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Test_A_Login(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        assert "/inventory.html" in browser.current_url

    def test_b_login_using_invalid_username(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("unknown_user") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

        self.assertIn('not match', response_message)

    def test_c_login_using_invalid_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("no_secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

        self.assertIn('not match', response_message)

    def test_d_login_using_empty_username(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

        self.assertIn('Username is required', response_message)

    def test_e_login_using_empty_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

        self.assertIn('Password is required', response_message)

    def test_f_login_using_empty_username_password(self):
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        response_message = browser.find_element(By.XPATH,"//div[@id='login_button_container']//form//h3").text

        self.assertIn('is required', response_message)

    def tearDown(self): 
        self.browser.close()

class Test_B_Add_To_Cart(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_add_to_cart(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)

        #validasi
        browser.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a[@class='shopping_cart_link']").click() #melihat selected product di cart
        time.sleep(1)
        response_message = browser.find_element(By.XPATH,"//div[@id='shopping_cart_container']//span[@class='shopping_cart_badge']").text

        self.assertIn('1', response_message)

    def test_b_success_remove_product_from_cart(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//button[@id='add-to-cart-sauce-labs-backpack']").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"//div[@id='shopping_cart_container']/a[@class='shopping_cart_link']").click() #melihat selected product di cart
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//button[@id='remove-sauce-labs-backpack']").click() #hapus selected product
        time.sleep(1)

    def tearDown(self): 
        self.browser.close()

class Test_C_Logout(unittest.TestCase):

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_logout(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html//input[@id='user-name']").send_keys("standard_user") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='password']").send_keys("secret_sauce") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//input[@id='login-button']").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//button[@id='react-burger-menu-btn']").click() # klik hamburger menu
        time.sleep(1)
        browser.find_element(By.XPATH,"/html//a[@id='logout_sidebar_link']").click() # klik tombol logout
        time.sleep(1)

        # validasi
        assert "https://www.saucedemo.com/" in browser.current_url

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__":
    unittest.main()