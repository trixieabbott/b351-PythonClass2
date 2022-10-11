

CREATE TABLE Customer_T
    (CustomerID                     NUMBER(11,0)        NOT NULL,
    CustomerName                    VARCHAR2(25)        NOT NULL,
    CustomerAddress                 VARCHAR2(30),
    CustomerCity                    VARCHAR2(20),
    CustomerState                   CHAR(2),
    CustomerPostalCode              VARCHAR2(9)
CONSTRAINT Customer_PK PRIMARY KEY (CustomerID));

CREATE TABLE Order_T
    (OrderID                        NUMBER(11,0)        NOT NULL,
    OrderDate                       DATE DEFAULT SYSDATE,
    CustomerID                      NUMBER(11,0),
CONSTRAINT Order_PK PRIMARY KEY (OrderID),
CONSTRAINT Order_FK FOREIGN KEY (CustomerID) REFERENCES Customer_T(CustomerID));

CREATE TABLE Product_T
    (ProductID                      NUMBER(11,0)        NOT NULL,
    ProductDescription              VARCHAR2(50),
    ProductFinish                   VARCHAR2(20)
                        CHECK (ProductFinish IN ('Cherry','Natural Ash', 'White Ash', 'Red Oak', 'Natural Oak', 'Walnut')),
    ProductStandardPrice            DECIMAL(6,2),
    ProductLineID                   INTEGER,
CONSTRAINT Product_PK PRIMARY KEY (ProductID));

CREATE TABLE OrderLine_T
    (OrderID                        NUMBER(11,0)        NOT NULL,
    ProductID                       INTEGER              NOT NULL,
    OrderedQuantity                 NUMBER(11,0),
CONSTRAINT OrderLine_PK PRIMARY KEY (OrderID, ProductID),
CONSTRAINT OrderLine_FK1 FOREIGN KEY (OrderID) REFERENCES Order_T(OrderID),
CONSTRAINT OrderLine_FK2 FOREIGN KEY (ProductID) REFERENCES Product_T(ProductID));