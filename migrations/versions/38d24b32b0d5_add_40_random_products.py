"""Add 40 random products

Revision ID: 38d24b32b0d5
Revises: a98af4d49fd9
Create Date: 2025-03-23 14:24:17.408346

"""
from alembic import op
import sqlalchemy as sa
import random
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '38d24b32b0d5'
down_revision = 'a98af4d49fd9'
branch_labels = None
depends_on = None


# Reference the product table
product_table = sa.table(
    "product",
    sa.column("name", sa.String),
    sa.column("description", sa.String),
    sa.column("price", sa.Float),
    sa.column("previous_price", sa.Float),
    sa.column("category_id", sa.Integer),
    sa.column("brand_id", sa.Integer),
    sa.column("quantity", sa.Integer),
    sa.column("product_image", sa.String),
    sa.column("flash_sale", sa.Boolean),
    sa.column("created_at", sa.DateTime),
    sa.column("updated_at", sa.DateTime),
)

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

def upgrade():
    products = [generate_random_product() for _ in range(40)]
    op.bulk_insert(product_table, products)

def downgrade():
    op.execute("DELETE FROM product")