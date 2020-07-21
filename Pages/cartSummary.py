from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CartSummary():

    def __init__(self, driver):
        self.driver = driver

    tab = (By.XPATH, "//ul[@id='order_step']/li[1]/span[1]")
    product_name = (By.XPATH, "//tr[@id='product_7_34_0_0']/td[2]/p")
    product_color = (By.XPATH, "//tr[@id='product_7_34_0_0']/td[2]/small/a")
    product_price = (By.XPATH, "//tr[@id='product_7_34_0_0']/td[4]/span //span[@class='price special-price']")
    product_quantity = (By.XPATH, "//tr[@id='product_7_34_0_0']/td[5]/input[2]")
    withoutshipping_total_price = (By.XPATH, "//tr[@id='product_7_34_0_0']/td[6]/span")
    product_shipping_price = (By.XPATH, "//td[@id='total_shipping']")
    withshipping_total_price = (By.XPATH, "//td[@id='total_price_without_tax']")
    all_total_price = (By.XPATH, "//span[@id='total_price']")
    oldPrice = (By.XPATH, "//span[@class='old-price']")
    discountPercent = (By.XPATH, "//span[@class='price-percent-reduction small']")
    discountedPrice = (By.XPATH, "//td[@class='cart_total']/span")


    def getTab(self):
        return self.driver.find_element(*CartSummary.tab).text

    def getProductName(self):
        return self.driver.find_element(*CartSummary.product_name).text

    def getProductColor(self):
        return self.driver.find_element(*CartSummary.product_color).text

    def getProductPrice(self):
        return self.driver.find_element(*CartSummary.product_price).text

    def getWithoutShippingTotalPrice(self):
        return self.driver.find_element(*CartSummary.withoutshipping_total_price).text

    def getProductShippingPrice(self):
        return self.driver.find_element(*CartSummary.product_shipping_price).text

    def getWithShippingTotalPrice(self):
        return self.driver.find_element(*CartSummary.withshipping_total_price).text

    def getAllTotalPrice(self):
        return self.driver.find_element(*CartSummary.all_total_price).text

    def getOldPrice(self):
        return self.driver.find_elements(*CartSummary.oldPrice)
    def getDiscountPercentage(self):
        return self.driver.find_elements(*CartSummary.discountPercent)
    def getDiscountedPrice(self):
        return self.driver.find_elements(*CartSummary.discountedPrice)

