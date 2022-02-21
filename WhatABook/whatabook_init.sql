
DROP USER IF EXISTS 'whatabook_user'@'localhost';

-- create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- drop contstraints if they exist
ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

-- drop tables if they exist
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS wishlist;
DROP TABLE IF EXISTS user;

/*
    Create table(s)
*/
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);

INSERT INTO store(locale)
    VALUES('123 Main Street USA, Bellevue, NE 68005');

/*
    insert book records 
*/
INSERT INTO book(book_name, author, details)
    VALUES('To Kill a Mockingbird', 'Harper Lee', 'A horrific racial event viewed through the eyes of a child');

INSERT INTO book(book_name, author, details)
    VALUES('Candide', 'Voltaire', 'Witty French satire of a desperate optimist trampled through fate');

INSERT INTO book(book_name, author, details)
    VALUES('The Republic', 'Plato', 'Society ruled by philosophers and guardians decides who is happier');

INSERT INTO book(book_name, author)
    VALUES('The Odyssey', 'Homer');

INSERT INTO book(book_name, author)
    VALUES('Flowers for Algernon', 'Daniel Keyes');

INSERT INTO book(book_name, author)
    VALUES('Jane Eyre', 'Charlotte Bronte');

INSERT INTO book(book_name, author)
    VALUES('Vilette', 'Charlotte Bronte');

INSERT INTO book(book_name, author)
    VALUES('The Illiad', 'Homer');

INSERT INTO book(book_name, author)
    VALUES('The Professor', 'Charlotte Bronte');

INSERT INTO book(book_name, author)
    VALUES('Wuthering Heights', 'Emily Bronte');
/*
    insert user
*/ 
INSERT INTO user(first_name, last_name) 
    VALUES('Charles', 'Dickens');

INSERT INTO user(first_name, last_name)
    VALUES('Mark', 'Twain');

INSERT INTO user(first_name, last_name)
    VALUES('Pearl', 'Buck');

/*
    insert wishlist records 
*/
INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Charles'), 
        (SELECT book_id FROM book WHERE book_name = 'Villette')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Mark'),
        (SELECT book_id FROM book WHERE book_name = 'Candide')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Pearl'),
        (SELECT book_id FROM book WHERE book_name = 'Flowers for Algernon')
    );
