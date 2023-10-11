from driver import Driver
from pages.login_page import LoginPage


def before_all(context):
    context.driver = Driver()
    context.login_page = LoginPage()
    # in "context" vom salva toate paginile modulelor testate (ex. register_page)

def after_all(context):
    context.driver.close()