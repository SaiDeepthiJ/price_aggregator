def get_mock_prices(product_name):
    # Lowercase for simple matching
    product_name = product_name.lower()

    # Mock database of products and their prices across sites
    products = {
        "iphone": [
            {"site": "Amazon", "price": "$999", "url": "https://amazon.com/search?q=iphone"},
            {"site": "eBay", "price": "$950", "url": "https://ebay.com/sch/i.html?_nkw=iphone"},
            {"site": "Flipkart", "price": "₹75,000", "url": "https://www.flipkart.com/search?q=iphone"}
        ],
        "macbook": [
            {"site": "Amazon", "price": "$1,299", "url": "https://amazon.com/search?q=macbook"},
            {"site": "eBay", "price": "$1,250", "url": "https://ebay.com/sch/i.html?_nkw=macbook"},
            {"site": "Flipkart", "price": "₹1,00,000", "url": "https://www.flipkart.com/search?q=macbook"}
        ],
        "galaxy s21": [
            {"site": "Amazon", "price": "$799", "url": "https://amazon.com/search?q=galaxy+s21"},
            {"site": "eBay", "price": "$750", "url": "https://ebay.com/sch/i.html?_nkw=galaxy+s21"},
            {"site": "Flipkart", "price": "₹65,000", "url": "https://www.flipkart.com/search?q=galaxy+s21"}
        ],
        # Add more products as needed
    }

    # Return matching results or empty list if none found
    return products.get(product_name, [{"site": "No results", "price": "-", "url": "#"}])
