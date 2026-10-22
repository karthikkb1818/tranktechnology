from conftest import page


class blog:
    def __init__(self, page):
        self.page=page
        self.blog=page.locator('(//a[text()="Blog"])[1]')


        self.adv=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[1]')
        self.ai2=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"])[1]')
        self.cm=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"])[1]')
        self.crm=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"])[1]')
        self.dm=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"])[1]')
        self.ed=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[1]')
        self.em=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"])[1]')
        self.gd=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[1]')
        self.sit=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"])[1]')
        self.sd=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"])[1]')
        self.uiux=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[1]')
        self.web=page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[1]')
        self.blog_options=[self.adv, self.ai2, self.cm, self.crm, self.dm, self.ed , self.em, self.gd, 
                           self.sit, self.sd, self.uiux, self.web]

    def blog_options_clicking(self):   
        for i in self.blog_options:
            self.blog.click()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back() 
        self.page.go_back() 