DELETE FROM Auteurs;
DELETE FROM Audio_Types;
DELETE FROM OeuvreAudios;
DELETE FROM Clients;
DELETE FROM Ecrit;
DELETE FROM Possede;

INSERT INTO Audio_Types VALUES("audiobook", 600);
INSERT INTO Audio_Types VALUES("song", 20);
INSERT INTO Audio_Types VALUES("podcast", 600);
INSERT INTO Clients VALUES(100, "Ronald", "Domi", '13-04-2002');
-- INSERT INTO Possede VALUES(100, 300);



INSERT INTO OeuvreAudios VALUES(300, "Earth", 59.99, "song");       
INSERT INTO OeuvreAudios VALUES(301, "Professional Rapper", 69.99, "song");       
INSERT INTO OeuvreAudios VALUES(302, "Without Me", 39.99, "song");       
INSERT INTO OeuvreAudios VALUES(303, "Zeus", 60.00, "song");       
INSERT INTO OeuvreAudios VALUES(304, "California Love", 10.00, "song");       
INSERT INTO OeuvreAudios VALUES(305, "Drop It Like It's Hot", 100.99, "song");        
INSERT INTO OeuvreAudios VALUES(306, "The Old Man and The Sea", 19.99, "audiobook");        
INSERT INTO OeuvreAudios VALUES(307, "#1034 - Elon Musk", 19.99, "podcast");        
INSERT INTO OeuvreAudios VALUES(308, "#995 - Jordan Peterson", 19.99, "podcast");        
INSERT INTO OeuvreAudios VALUES(309, "How to unlock your potential", 29.99, "podcast");        
INSERT INTO OeuvreAudios VALUES(310, "Life", 200.99, "podcast");        


-- Rappers
INSERT INTO Auteurs VALUES(200, "LilDicky");                                
INSERT INTO Auteurs VALUES(201, "Eminem");                                
INSERT INTO Auteurs VALUES(202, "DrDre");                                
INSERT INTO Auteurs VALUES(203, "SnoopDog");                                
INSERT INTO Auteurs VALUES(204, "Xzibit");                                
-- Autheurs
INSERT INTO Auteurs VALUES(205, "Ernest Hemingway");                                
INSERT INTO Auteurs VALUES(206, "Mark Twain");                                
INSERT INTO Auteurs VALUES(207, "George Orwell");                                
INSERT INTO Auteurs VALUES(208, "Ronald Domi");                                
-- Podcasters
INSERT INTO Auteurs VALUES(209, "Joe Rogan");                                
INSERT INTO Auteurs VALUES(210, "Tom Bilyeu");                                
INSERT INTO Auteurs VALUES(211, "Sadhguru");                                 

INSERT INTO Ecrit VALUES(200, 300);        
INSERT INTO Ecrit VALUES(200, 301);        
INSERT INTO Ecrit VALUES(201, 302);        
INSERT INTO Ecrit VALUES(201, 303);        
INSERT INTO Ecrit VALUES(202, 304);        
INSERT INTO Ecrit VALUES(203, 305);        
INSERT INTO Ecrit VALUES(205, 306);        
INSERT INTO Ecrit VALUES(209, 307);        
INSERT INTO Ecrit VALUES(209, 308);        
INSERT INTO Ecrit VALUES(210, 309);        
INSERT INTO Ecrit VALUES(211, 310);        




