\c company_db

insert into company values (1, 'Apple');
insert into company values (2, 'AMD');
insert into company values (3, 'Google');
insert into company values (4, 'Amazon');
insert into company values (5, 'Facebook');
insert into company values (6, 'Samsung');
insert into company values (7, 'Sony');
insert into company values (8, 'Musk Inc');


INSERT into DEPARTMENT values('iPad',  NULL, 1, 1);
INSERT into DEPARTMENT values('MAC',  NULL, 1, 2);

INSERT into DEPARTMENT values('Ryzen', NULL, 2, 1);
INSERT into DEPARTMENT values('Radeon', NULL, 2, 2);

INSERT into DEPARTMENT values('YouTube', NULL, 3, 1);
INSERT into DEPARTMENT values('Android', NULL, 3, 2);

INSERT into DEPARTMENT values('Amazon Shopping', NULL, 4, 1);
INSERT into DEPARTMENT values('AWS', NULL, 4, 2);

INSERT into DEPARTMENT values('WhatsApp', NULL, 5, 1);
INSERT into DEPARTMENT values('Instagram', NULL, 5, 2);

INSERT into DEPARTMENT values('Phones', NULL, 6, 1);
INSERT into DEPARTMENT values('Televisions', NULL, 6, 2);

INSERT into DEPARTMENT values('Camera', NULL, 7, 1);
INSERT into DEPARTMENT values('Bravia TV', NULL, 7, 2);

INSERT into DEPARTMENT values('SpaceX', NULL, 8, 1);
INSERT into DEPARTMENT values('Tesla', NULL, 8, 2);

--apple has ipad as department with ipad os as technology
--  Apple
-- -Ipad(Ipad OS)   -MAC(M1)
INSERT into TECHNOLOGIES values(1,'iPad OS',1,1);
INSERT into TECHNOLOGIES values(2,'M1',1,2);
--  amazon
-- -Amazon SHopping(Open Graph)   -AWS(docker)
INSERT into TECHNOLOGIES values(1,'Open Graph',4,1);
INSERT into TECHNOLOGIES values(2,'Docker',4,2);
--  Samasung
-- -Phones(Exynos)   -TV(QLED)
INSERT into TECHNOLOGIES values(1,'Exynos',6,1);
INSERT into TECHNOLOGIES values(2,'QLED',6,2);
--  SOny
-- -Camera(Image processing)   -TV(Dolby)
INSERT into TECHNOLOGIES values(1,'Image Processing',7,1);
INSERT into TECHNOLOGIES values(2,'Dolby',7,2);
--  Google
-- -Youtube(Recommendation algo)   -Android(Dalvik)
INSERT into TECHNOLOGIES values(1,'Recommendation Algorithm',3,1);
INSERT into TECHNOLOGIES values(2,'Dalvik',3,2);
--  Musk Inc
-- -SPaceX(Robotic Landing)   -Tesla(Autopilot)
INSERT into TECHNOLOGIES values(1,'Robotic Landing',8,1);
INSERT into TECHNOLOGIES values(2,'Autopilot',8,2);
--  Facebook
-- -Whatsapp(end to end encryption)   -Instagram(Reels)
INSERT into TECHNOLOGIES values(1,'End to End encryption',5,1);
INSERT into TECHNOLOGIES values(2,'Reels',5,2);
--  AMD
-- -Ryzen(SMT)   -Radeon(GPU rendering)
INSERT into TECHNOLOGIES values(1,'SMT',2,1);
INSERT into TECHNOLOGIES values(2,'GPU rendering',2,2);

INSERT into EMPLOYEE values ('Ap0001','Eager Chomu', 1, '450 Stone, Houston,TX', 98745632145 , 'Software engineer', 550000, 1, 1);
INSERT into EMPLOYEE values ('Ap0002','John Smith', 2, '839 Alaska, Houston,TX', 9783498134 , 'Product Manager', 400000, 1, 1);
INSERT into EMPLOYEE values ('Ap0003','Chandler Wong',3,'731 Fondren,Houston,TX',123456789,'Performance analyst',300000, 2 ,1);
INSERT into EMPLOYEE values ('Ap0004','Franklin Wade',4,'638 voss,Houston,TX', 8886655554, 'Performance analyst', 250000, 2, 1);

