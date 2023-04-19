DROP TABLE IF EXISTS user_info;

CREATE TABLE user_info (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(200) NOT NULL,
    pass_word VARCHAR(200) NOT NULL,
    bio VARCHAR(200) NOT NULL DEFAULT "",
    pic LONGBLOB NOT NULL DEFAULT "static/riddhi.jpeg"
);
