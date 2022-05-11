DROP TABLE IF EXISTS products;
CREATE TABLE products (
  brand text,
  brand_key text,
  ic_name text,
  ic_description text,
  rating real,
  rating_count int,
  ingredients text
);

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
  brand_key text,
  review_date text,
  rating int,
  title text,
  comment text
);