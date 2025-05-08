TRUNCATE TABLE brand, product, product_color, product_size, sku

create table if not exists brand (
    brand_id serial primary key,
    brand_name text not null
);


create table if not exists product (
    product_id serial primary key,
    product_name text not null,
    brand_id int not null references brand(brand_id)
);


create table if not exists product_color (
    product_color_id serial primary key,
    product_color_name text not null
);


create table if not exists product_size (
    product_size_id serial primary key,
    product_size_name text not null
);


create table if not exists sku (
    sku_id serial primary key,
    product_id int not null references product(product_id),
    product_size_id int not null references product_size(product_size_id),
    product_color_id int not null references product_color(product_color_id)
);

comment on table sku is 'конкретный предмет, выставленный на продажу (stock keeping unit)';


INSERT INTO product_color VALUES (1, 'Blue'), (2, 'Black');
INSERT INTO product_size VALUES (1, 'Small'), (2, 'Medium'), (3, 'Large');

INSERT INTO brand (brand_name)
SELECT 
    substr(md5(random()::text), 1, 8)
FROM generate_series(1, 10000) AS gs;
