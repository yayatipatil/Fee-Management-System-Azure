-- Fee Management System
-- Sample Administrator Data

INSERT INTO Administrators (AdminID, Name, Role)
VALUES
('A001', 'Sidhant', 'FeeManager'),
('A002', 'Stuti', 'Administrator');


-- Sample Student Data

INSERT INTO Students
(StudentID, Name, Course, TotalFee, PaidAmount, DueDate)
VALUES
('S001', 'Rahul Sharma', 'CSE', 100000, 100000, '2026-10-01'),
('S002', 'Priya Patil', 'AIML', 100000, 60000, '2026-10-15'),
('S003', 'Amit Kumar', 'ECE', 90000, 0, '2026-09-01'),
('S004', 'Sneha Joshi', 'CSE', 100000, 75000, '2026-11-01'),
('S005', 'Rohan Desai', 'ISE', 95000, 95000, '2026-10-20'),
('S006', 'Ananya Rao', 'AIML', 110000, 50000, '2026-09-15'),
('S007', 'Karan Kulkarni', 'CSE', 100000, 0, '2026-08-15'),
('S008', 'Neha Shah', 'ECE', 90000, 90000, '2026-10-10'),
('S009', 'Vivek Patil', 'ISE', 95000, 40000, '2026-09-20'),
('S010', 'Pooja Naik', 'CSE', 100000, 100000, '2026-11-15'),
('S011', 'Arjun Rao', 'AIML', 110000, 70000, '2026-10-05'),
('S012', 'Kavya Shetty', 'ECE', 90000, 0, '2026-08-01'),
('S013', 'Aditya More', 'CSE', 100000, 85000, '2026-11-10'),
('S014', 'Isha Kulkarni', 'ISE', 95000, 95000, '2026-10-25'),
('S015', 'Manoj Patil', 'AIML', 110000, 30000, '2026-09-10'),
('S016', 'Aishwarya Rao', 'CSE', 100000, 100000, '2026-12-01'),
('S017', 'Nikhil Desai', 'ECE', 90000, 20000, '2026-08-20'),
('S018', 'Meera Joshi', 'ISE', 95000, 60000, '2026-10-30'),
('S019', 'Siddharth Shah', 'CSE', 100000, 0, '2026-09-05'),
('S020', 'Divya Naik', 'AIML', 110000, 110000, '2026-11-20');