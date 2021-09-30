from speak_and_listen import speak, hear_me
from requests_html import HTMLSession
import random

def hear_price_and_get_number():
    while True:
        try:
            price = hear_me()
            #price.replace("pesos", "").replace(",", ".").replace("con", ".")
            final_price = price
            return final_price
        except ValueError:
            speak("No te entendí, a ver de nuevo")


def get_random_attrs():
    session = HTMLSession()

    main_site = session.get("https://www.venex.com.ar/")

    categories = main_site.html.find(".menu-item-list .mc-item .item")

    category = random.choice(categories)
    while category.text == "Venex Gaming Fest":
        category = random.choice(categories)

    product_page = session.get(category.attrs["href"])
    products = product_page.html.find(".product-box")

    product = random.choice(products)
    image_src = product.find(".thumb img", first=True).attrs["src"]
    product_name = product.find(".product-box-title", first=True).text
    product_price = product.find(".current-price", first=True).text

    final_price = float(product_price.replace("$", "").replace(",", "."))

    return image_src, product_name, final_price


def main():
    welcome_message = "Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos"
    print(welcome_message)
    speak(welcome_message)

    image_src, product_name, final_price = get_random_attrs()

    print(product_name)
    speak("El nombre del producto es {}, cuánto crees que vale?".format(product_name))
    user_guess = hear_price_and_get_number()
    speak("El precio era {}".format(final_price))
    print(final_price)


if __name__ == "__main__":
    main()