DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS comments;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    pass_word TEXT NOT NULL,
    bio VARCHAR(200) NOT NULL DEFAULT "",
    pic LONGBLOB NOT NULL DEFAULT "static/unk.jpg"
);

CREATE TABLE posts(
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL DEFAULT "", 
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pic LONGBLOB NOT NULL DEFAULT "static/unk.jpg",
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE comments(
    comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (post_id) REFERENCES posts(post_id)
);