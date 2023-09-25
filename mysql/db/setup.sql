CREATE TABLE `user` (
  `user_id` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) UNIQUE NOT NULL,
  `phone` varchar(255) NOT NULL
);

CREATE TABLE `vote` (
  `vote_id` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `type` enum("one_select", "many_select", "one_bolean", "many_bolean") DEFAULT "one_select" NOT NULL,
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `context` text,
  `status` enum("upcoming", "ongoing", "completed") DEFAULT "upcoming",
  `time_created` datetime NOT NULL,
  `user_id` integer
);

CREATE TABLE `option` (
  `option_id` integer PRIMARY KEY AUTO_INCREMENT,
  `vote_id` integer,
  `content` text 
);

CREATE TABLE `result_select` (
  `user_id` integer,
  `option_id` integer,
  PRIMARY KEY (`user_id`, `option_id`)
);
CREATE TABLE `result_many_boolean` (
  `user_id` integer,
  `option_id` integer,
  `answer` enum("true", "false") DEFAULT "false",
  PRIMARY KEY (`user_id`, `option_id`)
);

CREATE TABLE `result_one_boolean` (
  `user_id` integer,
  `vote_id` integer,
  `answer` enum("true", "false") DEFAULT "false",
  PRIMARY KEY (`user_id`, `vote_id`)
);

ALTER TABLE `vote` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

ALTER TABLE `option` ADD FOREIGN KEY (`vote_id`) REFERENCES `vote` (`vote_id`);

ALTER TABLE `result_select` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

ALTER TABLE `result_select` ADD FOREIGN KEY (`option_id`) REFERENCES `option` (`option_id`);

ALTER TABLE `result_many_boolean` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

ALTER TABLE `result_many_boolean` ADD FOREIGN KEY (`option_id`) REFERENCES `option` (`option_id`);

