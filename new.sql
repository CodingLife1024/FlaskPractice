DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS posts;

CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    pass_word TEXT NOT NULL,
    bio VARCHAR(200) NOT NULL DEFAULT "",
    pic LONGBLOB NOT NULL DEFAULT "static/unk.jpg"
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;;

CREATE TABLE posts(
    post_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    content TEXT NOT NULL DEFAULT "", 
    created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    pic LONGBLOB NOT NULL DEFAULT "static/unk.jpg",
    FOREIGN KEY (user_id) REFERENCES users(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;;