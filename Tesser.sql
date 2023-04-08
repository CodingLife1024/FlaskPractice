DROP DATABASE IF EXISTS Tesser;

CREATE DATABASE Tesser;

DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE user_info (
    user_id INT(200) NOT NULL AUTO_INCREMENT,
    username VARCHAR(200) NOT NULL,
    pass_word VARCHAR(200) NOT NULL,
    bio VARCHAR(200) NOT NULL,
    PRIMARY KEY (user_id)
);

INSERT INTO Tesser.user_info (username, pass_word, bio) 
VALUES 
    ('nickey','hithere','animal lover'),
    ('JohnDoe', 'mysecretpassword', 'I am a software engineer.'), 
    ('JaneDoe', 'anotherpassword', 'I am a web developer.'),
    ('BobSmith', 'password123', 'I am a data analyst.'),
    ('Ojas','nopassword','traveller');

DROP TABLE IF EXISTS Tesser.posts;

CREATE TABLE Tesser.posts (
    id int(200) NOT NULL,
    post_id int(200) NOT NULL AUTO_INCREMENT,
    user_id int(200) NOT NULL,
    content VARCHAR(200) NOT NULL,
    likes int(200) NOT NULL, 
    dislikes int(200) NOT NULL, 
    time_posted VARCHAR(200) NOT NULL,
    PRIMARY KEY (post_id),
    KEY fk_post_to_user (user_id),
    CONSTRAINT fk_post_to_user FOREIGN KEY (user_id) REFERENCES user_info (user_id) ON UPDATE CASCADE
);

INSERT INTO Tesser.posts (id, user_id, content, likes, dislikes, time_posted)
VALUES
    (1, 1, 'Hello world!', 10, 2, '2023-04-06 12:00:00'),
    (2, 2, 'This is my first post', 15, 1, '2023-04-06 12:30:00'),
    (3, 3, 'I like to travel', 5, 0, '2023-04-06 13:00:00');


DROP TABLE IF EXISTS Tesser.comments;

CREATE TABLE Tesser.comments
(
    user_id int(200) NOT NULL,
    comment_id int(200) NOT NULL AUTO_INCREMENT,
    post_id int(200) NOT NULL,
    comment_material VARCHAR(200) NOT NULL,
    likes int(200) NOT NULL, 
    dislikes int(200) NOT NULL, 
    time_posted VARCHAR(200) NOT NULL,
    PRIMARY KEY (comment_id),
    KEY fk_comment_to_post (post_id),
    CONSTRAINT fk_comment_to_post FOREIGN KEY (post_id) REFERENCES posts (post_id) ON UPDATE CASCADE
);

INSERT INTO Tesser.comments (user_id, post_id, comment_material, likes, dislikes, time_posted) 
VALUES 
    (1, 1, 'Great post!', 5, 0, '2023-04-06 14:00:00'),
    (2, 1, 'Thanks for sharing your thoughts', 2, 1, '2023-04-06 14:30:00'),
    (3, 2, 'I have a question about this', 0, 0, '2023-04-06 15:00:00');


DROP TABLE IF EXISTS Tesser.follow;

CREATE TABLE Tesser.follow
(
    id int(200) NOT NULL AUTO_INCREMENT,
    user1_id int(200) NOT NULL,
    user2_id int(200) NOT NULL,
    PRIMARY KEY (id),
    KEY fk_follow1 (user1_id),
    KEY fk_follow2 (user2_id),
    CONSTRAINT fk_follow1 FOREIGN KEY (user1_id) REFERENCES user_info (user_id) ON UPDATE CASCADE,
    CONSTRAINT fk_follow2 FOREIGN KEY (user2_id) REFERENCES user_info (user_id) ON UPDATE CASCADE
);

INSERT INTO Tesser.follow (user1_id, user2_id)
VALUES
    (2,4),
    (1,4),
    (1,3);

DROP TABLE IF EXISTS Tesser.user_image;

CREATE TABLE Tesser.user_image (
  user_id int(200) NOT NULL,
  pic longblob NOT NULL,
  PRIMARY KEY (user_id)
);

INSERT INTO Tesser.user_image (user_id, pic) VALUES (1, LOAD_FILE('C:/Users/TB Pal/OneDrive/Desktop/MySQL Practice/imgg/10776.jpg'));
INSERT INTO Tesser.user_image (user_id, pic) VALUES (2, LOAD_FILE('C:/Users/TB Pal/OneDrive/Desktop/MySQL Practice/imgg/33217.jpg'));
INSERT INTO Tesser.user_image (user_id, pic) VALUES (3, LOAD_FILE('C:/Users/TB Pal/OneDrive/Desktop/MySQL Practice/imgg/33278.jpg'));
INSERT INTO Tesser.user_image (user_id, pic) VALUES (4, LOAD_FILE('C:/Users/TB Pal/OneDrive/Desktop/MySQL Practice/imgg/ccccc.jpg'));
INSERT INTO Tesser.user_image (user_id, pic) VALUES (5, LOAD_FILE('C:/Users/TB Pal/OneDrive/Desktop/MySQL Practice/imgg/i.jpg'));