INSERT into Teaching values(8,'Ap0001',1,1,1);
INSERT into Teaching values(6,'Ap0003',2,2,1);
INSERT into Learning values(7,'Ap0002',1,1,1);
INSERT into Learning values(9,'Ap0004',2,2,1);

INSERT into EMPLOYEE values ('AMD0005','Alicia J Zelaya', 1, '232 Mary street, Britain', 3212343212 , 'Performance analyst', 100000, 1, 2);
INSERT into EMPLOYEE values ('AMD0006','Buddy M Thomson', 2, '710 McVaney Road, North Carolina', 127123737 , 'Performance analyst', 76000, 1, 2);
INSERT into EMPLOYEE values ('AMD0007','Katie B Patterson',3,'1672 Ryder Avenue, Washington',	3018586098,'Graphics engineer',150000, 2 ,2);
INSERT into EMPLOYEE values ('AMD0008','Wayne L Stennett',4,'473 Tree Top Lane, Texas', 5025225878, 'Graphics engineer', 120000, 2, 2);

INSERT into Teaching values(7,'AMD0005',1,1,2);
INSERT into Teaching values(8,'AMD0007',2,2,2);
INSERT into Learning values(2,'AMD0006',1,1,2);
INSERT into Learning values(9,'AMD0008',2,2,2);

INSERT into EMPLOYEE values ('Go0009','Anthony R Hines', 1, '618 Dancing Dove Lane, New York', 6315600424 , 'Recommendation tweaking', 125000, 1, 3);
INSERT into EMPLOYEE values ('Go0010','Jennifer Quint', 2, '415, Azzefr, Germany', 123523123 , 'Recommendation tweaking', 110000, 1, 3);
INSERT into EMPLOYEE values ('Go0011','Zoeey Cer',3,'3923 Del Dew Drive, Saint Margarets, Maryland', 3018586098,'Pipeline engineer',350000, 2 ,3);
INSERT into EMPLOYEE values ('Go0012','Anna C Debnam',4,'524 Gregory Lane, Louisville, Kentucky', 5025225878, 'Pipeline engineer', 220000, 2, 3);

INSERT into Teaching values(10,'Go0009',1,1,3);
INSERT into Teaching values(8,'Go0011',2,2,3);
INSERT into Learning values(6,'Go0010',1,1,3);
INSERT into Learning values(10,'Go0012',2,2,3);

INSERT into EMPLOYEE values ('Amz0013','Larry S Valle', 1, '911 Chenoweth Drive, Tennessee', 9314572434 , 'Machine Learning', 105000, 1, 4);
INSERT into EMPLOYEE values ('Amz0014','Wayne C Payne', 2, '931 Chenoweth Drive, Tennessee', 2748329172 , 'Machine Learning', 75000, 1, 4);
INSERT into EMPLOYEE values ('Amz0015','Cynthia M Barker',3,'3150 Franklin Avenue, MOKANE, Missouri',	3862127374,'Hardware acceleration',155000, 2 ,4);
INSERT into EMPLOYEE values ('Amz0016','Kevin M Godfrey',4,'602 Black Oak Hollow Road, PETACA, New Mexico', 4087441893, 'Hardware acceleration', 100000, 2, 4);

INSERT into Teaching values(4,'Amz0013',1,1,4);
INSERT into Teaching values(8,'Amz0015',2,2,4);
INSERT into Learning values(9,'Amz0014',1,1,4);
INSERT into Learning values(9,'Amz0016',2,2,4);

INSERT into EMPLOYEE values ('Fb0017','Vickie R Donovan', 1, '2847 Chandler Drive, Sparta, Missouri', 4176347176 , 'Encryption expert', 90000, 1, 5);
INSERT into EMPLOYEE values ('Fb0018','Vivian B Rice', 2, '1775 Hazelwood Avenue, Tennessee', 8704262871 , 'Encryption expert', 80000, 1, 5);
INSERT into EMPLOYEE values ('Fb0019','Grace B Zambrano',3,'4692 Virgil Street, Tallahassee',	8502730725,'Pipeline engineer',135000, 2 ,5);
INSERT into EMPLOYEE values ('Fb0020','',4,'524 Gregory Lane, Louisville, Kentucky', 5025225878, 'Pipeline engineer', 115000, 2, 5);


