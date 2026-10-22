from conftest import page


class technologies:
    def __init__(self, page):
        self.page=page
        self.technologies=page.locator('(//a[text()="Technologies"])[1]')

        #ecommerce
        self.ecommerce=page.locator('//strong[text()="eCommerce Development"]')
        self.tec1=page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.tec2=page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.tec3 =page.locator('//a[text()="Codeigniter Development"]')
        self.tec3=page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.tec4=page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.tec5=page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.tec6=page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.tec7=page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.tec8=page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.tec9=page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
        self.tec10=page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
        self.tec11=page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.tec12=page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.tec13=page.locator('(//a[@href="https://www.tranktechnologies.com/drupal-development"])[1]')
        self.tec14=page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.tec15=page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.tec16=page.locator('(//a[@href="https://www.tranktechnologies.com/react-js-development"])[1]')
        self.tec17=page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')
        self.ecommerce_options=[self.tec1, self.tec2,self.tec3,self.tec4, self.tec5, 
                                self.tec6, self.tec7, self.tec8, self.tec9, self.tec10 , 
                                self.tec11, self.tec12, self.tec13,self.tec14, self.tec15, 
                                self.tec16, self.tec17 ] 

        #mobileappdev
        self.mobile=page.locator('//strong[text()="Mobile App Development"]')
        self.mad1=page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.mad2=page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.mad3=page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.mad4=page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.mad5=page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.mad6=page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
        self.mad7=page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
        self.mad8=page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
        self.mobile_options=[self.mad1 , self.mad2, self.mad3, self.mad4, self.mad5, 
                              self.mad6, self.mad7, self.mad8]

    #ai_page
        self.ai=page.locator('//strong[text()="Artificial Intelligence"]')


    def ecommerce_options_clicking(self):
        for i in self.ecommerce_options:
            self.technologies.hover()
            self.ecommerce.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def mobile_options_clicking(self):
        for i in self.mobile_options:
            self.technologies.hover()
            self.mobile.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def ai_clicking(self):
            self.technologies.hover()
            self.ai.hover()
            self.page.wait_for_load_state("load")
            self.page.go_back()