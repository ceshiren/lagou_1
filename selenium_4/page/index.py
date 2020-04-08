from time import sleep

from selenium.webdriver.common.by import By

from selenium_4.page.add_member import AddMember
from selenium_4.page.base_page import BasePage


class Index(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def goto_add_member(self):
        self.find(By.ID, "menu_contacts").click()
        def wait(driver):
            ele_len = len(self.finds(By.ID, "username"))
            if ele_len < 1:
                self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1) .js_add_member").click()
            # 如果username存在，就返回true
            return ele_len >= 1
        self.wait_for(wait)
        # 对AddMember进行了实例化
        return AddMember(reuse=True)

    def goto_import_address(self):
        pass

    def goto_member_join(self):
        pass
