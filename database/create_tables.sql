-- Fee Management System
-- Database Table Creation Script

CREATE TABLE Students (
    StudentID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Course VARCHAR(100) NOT NULL,
    TotalFee DECIMAL(10,2) NOT NULL,
    PaidAmount DECIMAL(10,2) NOT NULL DEFAULT 0,
    DueDate DATE NOT NULL
);

CREATE TABLE Administrators (
    AdminID VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Role VARCHAR(50) NOT NULL
);