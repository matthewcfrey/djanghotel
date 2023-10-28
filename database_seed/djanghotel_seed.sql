--this file is to seed the database in your local environment

INSERT INTO booking_room 
(room_number, num_beds, smoking, description) 
VALUES 
(101, 2, FALSE, 'Our standard room'),
(102, 2, TRUE, 'Our standard smoking room'),
(103, 4, FALSE, 'Plenty of room for activities'),
(104, 4, TRUE, 'Plenty of room for activities and smoking'),
(105, 3, FALSE, 'Our fifth room')

INSERT INTO booking_roomcost
(room_id, cost)
VALUES
(101, 200),
(102, 300),
(103, 500),
(104, 600),
(105, 600)

INSERT INTO chat_responses
(keyword, resp)
VALUES
('thank you', 'You are welcome!'),
('responsenotfound', 'We did not recognize your issue. Please leave us a message here:'),
('representative', 'Someone should be with you shortly...'),
('hello', 'Hello! Thank you for chatting with Automod.'),
('booking', 'To book a room, visit this link:')