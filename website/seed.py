import random
from datetime import datetime
from website import create_app, db
from website.models import Brand, Category, Product  # Import the necessary models

app = create_app()

# Seed function
def generate_random_product():
    categories = list(range(1, 13))  # Assuming 12 categories
    brands = list(range(1, 13))  # Assuming 12 brands
    names = ["Laptop", "Smartphone", "Tablet", "Camera", "Headphones", "Monitor", "Printer", "Smartwatch", "Gaming Console", "Sneakers"]
    images = ["product1.jpg", "product2.jpg", "product3.jpg", "product4.jpg"]
    now = datetime.utcnow()
    
    return {
        "name": random.choice(names) + " " + str(random.randint(100, 999)),
        "description": "A high-quality " + random.choice(names),
        "price": round(random.uniform(50, 2000), 2),
        "previous_price": round(random.uniform(50, 2000), 2),
        "category_id": random.choice(categories),
        "brand_id": random.choice(brands),
        "quantity": random.randint(1, 50),
        "product_image": random.choice(images),
        "flash_sale": random.choice([True, False]),
        "created_at": now,
        "updated_at": now,
    }

# Insert brands and categories
with app.app_context():
    now = datetime.utcnow()

    # Insert 12 brands
    db.session.bulk_insert_mappings(Brand, [
        {"name": "Unknow", "slug": "unknow", "created_at": now, "updated_at": now},
        {"name": "Apple", "slug": "apple", "created_at": now, "updated_at": now},
        {"name": "Samsung", "slug": "samsung", "created_at": now, "updated_at": now},
        {"name": "Sony", "slug": "sony", "created_at": now, "updated_at": now},
        {"name": "LG", "slug": "lg", "created_at": now, "updated_at": now},
        {"name": "Dell", "slug": "dell", "created_at": now, "updated_at": now},
        {"name": "HP", "slug": "hp", "created_at": now, "updated_at": now},
        {"name": "Asus", "slug": "asus", "created_at": now, "updated_at": now},
        {"name": "Lenovo", "slug": "lenovo", "created_at": now, "updated_at": now},
        {"name": "Microsoft", "slug": "microsoft", "created_at": now, "updated_at": now},
        {"name": "Google", "slug": "google", "created_at": now, "updated_at": now},
        {"name": "Nike", "slug": "nike", "created_at": now, "updated_at": now},
    ])
    db.session.commit()

    # Insert 12 categories
    db.session.bulk_insert_mappings(Category, [
        {"name": "No Category", "slug": "no-category", "created_at": now, "updated_at": now},
        {"name": "Laptops", "slug": "laptops", "created_at": now, "updated_at": now},
        {"name": "Smartphones", "slug": "smartphones", "created_at": now, "updated_at": now},
        {"name": "Tablets", "slug": "tablets", "created_at": now, "updated_at": now},
        {"name": "Cameras", "slug": "cameras", "created_at": now, "updated_at": now},
        {"name": "Headphones", "slug": "headphones", "created_at": now, "updated_at": now},
        {"name": "Monitors", "slug": "monitors", "created_at": now, "updated_at": now},
        {"name": "Printers", "slug": "printers", "created_at": now, "updated_at": now},
        {"name": "Smartwatches", "slug": "smartwatches", "created_at": now, "updated_at": now},
        {"name": "Accessories", "slug": "accessories", "created_at": now, "updated_at": now},
        {"name": "Gaming", "slug": "gaming", "created_at": now, "updated_at": now},
        {"name": "Snecker", "slug": "snecker", "created_at": now, "updated_at": now},
    ])
    db.session.commit()

    # Insert random products
    for _ in range(50):  # You can choose the number of products to generate
        product_data = generate_random_product()
        product = Product(**product_data)
        db.session.add(product)
    db.session.commit()

    print("Seeding complete!")
