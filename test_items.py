import time 

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_exist(browser):
    browser.get(link)
    time.sleep(4)
    assert browser.find_element_by_css_selector("button.btn-add-to-basket"), 'Button to add to cart not found'