INSERT into Teaching values(6,'Fb0017',1,1,5);
INSERT into Teaching values(9,'Fb0019',2,2,5);
INSERT into Learning values(6,'Fb0018',1,1,5);
INSERT into Learning values(9,'Fb0020',2,2,5);


INSERT into EMPLOYEE values ('Sg0021','Mary J Crist', 1, '406 Lynch Street, Florida', 9209299544 , 'Thermal management', 100000, 1, 6);
INSERT into EMPLOYEE values ('Sg0022','Gary M Allison', 2, '559 Roosevelt Street, California', 4154444712 , 'Thermal management', 85000, 1, 6);
INSERT into EMPLOYEE values ('Sg0023','Rosemary B King',3,'33081 Cerullo Road, 3081 Cerullo Road',	502396342,'Pixel engineer',70000, 2 ,6);
INSERT into EMPLOYEE values ('Sg0024','Loretta J Warren',4,'921 Cabell Avenue, Virginia', 7035620072, 'Pixel engineer', 60000, 2, 6);


INSERT into Teaching values(9,'Sg0021',1,1,6);
INSERT into Teaching values(10,'Sg0023',2,2,6);
INSERT into Learning values(3,'Sg0022',1,1,6);
INSERT into Learning values(10,'Sg0024',2,2,6);

INSERT into EMPLOYEE values ('Sy0025','Mary R Langhorne', 1, '390 Pooh Bear Lane, South Carolina', 8646804361 , 'Face recognition expert', 200000, 1, 7);
INSERT into EMPLOYEE values ('Sy0026','Connie J Lema', 2, '3838 Retreat Avenue, Maine', 2073544959 , 'Face recognition expert', 200000, 1, 7);
INSERT into EMPLOYEE values ('Sy0027','Loretta K Trapp',3,'1416 Sycamore Road, Oregon',	5413962217,'Audio Engineer', 175000, 2 ,7);
INSERT into EMPLOYEE values ('Sy0028','Velma R McKinnon',4,'3153 Hilltop Drive, Texas', 8062733116, 'Audio Engineer', 150000, 2, 7);

INSERT into Teaching values(4,'Sy0025',1,1,7);
INSERT into Teaching values(2,'Sy0027',2,2,7);
INSERT into Learning values(9,'Sy0026',1,1,7);
INSERT into Learning values(10,'Sy0028',2,2,7);

INSERT into EMPLOYEE values ('MI0029','Anne R Burlison', 1, '2774 Hannah Street, North Carolina', 8283969740 , 'Research head', 500000, 1, 8);
INSERT into EMPLOYEE values ('MI0030','Emily L Curci', 2, '4410 Bel Meadow Drive, California', 909-445-9677 , 'Reasearch', 100000, 1, 8);
INSERT into EMPLOYEE values ('MI0031','Paula W Branum',3,'891 White River Way, Utah',	8015107395, 'ML and Image Processing expert', 165000, 2 ,8);
INSERT into EMPLOYEE values ('MI0032','Susan T Herbert',4,'2732 New Street, Oregon', 5025225878, 'ML and Image Processing', 130000, 2, 8);

INSERT into Teaching values(7,'MI0029',1,1,8);
INSERT into Teaching values(6,'MI0031',2,2,8);
INSERT into Learning values(10,'MI0030',1,1,8);
INSERT into Learning values(10,'MI0032',2,2,8);


Alter Table Department add constraint department_mgr_ssn_fkey FOREIGN KEY (Mgr_ssn) REFERENCES  EMPLOYEE(Ssn);
Update Department set mgr_ssn='Ap0001' where( departmentid=1 and companyid=1);
Update Department set mgr_ssn='Ap0003' where( departmentid=2 and companyid=1);

