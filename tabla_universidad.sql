CREATE TABLE IF NOT EXISTS university(
    id_university INTEGER PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE table IF NOT EXISTS country(
    id_country INTEGER PRIMARY KEY,
    name varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS city(
    id_city INTEGER PRIMARY KEY,
    name varchar(255) NOT NULL,
    id_country INTEGER,
    CONSTRAINT fk_id_country
    FOREIGN KEY (id_country) REFERENCES
    country(id_country)
);
/*
id 
first_name
last_name
email
gender
city
country
university
*/

Create table if not exists person(
    id_person int PRIMARY KEY,
    first_name varchar(50),
    last_name varchar (50),
    email varchar(100),
    gender varchar (50),
    city_id INTEGER,
    country_id INTEGER,
    university_id INTEGER,
    CONSTRAINT fk_city_id FOREIGN KEY (city_id) REFERENCES city(id_city),
    CONSTRAINT fk_country_id FOREIGN KEY (country_id) REFERENCES country(id_country),
    CONSTRAINT fk_university_id FOREIGN Key (university_id) REFERENCES university(id_university)
);