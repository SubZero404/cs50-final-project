"""Insert brands and categories

Revision ID: 92a70131ee0e
Revises: f57ec2fb4e5f
Create Date: 2025-03-20 10:00:42.601916

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column
from datetime import datetime


# revision identifiers, used by Alembic.
revision = '92a70131ee0e'
down_revision = 'f57ec2fb4e5f'
branch_labels = None
depends_on = None

brand_table = table(
    'brand',
    column('id', sa.Integer),
    column('name', sa.String(64)),
    column('slug', sa.String(64)),
    column('created_at', sa.DateTime),
    column('updated_at', sa.DateTime)
)

category_table = table(
    'category',
    column('id', sa.Integer),
    column('name', sa.String(64)),
    column('slug', sa.String(64)),
    column('created_at', sa.DateTime),
    column('updated_at', sa.DateTime)
)

def upgrade():
    now = datetime.utcnow()

    # Insert 10 brands
    op.bulk_insert(
        brand_table,
        [
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
        ]
    )

    # Insert 10 categories
    op.bulk_insert(
        category_table,
        [
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
        ]
    )

def downgrade():
    op.execute("DELETE FROM brand WHERE slug IN ('apple', 'samsung', 'sony', 'lg', 'dell', 'hp', 'asus', 'lenovo', 'microsoft', 'google')")
    op.execute("DELETE FROM category WHERE slug IN ('laptops', 'smartphones', 'tablets', 'cameras', 'headphones', 'monitors', 'printers', 'smartwatches', 'accessories', 'gaming')")