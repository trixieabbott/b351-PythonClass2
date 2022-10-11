CREATE TABLE Customer_T
    (CustomerID         NUMBER(11,0)       NOT NULL,
    CustomerName        VARCHAR2(25)         NOT NULL,
    CustomerAddress     VARCHAR2(30),
    CustomerCity        CHAR(2),
    CustomerPostalCode  VARCHAR2(9),
CONSTRAINT Customer_PK PRIMARY KEY (CustomerID));

CREATE TABLE ORDER_T
    (OrderID            NUMBER(11,0)       NOT NULL,
    OrderDate           DATE DEFAULT SYSDATE,
    CustomerID          NUMBER(11,0),
CONSTRAINT Order_PK PRIMARY KEY(OrderID),
CONSTRAINT Order_FK FOREIGN KEY(CustomerID) REFERENCES Customer_T(CustomerID));

CREATE TABLE Product_T
    (ProductID          NUMBER(11,0)        NOT NULL,
    ProductDescription  VARCHAR2(50),
    ProductFinish       VARCHAR2(50).,
    )