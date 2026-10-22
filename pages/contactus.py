from conftest import page


class contactus:
    def __init__(self, page):
        self.page=page
        self.contactus=page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]')



#Click on Contact us

        self.name=page.locator('(//input[@placeholder="Your Name"])[2]')
        self.mail=page.locator('(//input[@placeholder="Your Mail"])[2]')
        self.company=page.locator('(//input[@placeholder="Your Company"])[2]')
        self.service=page.locator('(//select[@name="service"])[2]')
        self.phone=page.locator('(//input[@placeholder="Your Phone"])[2]')
        self.message=page.locator('(//textarea[@placeholder="Message"])[2]')
        self.submit=page.locator('(//input[@type="submit"])[2]')
        self.contactus_options=[self.name,self.mail,self.company,self.service,self.phone,self.message,self.submit]
    def contactus_options_clicking(self):
            self.contactus.click()
            self.name.fill("karthik")
            self.mail.fill("karthik@gmail.com")
            self.company.fill("uncodemy")
            self.service.select_option("App Development")
            self.phone.fill("9876987678")
            self.message.fill("provide the info on the same")
            self.submit.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()   

  
