from selene import browser,  have


def test_first(browser_resolution):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').type('qa.guru').press_enter()
    browser.element('html').should(have.text('qa.guru — российская онлайн-школа инженеров по автоматизации тестирования'))


def test_second(browser_resolution):
    browser.open('https://duckduckgo.com/')
    browser.element('[name="q"]').type('авфывфывыфафаыфвфца23123').press_enter()
    browser.element('html').should(have.text('ничего не найдено'))