from playwright.sync_api import sync_playwright
import time

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto('https://www.saucedemo.com/')

page.type(selector='[id="user-name"]', text='standard_user', delay=100)
page.fill(selector='#password', value='secret_sauce')
page.click('#login-button')
page.wait_for_url('https://www.saucedemo.com/inventory.html', timeout=10000)
page.wait_for_selector('#inventory_container')

button_add_cart = '#add-to-cart-sauce-labs-backpack'
alt_locator_for_button =

page.is_visible(button_add_cart)
page.is_enabled(button_add_cart)
page.click(button_add_cart)



time.sleep(5)

browser.close()
playwright.stop()



