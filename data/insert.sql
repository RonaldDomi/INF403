-- AUDIO TYPES
DELETE FROM Audio_Types;
INSERT INTO Audio_Types VALUES("audiobook", 600);
INSERT INTO Audio_Types VALUES("song", 20);
INSERT INTO Audio_Types VALUES("podcast", 600);

-- CLIENTS
DELETE FROM Clients;
INSERT INTO Clients VALUES(100, "Ronald", "Domi", '13-04-2002');
INSERT INTO Clients VALUES(101, "Zeynel", "Altun", '23-02-2001');
INSERT INTO Clients VALUES(102, "Jean", "Dupont", '02-11-1997');
INSERT INTO Clients VALUES(103, "Paul", "Durand", '23-02-2005');

-- OEUVRE AUDIOS
DELETE FROM OeuvreAudios;
INSERT INTO OeuvreAudios VALUES(300, "Earth", 59.99, "song");       
INSERT INTO OeuvreAudios VALUES(301, "Professional Rapper", 69.99, "song");       
INSERT INTO OeuvreAudios VALUES(302, "Without Me", 200, "song");       
INSERT INTO OeuvreAudios VALUES(303, "Zeus", 60.00, "song");       
INSERT INTO OeuvreAudios VALUES(304, "California Love", 10.00, "song");       
INSERT INTO OeuvreAudios VALUES(305, "Drop It Like It's Hot", 100.99, "song");        
INSERT INTO OeuvreAudios VALUES(306, "The Old Man and The Sea", 19.99, "audiobook");        
INSERT INTO OeuvreAudios VALUES(307, "#1034 - Elon Musk", 19.99, "podcast");        
INSERT INTO OeuvreAudios VALUES(308, "#995 - Jordan Peterson", 19.99, "podcast");        
INSERT INTO OeuvreAudios VALUES(309, "How to unlock your potential", 29.99, "podcast");        
INSERT INTO OeuvreAudios VALUES(310, "Life", 200.99, "podcast");        

-- AUTEURS
DELETE FROM Auteurs;

INSERT INTO Auteurs VALUES(200, "LilGangstar");                                
INSERT INTO Auteurs VALUES(201, "Eminem");                                
INSERT INTO Auteurs VALUES(202, "DrDre");                                
INSERT INTO Auteurs VALUES(203, "SnoopDog");                                
INSERT INTO Auteurs VALUES(204, "Xzibit");                                
INSERT INTO Auteurs VALUES(205, "Ernest Hemingway");                                
INSERT INTO Auteurs VALUES(206, "Mark Twain");                                
INSERT INTO Auteurs VALUES(207, "George Orwell");                                
INSERT INTO Auteurs VALUES(208, "Ronald Domi");                                
INSERT INTO Auteurs VALUES(209, "Joe Rogan");                                
INSERT INTO Auteurs VALUES(210, "Tom Bilyeu");                                
INSERT INTO Auteurs VALUES(211, "Sadhguru");                                 

-- ECRIT
DELETE FROM Ecrit;
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


-- POSSEDE
DELETE FROM Possede;
INSERT INTO Possede VALUES(101, 300);
INSERT INTO Possede VALUES(101, 303);
INSERT INTO Possede VALUES(100, 303);
INSERT INTO Possede VALUES(100, 301);
INSERT INTO Possede VALUES(102, 302);




