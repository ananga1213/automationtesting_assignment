from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.cartSummary import CartSummary


class IndexPage():

    def __init__(self, driver):
        self.driver = driver
    popularText = (By.XPATH, "//a[@class='homefeatured']")
    productPrice = (By.XPATH, "//ul[@class='product_list grid row homefeatured tab-pane active']//div[1]//div[2]//div[1]//span[@class='price product-price']")
    addButton = (By.XPATH, "//div[@class='button-container']//a[@title='Add to cart']")
    conf_cart = (By.XPATH, "//div[@id='layer_cart']//div//div[1]//h2[1]")
    product_name = (By.XPATH, "//span[@id='layer_cart_product_title']")
    product_color = (By.XPATH, "//span[@id='layer_cart_product_attributes']")
    product_quantity = (By.XPATH, "//span[@id='layer_cart_product_quantity']")
    product_price = (By.XPATH, "//span[@id='layer_cart_product_price']")
    window_close = (By.XPATH, "//div[@id='layer_cart']/div/div/span[1]")
    view_cart = (By.XPATH, "//div[@class='container']/div/div[3]/div/a")
    verify_cart_quantity = (By.XPATH, "//div[@class='cart-info']/div //span[@class='quantity']")
    verify_cart_name = (By.XPATH, "//div[@class='cart-info']/div //a[@class='cart_block_product_name']")
    verify_cart_color = (By.XPATH, "//div[@class='cart-info']/div[2]/a")
    verify_shipping_price = (By.XPATH, "//div[@class='cart-prices-line first-line']/span[1]")
    verify_all_total_price = (By.XPATH, "//div[@class='cart-prices-line last-line']/span[1]")
    ClickOnCart = (By.XPATH, "//div[@class='shopping_cart']/a")
    product = (By.XPATH,"//ul[@class='product_list grid row homefeatured tab-pane active'] //div[@class='product-container']")
    discountedProduct = (By.XPATH, "//ul[@class='product_list grid row homefeatured tab-pane active'] //div[@class='product-container']/div[2]/div[1]")
    def getpopularText(self):
        return self.driver.find_element(*IndexPage.popularText)
    def getPrice(self):
        return self.driver.find_elements(*IndexPage.productPrice)
    def getAddButton(self):
        return self.driver.find_elements(*IndexPage.addButton)
    def getconfCart(self):
        return self.driver.find_element(*IndexPage.conf_cart).text
    def getproductName(self):
        return self.driver.find_element(*IndexPage.product_name).text
    def getproductColor(self):
        return self.driver.find_element(*IndexPage.product_color).text
    def getproductQuantity(self):
        return self.driver.find_element(*IndexPage.product_quantity).text
    def getproductPrice(self):
        return self.driver.find_element(*IndexPage.product_price).text
    def getWindowClosed(self):
        return self.driver.find_element(*IndexPage.window_close)
    def getViewCart(self):
        cart = self.driver.find_element(*IndexPage.view_cart)
        action = ActionChains(self.driver)
        return action.move_to_element(cart).perform()
    def getverifyCartQuantity(self):
        return self.driver.find_element(*IndexPage.verify_cart_quantity).text
    def getVerifyProductName(self):
        return self.driver.find_element(*IndexPage.verify_cart_name).text
    def getverifyCartColor(self):
        return self.driver.find_element(*IndexPage.verify_cart_color).text
    def getVerifyShippingPrice(self):
        return self.driver.find_element(*IndexPage.verify_shipping_price).text
    def getVerifyAllTotalPrice(self):
        return self.driver.find_element(*IndexPage.verify_all_total_price).text
    def getClickOnCart(self):
        self.driver.find_element(*IndexPage.ClickOnCart).click()
        cartsummary = CartSummary(self.driver)
        return cartsummary

    def getProduct(self):
        return self.driver.find_elements(*IndexPage.product)

    def getDiscountedProduct(self):
        return self.driver.find_elements(*IndexPage.discountedProduct)




