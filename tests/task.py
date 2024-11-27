import os
from selene import browser, be, by

def test_forma_auto():
    browser.element("#firstName").should(be.blank).type('Sema').press_enter()
    browser.element("#lastName").should(be.blank).type('Semenov').press_enter()
    browser.element("#userEmail").should(be.blank).type('sema@test.com').press_enter()

    browser.element(by.text("Male")).click()
    browser.element("#userNumber").should(be.blank).type("0123456789").press_tab()
    browser.element("#dateOfBirthInput").type('01-02-2002').press_enter()

    browser.element("#subjectsInput").type("English").press_enter()
    browser.element(by.text("Sports")).click()
    browser.element(by.text("Reading")).click()
    browser.element(by.text("Music")).click()

    browser.element('[id="uploadPicture"]').set_value(os.path.abspath("../tests/Proverka.jpg"))
    browser.element("#currentAddress").type("Perm")
    browser.element("#state").click().element(by.text("NCR")).click()
    browser.element("#city").click().element(by.text("Delhi")).click()
    browser.element("#submit").click()

    def test_forma_manual():
        browser.element("#firstName").should(be.blank).type('Sema').press_enter()
        browser.element("#lastName").should(be.blank).type('Semenov').press_enter()
        browser.element("#userEmail").should(be.blank).type('sema@test.com').press_enter()

        browser.element(by.text("Male")).click()
        browser.element("#userNumber").should(be.blank).type("0123456789").press_tab()
        #browser.element("#dateOfBirthInput").type('01-02-2002').press_enter()

        browser.element("#subjectsInput").type("English").press_enter()
        browser.element(by.text("Sports")).click()
        browser.element(by.text("Reading")).click()
        browser.element(by.text("Music")).click()

        browser.element('[id="uploadPicture"]').set_value(os.path.abspath("../tests/Proverka.jpg"))
        browser.element("#currentAddress").type("Perm")
        browser.element("#state").click().element(by.text("NCR")).click()
        browser.element("#city").click().element(by.text("Delhi")).click()
        browser.element("#submit").click()