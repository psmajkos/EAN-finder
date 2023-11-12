from selenium import webdriver
from selenium.webdriver.common.by import By

def search_amazon(ean):
    url = f'https://www.amazon.de/s?k={ean}'

    # Use a headless browser (invisible) for scraping
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Comment this line if you want to see the browser
    driver = webdriver.Chrome(options=options)

    driver.get(url)

    try:
        # Wait for some time to let the page load
        driver.implicitly_wait(0)

        # Extract the price from the first search result
        price_element = driver.find_element(By.CSS_SELECTOR, 'span.a-price-whole')
        price_symbol = driver.find_element(By.CSS_SELECTOR, 'span.a-price-symbol')

        if price_element:
            price = price_element.text
            symbol = price_symbol.text
            print(f'The price on Amazon for EAN {ean} is: {price} {symbol}')
        else:
            print(f'Price not found for EAN {ean}')
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        driver.quit()


# Example usage
ean_code = '3052910018917'  # Replace this with the actual EAN
search_amazon(ean_code)


# "values":[{"id":null,"valueLabel":"6198438308998","url":null}]},