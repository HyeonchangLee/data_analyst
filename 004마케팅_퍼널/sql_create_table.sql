CREATE TABLE sales_table (
 seq        INT NOT NULL ,
 invoice_no     VARCHAR(30),
 stock_code    VARCHAR(30),
 description   VARCHAR(500),
 quantity    INT,  
 invoice_date    DATETIME,  
 unit_price    FLOAT,  
 custome_id    VARCHAR(20),  
 country   VARCHAR(50),
  PRIMARY KEY(seq)
) ENGINE=MYISAM ;