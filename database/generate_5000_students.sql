-- Scalability test script
-- Generates 5,000 unique student records.
-- Run this only in a test database, not the demo database.

;WITH Numbers AS
(
    SELECT TOP (5000)
        ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) AS n
    FROM sys.all_objects a
    CROSS JOIN sys.all_objects b
)
INSERT INTO Students
(
    StudentID,
    Name,
    Course,
    TotalFee,
    PaidAmount,
    DueDate
)
SELECT
    'TEST' + RIGHT('00000' + CAST(n AS VARCHAR(5)), 5),
    'Test Student ' + CAST(n AS VARCHAR(5)),
    CASE
        WHEN n % 3 = 0 THEN 'CSE'
        WHEN n % 3 = 1 THEN 'AIML'
        ELSE 'ISE'
    END,
    100000.00,
    50000.00,
    DATEADD(DAY, 30, CAST(GETDATE() AS DATE))
FROM Numbers
WHERE NOT EXISTS
(
    SELECT 1
    FROM Students s
    WHERE s.StudentID = 'TEST' + RIGHT('00000' + CAST(n AS VARCHAR(5)), 5)
);

-- Verify the number of test records
SELECT COUNT(*) AS TestStudentCount
FROM Students
WHERE StudentID LIKE 'TEST%';