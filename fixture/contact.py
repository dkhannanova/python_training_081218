from selenium.webdriver.support.select import Select


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def change_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_select(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field("firstname", contact.firstname)
        self.change_field("middlename", contact.middlename)
        self.change_field("lastname", contact.lastname)
        self.change_field("nickname", contact.nickname)
        self.change_field("photo", contact.photo)
        self.change_field("title", contact.title)
        self.change_field("company", contact.company)
        self.change_field("address", contact.address)
        self.change_field("home", contact.home)
        self.change_field("mobile", contact.mobile)
        self.change_field("work", contact.work)
        self.change_field("fax", contact.fax)
        self.change_field("email", contact.email)
        self.change_field("homepage", contact.homepage)
        self.change_field("bday", contact.bday)
        self.change_field("work", contact.work)
        self.change_field("work", contact.work)
        self.change_field("work", contact.work)
        self.change_field("work", contact.work)
        self.change_field("work", contact.work)
        self.change_field("work", contact.work)
        self.change_field("work", contact.work)
        self.change_field_select("bday", contact.bday)
        self.change_field_select("bmonth", contact.bmonth)
        self.change_field("byear", contact.byear)
        self.change_field("address2", contact.address2)
        self.change_field("phone", contact.phone)
        self.change_field("notes", contact.notes)

    def create_new_contact(self, contact):
        # create contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_contact(self):
            # delete contact
            wd = self.app.wd
            wd.find_element_by_name("selected[]").click()
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            wd.switch_to_alert().accept()
            self.return_to_contacts_page()

    def modify_contact(self, contact):
            wd = self.app.wd
            wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
            self.fill_contact(contact)
            wd.find_element_by_name("update").click()
