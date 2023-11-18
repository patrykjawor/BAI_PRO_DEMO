DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS users;

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    thumbnail TEXT NOT NULL,
    price DECIMAL(10, 5)
);

-- List of products downloaded from https://dummyjson.com/docs/products --
INSERT INTO products (name, price, thumbnail) VALUES 
('iPhone 9', 549, 'https://i.dummyjson.com/data/products/1/thumbnail.jpg'),
('iPhone X', 899, 'https://i.dummyjson.com/data/products/2/thumbnail.jpg'),
('Samsung Universe 9', 1249, 'https://i.dummyjson.com/data/products/3/thumbnail.jpg'),
('OPPOF19', 280, 'https://i.dummyjson.com/data/products/4/thumbnail.jpg'),
('Huawei P30', 499, 'https://i.dummyjson.com/data/products/5/thumbnail.jpg'),
('MacBook Pro', 1749, 'https://i.dummyjson.com/data/products/6/thumbnail.png'),
('Samsung Galaxy Book', 1499, 'https://i.dummyjson.com/data/products/7/thumbnail.jpg'),
('Microsoft Surface Laptop 4', 1499, 'https://i.dummyjson.com/data/products/8/thumbnail.jpg'),
('Infinix INBOOK', 1099, 'https://i.dummyjson.com/data/products/9/thumbnail.jpg'),
('HP Pavilion 15-DK1056WM', 1099, 'https://i.dummyjson.com/data/products/10/thumbnail.jpeg'),
('perfume Oil', 13, 'https://i.dummyjson.com/data/products/11/thumbnail.jpg'),
('Brown Perfume', 40, 'https://i.dummyjson.com/data/products/12/thumbnail.jpg'),
('Fog Scent Xpressio Perfume', 13, 'https://i.dummyjson.com/data/products/13/thumbnail.webp'),
('Non-Alcoholic Concentrated Perfume Oil', 120, 'https://i.dummyjson.com/data/products/14/thumbnail.jpg'),
('Eau De Perfume Spray', 30, 'https://i.dummyjson.com/data/products/15/thumbnail.jpg'),
('Hyaluronic Acid Serum', 19, 'https://i.dummyjson.com/data/products/16/thumbnail.jpg'),
('Tree Oil 30ml', 12, 'https://i.dummyjson.com/data/products/17/thumbnail.jpg'),
('Oil Free Moisturizer 100ml', 40, 'https://i.dummyjson.com/data/products/18/thumbnail.jpg'),
('Skin Beauty Serum.', 46, 'https://i.dummyjson.com/data/products/19/thumbnail.jpg'),
('Freckle Treatment Cream- 15gm', 70, 'https://i.dummyjson.com/data/products/20/thumbnail.jpg'),
('- Daal Masoor 500 grams', 20, 'https://i.dummyjson.com/data/products/21/thumbnail.png'),
('Elbow Macaroni - 400 gm', 14, 'https://i.dummyjson.com/data/products/22/thumbnail.jpg'),
('Orange Essence Food Flavou', 14, 'https://i.dummyjson.com/data/products/23/thumbnail.jpg'),
('cereals muesli fruit nuts', 46, 'https://i.dummyjson.com/data/products/24/thumbnail.jpg'),
('Gulab Powder 50 Gram', 70, 'https://i.dummyjson.com/data/products/25/thumbnail.jpg'),
('Plant Hanger For Home', 41, 'https://i.dummyjson.com/data/products/26/thumbnail.jpg'),
('Flying Wooden Bird', 51, 'https://i.dummyjson.com/data/products/27/thumbnail.webp'),
('3D Embellishment Art Lamp', 20, 'https://i.dummyjson.com/data/products/28/thumbnail.jpg'),
('Handcraft Chinese style', 60, 'https://i.dummyjson.com/data/products/29/thumbnail.webp'),
('Key Holder', 30, 'https://i.dummyjson.com/data/products/30/thumbnail.jpg');

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
);

-- List of users downloaded from https://dummyjson.com/docs/users --
INSERT INTO users (username, email, password) VALUES
('atuny0', 'atuny0@sohu.com', '9uQFF1Lh'),
('hbingley1', 'hbingley1@plala.or.jp', 'CQutx25i8r'),
('rshawe2', 'rshawe2@51.la', 'OWsTbMUgFc'),
('yraigatt3', 'yraigatt3@nature.com', 'sRQxjPfdS'),
('kmeus4', 'kmeus4@upenn.edu', 'aUTdmmmbH'),
('jtreleven5', 'jtreleven5@nhs.uk', 'zY1nE46Zm'),
('dpettegre6', 'dpettegre6@columbia.edu', 'YVmhktgYVS'),
('ggude7', 'ggude7@chron.com', 'MWwlaeWcOoF6'),
('nloiterton8', 'nloiterton8@aol.com', 'HTQxxXV9Bq4'),
('umcgourty9', 'umcgourty9@jalbum.net', 'i0xzpX'),
('acharlota', 'acharlota@liveinternet.ru', 'M9lbMdydMN'),
('rhallawellb', 'rhallawellb@dropbox.com', 'esTkitT1r'),
('lgribbinc', 'lgribbinc@posterous.com', 'ftGj8LZTtv9g'),
('mturleyd', 'mturleyd@tumblr.com', 'GyLnCB8gNIp'),
('kminchelle', 'kminchelle@qq.com', '0lelplR'),
('dpierrof', 'dpierrof@vimeo.com', 'Vru55Y4tufI4'),
('vcholdcroftg', 'vcholdcroftg@ucoz.com', 'mSPzYZfR'),
('sberminghamh', 'sberminghamh@chron.com', 'cAjfb8vg'),
('bleveragei', 'bleveragei@so-net.ne.jp', 'UZGAiqPqWQHQ'),
('aeatockj', 'aeatockj@psu.edu', 'szWAG6hc'),
('ckensleyk', 'ckensleyk@pen.io', 'tq7kPXyf'),
('froachel', 'froachel@howstuffworks.com', 'rfVSKImC'),
('beykelhofm', 'beykelhofm@wikispaces.com', 'zQwaHTHbuZyr'),
('brickeardn', 'brickeardn@fema.gov', 'bMQnPttV'),
('dfundello', 'dfundello@amazon.co.jp', 'k9zgV68UKw8m'),
('lgronaverp', 'lgronaverp@cornell.edu', '4a1dAKDv9KB9'),
('fokillq', 'fokillq@amazon.co.jp', 'xZnWSWnqH'),
('xisherwoodr', 'xisherwoodr@ask.com', 'HLDqN5vCF'),
('jissetts', 'jissetts@hostgator.com', 'ePawWgrnZR8L'),
('kdulyt', 'kdulyt@umich.edu', '5t6q4KC7O');