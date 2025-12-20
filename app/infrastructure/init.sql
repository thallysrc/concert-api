CREATE TABLE concerts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    date TIMESTAMPTZ NOT NULL,
    image_url TEXT NOT NULL,
    location TEXT NOT NULL,
    price DOUBLE PRECISION,
    participants INTEGER
);