Update Department set mgr_ssn='AMD0005' where( departmentid=1 and companyid=2);
Update Department set mgr_ssn='AMD0007' where( departmentid=2 and companyid=2);

Update Department set mgr_ssn='Go0009' where( departmentid=1 and companyid=3);
Update Department set mgr_ssn='Go0011' where( departmentid=2 and companyid=3);

Update Department set mgr_ssn='Amz0013' where( departmentid=1 and companyid=4);
Update Department set mgr_ssn='Amz0015' where( departmentid=2 and companyid=4);

Update Department set mgr_ssn='Fb0017' where( departmentid=1 and companyid=5);
Update Department set mgr_ssn='Fb0019' where( departmentid=2 and companyid=5);

Update Department set mgr_ssn='Sg0021' where( departmentid=1 and companyid=6);
Update Department set mgr_ssn='Sg0023' where( departmentid=2 and companyid=6);

Update Department set mgr_ssn='Sy0025' where( departmentid=1 and companyid=7);
Update Department set mgr_ssn='Sy0027' where( departmentid=2 and companyid=7);

Update Department set mgr_ssn='MI0029' where( departmentid=1 and companyid=8);
Update Department set mgr_ssn='MI0031' where( departmentid=2 and companyid=8);
--apple has ipad as department with ipad os as technology
--  Apple
-- -Ipad(Ipad OS)   -MAC(M1)
-- INSERT into TECHNOLOGIES values(1,'iPad OS',1,1);
-- INSERT into TECHNOLOGIES values(2,'M1',1,2);
-- --  amazon
-- -- -Amazon SHopping(Open Graph)   -AWS(docker)
-- INSERT into TECHNOLOGIES values(1,'Open Graph',4,1);
-- INSERT into TECHNOLOGIES values(2,'Docker',4,2);
-- --  Samasung
-- -- -Phones(Exynos)   -TV(QLED)
-- INSERT into TECHNOLOGIES values(1,'Exynos',6,1);
-- INSERT into TECHNOLOGIES values(2,'QLED',6,2);
-- --  SOny
-- -- -Camera(Image processing)   -TV(Dolby)
-- INSERT into TECHNOLOGIES values(1,'Image Processing',7,1);
-- INSERT into TECHNOLOGIES values(2,'Dolby',7,2);
-- --  Google
-- -- -Youtube(Recommendation algo)   -Android(Dalvik)
-- INSERT into TECHNOLOGIES values(1,'Recommendation Algorithm',3,1);
-- INSERT into TECHNOLOGIES values(2,'Dalvik',3,2);
-- --  Musk Inc
-- -- -SPaceX(Robotic Landing)   -Tesla(Autopilot)
-- INSERT into TECHNOLOGIES values(1,'Robotic Landing',8,1);
-- INSERT into TECHNOLOGIES values(2,'Autopilot',8,2);
-- --  Facebook
-- -- -Whatsapp(end to end encryption)   -Instagram(Reels)
-- INSERT into TECHNOLOGIES values(1,'End to End encryption',5,1);
-- INSERT into TECHNOLOGIES values(2,'Reels',5,2);
-- --  AMD
-- -- -Ryzen(SMT)   -Radeon(GPU rendering)
-- INSERT into TECHNOLOGIES values(1,'SMT',2,1);
-- INSERT into TECHNOLOGIES values(2,'GPU rendering',2,2);




-- INSERT into DEPENDENT values(333445555, 'Alice', 'F', '1986-04-05','Daughter');
-- INSERT into DEPENDENT values(333445555, 'Theodore', 'M', '1983-10-25','Son');
-- INSERT into DEPENDENT values(333445555, 'Joy', 'F', '1958-05-03','Spouse');
-- INSERT into DEPENDENT values(987654321, 'Abner', 'M', '1942-02-28','Spouse');
-- INSERT into DEPENDENT values(123456789, 'Michael', 'F', '1988-01-04','Son');
-- INSERT into DEPENDENT values(123456789, 'Alice', 'F', '1988-12-30','Daughter');	
-- INSERT into DEPENDENT values(123456789, 'Elizabeth', 'F', '1967-05-05','Spouse');
-- 
	













