from behave import *


@given("I am on the Saucedemo login page")
def step_impl(context):
    context.login_page.navigate_to_login_page()

@when("I insert a correct username and password")
def step_impl(context):
    context.login_page.set_correct_username_and_password()

@when("I click the login button")
def set_impl(context):
    context.login_page.click_login_button()

@then("I am logged in and I see the list of products")
def set_impl(context):
    context.login_page.verify_url()







