import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from common.util import fetch_user_agent

# from subprocess import CREATE_NO_WINDOW


class Driver:
    def __init__(self, headless_flg: bool = True):
        self.driver = self.driver_setting(headless_flg)

    def driver_setting(self, headless_flg: bool):
        user_agent_random = fetch_user_agent()
        # ドライバーの読み込み
        options = webdriver.ChromeOptions()

        # ヘッドレスモードの設定
        if os.name == "posix" or headless_flg:  # Linux　➙　本番環境のためHeadless
            options.add_argument("--headless")

        options.add_argument("--user-agent=" + user_agent_random)
        options.add_argument("log-level=3")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("--incognito")  # シークレットモードの設定を付与
        options.add_argument("--disable-extensions")  # 全ての拡張機能無効
        options.add_argument("disable-infobars")  # AmazonLinux用
        # options.add_argument("--start-maximized") # 画面最大化
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--disable-web-security")
        options.add_argument("--disable-desktop-notifications")
        options.add_argument("--disable-application-cache")
        options.add_argument("--lang=ja")
        # 画像を読み込まないで軽くする
        # options.add_argument("--blink-settings=imagesEnabled=false")
        service = Service(ChromeDriverManager().install())
        # service.creationflags = CREATE_NO_WINDOW #exe化後ターミナルを開かないようにする(windowsのみ)

        try:
            driver = webdriver.Chrome(service=service, options=options)
            return driver
        except Exception:
            return None

    def get(self, url: str) -> None:
        self.driver.get(url)

    # .get_attribute("href")
    def el_selector(self, s: str):
        return self.driver.find_element_by_css_selector(s)

    def els_selector(self, s: str):
        return self.driver.find_elements_by_css_selector(s)

    def el_id(self, s: str):
        return self.driver.find_element_by_id(s)

    def els_id(self, s: str):
        return self.driver.find_elements_by_id(s)

    def el_class(self, s: str):
        return self.driver.find_element_by_class_name(s)

    def els_class(self, s: str):
        return self.driver.find_elements_by_class_name(s)

    def el_xpath(self, s: str):
        return self.driver.find_element_by_xpath(s)

    def els_xpath(self, s: str):
        return self.driver.find_elements_by_xpath(s)

    def script_click(self, s: str):
        return self.driver.execute_script(f"document.querySelector({s}).click()")

    # 画像は基本pngでjpgで保存しようとするエラーメッセージが出るが保存される。
    def save_screenshot(self, path: str, img_name: str):
        w = self.driver.execute_script("return document.body.scrollWidth;")
        h = self.driver.execute_script("return document.body.scrollHeight;")
        self.driver.set_window_size(w, h)
        self.driver.save_screenshot(path + "/" + img_name)

    def save_img(self, el, path: str, img_name: str):
        # img_elm=driver.find_element_by_css_selector("img")
        # save_img(img_elm, path, "~~~~.png")
        path = path + "/" + img_name
        with open(path, "wb") as f:
            f.write(el.screenshot_as_png)

    def quit(self):
        return self.driver.quit()