ALTER TABLE `result_one_boolean` ADD FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`);

ALTER TABLE `result_one_boolean` ADD FOREIGN KEY (`vote_id`) REFERENCES `vote` (`vote_id`);

INSERT INTO user (name, Email, phone)
VALUES
  ('NguyenVan A', 'nguyen111vana@example.com', '01243456789'),
  ('TranThi B', 'tranthib@example.com', '0987654321'),
  ('LeMinh C', 'leminhc@example.com', '0369842157'),
 ('Phạm Đức D', 'phamducd@example.com', '0123456780'),
  ('Nguyễn Hoàng E', 'nguyenhoange@example.com', '0987654320'),
  ('Vũ Ngọc F', 'vungocf@example.com', '0369842150'),
  ('Hoàng Thu G', 'hoangthug@example.com', '0123456781'),
  ('Lý Thành H', 'lythanh@example.com', '0987654322'),
  ('Trần Hòa I', 'tranhoai@example.com', '0369842152'),
  ('Nguyễn Tùng K', 'nguyentungk@example.com', '0123456782'),
  ('Đinh Thị L', 'dinhthil@example.com', '0987654323'),
  ('Phan Văn M', 'phanvanm@example.com', '0369842153'),
  ('Lê Quang N', 'lequangn@example.com', '0123456783'),
  ('Võ Đức P', 'voducp@example.com', '0987654324'),
  ('Hoàng Quốc R', 'hoangquocr@example.com', '0369842154');

INSERT INTO vote (name, type, start_time, end_time, context, status, time_created, user_id)
VALUES
  ('Cuộc bầu chọn 1', "one_select", '2023-09-19 08:00:00', '2023-09-19 17:00:00', 'Nội dung cuộc bầu chọn 1', 'upcoming', '2023-09-19 10:00:00', 1),
  ('Cuộc bầu chọn 2', "one_select", '2023-09-20 09:00:00', '2023-09-20 18:00:00', 'Nội dung cuộc bầu chọn 2', 'ongoing', '2023-09-20 11:30:00', 2),
  ('Cuộc bầu chọn 3', "one_select", '2023-09-21 10:00:00', '2023-09-21 19:00:00', 'Nội dung cuộc bầu chọn 3', 'completed', '2023-09-21 12:45:00', 3),
  ('Cuộc bầu chọn 4', "one_select", '2023-09-22 10:00:00', '2023-09-22 19:00:00', 'Nội dung cuộc bầu chọn 4', 'upcoming', '2023-09-22 12:00:00', 4),
  ('Cuộc bầu chọn 5', 'many_select', '2023-09-19 08:00:00', '2023-09-19 17:00:00', 'Nội dung cuộc bầu chọn 5', 'upcoming', '2023-09-19 10:00:00', 1),
  ('Cuộc bầu chọn 6', 'many_select', '2023-09-20 09:00:00', '2023-09-20 18:00:00', 'Nội dung cuộc bầu chọn 6', 'ongoing', '2023-09-20 11:30:00', 2),
  ('Cuộc bầu chọn 7', 'many_select', '2023-09-21 10:00:00', '2023-09-21 19:00:00', 'Nội dung cuộc bầu chọn 7', 'completed', '2023-09-21 12:45:00', 3),
('Cuộc bầu chọn 8', 'one_bolean', '2023-09-22 08:00:00', '2023-09-22 17:00:00', 'Nội dung cuộc bầu chọn 8', 'upcoming', '2023-09-22 10:00:00', 4),
  ('Cuộc bầu chọn 9', 'one_bolean', '2023-09-23 09:00:00', '2023-09-23 18:00:00', 'Nội dung cuộc bầu chọn 9', 'ongoing', '2023-09-23 11:30:00', 5),
  ('Cuộc bầu chọn 10', 'one_bolean', '2023-09-24 10:00:00', '2023-09-24 19:00:00', 'Nội dung cuộc bầu chọn 10', 'completed', '2023-09-24 12:45:00', 6),
 ('Cuộc bầu chọn 11', 'many_bolean', '2023-09-25 08:00:00', '2023-09-25 17:00:00', 'Nội dung cuộc bầu chọn 11', 'upcoming', '2023-09-25 10:00:00', 7),
  ('Cuộc bầu chọn 12', 'many_bolean', '2023-09-26 09:00:00', '2023-09-26 18:00:00', 'Nội dung cuộc bầu chọn 12', 'ongoing', '2023-09-26 11:30:00', 8),
  ('Cuộc bầu chọn 13', 'many_bolean', '2023-09-27 10:00:00', '2023-09-27 19:00:00', 'Nội dung cuộc bầu chọn 13', 'completed', '2023-09-27 12:45:00', 9);


INSERT INTO `option` (vote_id, content)
VALUES
  (1, 'Tùy chọn 1 cho cuộc bầu chọn 1'),
  (1, 'Tùy chọn 2 cho cuộc bầu chọn 1'),
  (2, 'Tùy chọn 1 cho cuộc bầu chọn 2'),
  (2, 'Tùy chọn 2 cho cuộc bầu chọn 2'),
  (3, 'Tùy chọn 1 cho cuộc bầu chọn 3'),
  (3, 'Tùy chọn 2 cho cuộc bầu chọn 3'),
  (4, 'Tùy chọn 1 cho cuộc bầu chọn 4'),
  (4, 'Tùy chọn 2 cho cuộc bầu chọn 4'),
  (5, 'Tùy chọn 1 cho cuộc bầu chọn 5'),
  (5, 'Tùy chọn 2 cho cuộc bầu chọn 5'),
  (5, 'Tùy chọn 3 cho cuộc bầu chọn 5'),
  (5, 'Tùy chọn 4 cho cuộc bầu chọn 5'),
  (6, 'Tùy chọn 1 cho cuộc bầu chọn 6'),
  (6, 'Tùy chọn 2 cho cuộc bầu chọn 6'),
  (6, 'Tùy chọn 3 cho cuộc bầu chọn 6'),
  (6, 'Tùy chọn 4 cho cuộc bầu chọn 6'),
   (7, 'Tùy chọn 1 cho cuộc bầu chọn 7'),
  (7, 'Tùy chọn 2 cho cuộc bầu chọn 7'),
  (7, 'Tùy chọn 3 cho cuộc bầu chọn 7'),
  (7, 'Tùy chọn 4 cho cuộc bầu chọn 7'),
  (11, 'Tùy chọn 1 cho Cuộc bầu chọn 11'),
  (11, 'Tùy chọn 2 cho Cuộc bầu chọn 11'),
  (11, 'Tùy chọn 3 cho Cuộc bầu chọn 11'),
  (11, 'Tùy chọn 4 cho Cuộc bầu chọn 11'),
  (12, 'Tùy chọn 1 cho Cuộc bầu chọn 12'),
  (12, 'Tùy chọn 2 cho Cuộc bầu chọn 12'),
  (12, 'Tùy chọn 3 cho Cuộc bầu chọn 12'),
  (12, 'Tùy chọn 4 cho Cuộc bầu chọn 12'),
  (13, 'Tùy chọn 1 cho Cuộc bầu chọn 13'),
  (13, 'Tùy chọn 2 cho Cuộc bầu chọn 13'),
  (13, 'Tùy chọn 3 cho Cuộc bầu chọn 13'),
  (13, 'Tùy chọn 4 cho Cuộc bầu chọn 13');

INSERT INTO result_select (user_id, option_id)
VALUES
  (1, 1),
  (10, 1),
  (2, 2),
  (6, 2),
  (11, 2),
  (15, 2),
  (9, 3),
  (10, 3),
  (2, 4),
  (13, 5),
  (4, 5),
  (8, 6),
  (10, 7),
  (11, 7),
  (3, 8),
  (5, 8),
  (6, 8),
  (15, 8);

 INSERT INTO result_select (user_id, option_id)
VALUES
  (8, 9), (5, 9), (2, 9), (14, 9), (10, 9), (4, 9), (6, 10), (3, 10), (15, 10), (11, 10), 
  (7, 10), (4, 11), (1, 11), (12, 11), (9, 11), (5, 11), (2, 11), (14, 11), (13, 11), (8, 11), (6, 11),
  (7, 12), (8, 12), (5, 12), (2, 12), (14, 12), (10, 12), (6, 13), (3, 13), (15, 13), (7, 14), (4, 14), (10, 14), (1, 14), (5, 14), (2, 16), 
  (14, 16), (13, 16), (8, 16), (6, 16), (11, 16), (7, 17), (8, 17), (5, 17), (2, 17), (14, 17), (10, 17), (6, 17),
  (3, 17), (15, 18), (11, 18), (7, 19), (4, 19), (10, 19), (1, 19), (12, 19), (9, 19), (5, 19), (2, 19), (14, 20), (13, 20), (8, 20), (6, 20), (11, 20), (7, 20);

  INSERT INTO result_one_boolean (user_id, vote_id, answer)
VALUES
(5, 8, "true"),
(2, 8, "false"),
(14, 8, "true"),
(10, 8, "false"),
(6, 8, "false"),
(3, 8, "true"),
(15, 8, "false"),
(11, 9, "true"),
(7, 9, "false"),
(4, 9, "false"),
(10, 9, "true"),
(2, 9, "false"),
(1, 9, "true"),
(8, 9, "true"),
(13, 9, "true"),
(12, 9, "true"),
(9, 10, "true"),
(1, 10, "true"),
(6, 10, "false"),
(8, 10, "false"),
(13, 10, "true"),
(15, 10, "false"),
(11, 10, "true"),
(7, 10, "false"),
(4, 10, "false");

INSERT INTO result_many_boolean (user_id, option_id, answer)
VALUES
(6, 21, "false"),
(8, 21, "false"),
(13, 21, "true"),
(15, 21, "false"),
(11, 21, "true"),
(7, 21, "false"),
(4, 22, "false"),
(14, 22, "true"),
(1, 22, "false"),
(2, 22, "true"),
(9, 22, "false"),
(5, 22, "true"),
(5, 23, "true"),
(2, 23, "false"),
(14, 23, "true"),
(10, 23, "false"),
(6, 23, "false"),
(3, 23, "true"),
(15, 23, "false"),
(11, 24, "true"),
(7, 24, "false"),
(4, 24, "false"),
(10, 24, "true"),
(2, 24, "false"),
(1, 24, "true"),
(8, 24, "true"),
(13, 25, "true"),
(12, 25, "true"),
(9, 25, "true"),
(1, 25, "true"),
(6, 25, "false"),
(8, 25, "false"),
(2, 25, "true"),
(15, 26, "false"),
(11, 26, "true"),
(2, 26, "false"),
(10, 26, "false"),
(13, 26, "true"),
(1, 26, "false"),
(7, 27, "false"),
(4, 27, "false"),
(6, 27, "false"),
(8, 27, "false"),
(13, 27, "true"),
(15, 27, "false"),
(11, 28, "true"),
(7, 28, "false"),
(4, 28, "false"),
(14, 28, "true"),
(1, 28, "false"),
(2, 28, "true"),
(9, 28, "false"),
(5, 29, "true"),
(2, 29, "false"),
(14, 29, "true"),
(10, 29, "false"),
(6, 29, "false"),
(3, 29, "true"),
(15, 29, "false"),
(11, 29, "true"),
(7, 29, "false"),
(4, 29, "false"),
(10, 30, "true"),
(2, 30, "false"),
(1, 30, "true"),
(8, 30, "true"),
(13, 30, "true"),
(12, 30, "true"),
(9, 30, "true"),
(1, 31, "true"),
(6, 31, "false"),
(8, 31, "false"),
(13, 31, "true"),
(15, 31, "false"),
(11, 31, "true"),
(2, 31, "false"),
(10, 31, "false"),
(13, 29, "true"),
(15, 30, "false"),
(7, 31, "false"),
(4, 31, "false"),
(6, 32, "false"),
(8, 32, "false"),
(13, 32, "true"),
(15, 32, "false"),
(11, 32, "true"),
(7, 32, "false"),
(4, 32, "false"),
(14, 32, "true"),
(1, 32, "false"),
(2, 32, "true"),
(9, 32, "false");