# switch user to 'postgres'!

CREATE DATABASE franksdb;

\c franksdb

CREATE TABLE pingpongs (
  id SERIAL PRIMARY KEY,
  counter INTEGER
);

INSERT INTO pingpongs(id, counter) values(1, 0);