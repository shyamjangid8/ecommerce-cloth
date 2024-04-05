import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "kurtis.settings")

# Initialize Django
django.setup()

# Import Django models after Django is initialized
from store.models import Product, AvailableSize
from category.models import category  # Adjust the import based on your actual model name

def create_product_with_sizes(product_name, slug, description, price, size_data, stock, is_available, category):
    # Get or create the category instance
    category = category.objects.get_or_create(category_name=category)

    # Create the product
    product = Product.objects.create(
        product_name=product_name,
        slug=slug,
        description=description,
        price=price,
        stock=stock,
        is_available=is_available,
        category=category
    )

    # Associate sizes with the product
    for size_name, size_price in size_data:
        size = AvailableSize.objects.get_or_create(size=size_name, price=size_price)[0]
        product.availabel_size.add(size)

    return product

# Example usage
product_name = 'T-shirt'
slug = 't-shirt'
description = 'A basic T-shirt'
price = 19.99
size_data = [('S', 19.99), ('M', 21.99), ('L', 24.99)]  # List of size names and prices
stock = 100
is_available = True
category = 'shrit'

# Call the function to create the product with multiple sizes
create_product_with_sizes(product_name, slug, description, price, size_data, stock, is_available, category)
