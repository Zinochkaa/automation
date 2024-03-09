import time
#
# from pages.base_page import BasePage
#
# def test(driver):
#     page = BasePage(driver, 'https://www.google.com')
#     page.open()
#     time.sleep(5)


from pages.elements_page import TextBoxPage

class TestElements:
    class TestTextBox:
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()
            print(output_name)
            print(output_email)
            print(output_cur_addr)
            print(output_per_addr)

            # time.sleep(5)
