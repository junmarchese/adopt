DROP DATABASE IF EXISTS adopt;

CREATE DATABASE adopt;

\c adopt

CREATE TABLE pets
(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INT,
    notes TEXT,
    available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
    (name, species, photo_url, age, notes, available)
VALUES
    ('Woofsie', 'dog', 'https://cdn.pixabay.com/photo/2020/03/31/19/20/dog-4988985_1280.jpg', 3, 'Sunny and loving!', 't'),
    ('Porcupi', 'porcupine', 'https://cdn.pixabay.com/photo/2019/07/02/06/31/echidna-4311612_1280.jpg', 2, 'Spiky and adorable!', 't'),
    ('Meowie', 'cat', 'https://cdn.pixabay.com/photo/2018/04/20/17/18/cat-3336579_1280.jpg', 1, null, 't'),
    ('Clawsie', 'cat', NULL, NULL, NULL, false);