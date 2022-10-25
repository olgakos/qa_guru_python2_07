from demoqa.models.controls import datepicker
from demoqa.models.pages.automation_practice_form import *
#browser.config.hold_browser_open = True


def test_practice_form():
    open_page('https://demoqa.com', '/automation-practice-form')
    set_first_name('Olga')
    set_last_name('Kos')
    set_email('test@test.uk')
    set_gender('Female')
    set_user_number('0123456789') #10!
    datepicker.select_date_of_bday_1('20 Oct 2022')
    #datepicker.select_date_of_bday_2()
    set_subject('Arts', 'English')
    set_hobbies('Sports', 'Music')
    set_photo('../resources/siegfriedsassoon.jpg')
    set_address('Peterburg, Moskowsky 16') #simple text
    select_state('Haryana')
    select_city('Karnal')
    submit()

    data_verification('Olga Kos')
    data_verification('test@test.uk')
    data_verification('Female')
    data_verification('0123456789')
    data_verification('20 October,2022')
    data_verification('Arts, English')
    data_verification('Sports, Music')
    data_verification('siegfriedsassoon.jpg')
    data_verification('Peterburg, Moskowsky 16')
    data_verification('Haryana Karnal')