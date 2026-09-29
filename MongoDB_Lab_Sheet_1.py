// ============================================================
// PYTHON LIBRARIES AND APPLICATIONS
// MONGODB LAB SHEET 1
// Course: BCA
// Topic: MongoDB Database, Collections and CRUD Operations
// Tool: MongoDB Shell (mongosh)
// ============================================================


// ============================================================
// Q1. Create a new MongoDB database named StudentDB and verify
//     its successful creation using MongoDB Shell.
// ============================================================

use StudentDB

// Insert a sample document so that StudentDB is actually created.
db.Students.insertOne({
    RollNo: 101,
    Name: "Amit",
    Department: "BCA",
    Semester: 5,
    CGPA: 8.2
})

// Verify the current database.
db.getName()

// Display available databases.
show dbs


// ============================================================
// Q2. Create collections Students, Faculty and Courses.
// ============================================================

db.createCollection("Students")
db.createCollection("Faculty")
db.createCollection("Courses")

// Verify collections.
show collections


// ============================================================
// Q3. Insert a single document into Students.
// ============================================================

db.Students.insertOne({
    RollNo: 102,
    Name: "Neha",
    Department: "BCA",
    Semester: 5,
    CGPA: 8.7
})


// ============================================================
// Q4. Insert multiple student documents.
// ============================================================

db.Students.insertMany([
    {
        RollNo: 103,
        Name: "Rahul",
        Department: "MCA",
        Semester: 3,
        CGPA: 7.8
    },
    {
        RollNo: 104,
        Name: "Priya",
        Department: "BCA",
        Semester: 5,
        CGPA: 9.1
    },
    {
        RollNo: 105,
        Name: "Rohan",
        Department: "MCA",
        Semester: 3,
        CGPA: 8.5
    },
    {
        RollNo: 106,
        Name: "Kavya",
        Department: "BCA",
        Semester: 5,
        CGPA: 8.9
    },
    {
        RollNo: 107,
        Name: "Arjun",
        Department: "BCA",
        Semester: 5,
        CGPA: 7.6
    }
])


// ============================================================
// Q5. Retrieve all documents from Students.
// ============================================================

db.Students.find()


// ============================================================
// Q6. Retrieve a specific student using Roll Number.
// ============================================================

db.Students.findOne({
    RollNo: 104
})


// ============================================================
// Q7. Retrieve students based on Department.
// ============================================================

db.Students.find({
    Department: "BCA"
})


// ============================================================
// Q8. Display only Name and Department using projection.
//     _id: 0 hides the MongoDB generated ID.
// ============================================================

db.Students.find(
    {},
    {
        _id: 0,
        Name: 1,
        Department: 1
    }
)


// ============================================================
// Q9. Update the department of a specific student.
// ============================================================

db.Students.updateOne(
    { RollNo: 107 },
    { $set: { Department: "MCA" } }
)

// Verify the update.
db.Students.findOne({ RollNo: 107 })


// ============================================================
// Q10. Modify the semester of all students belonging to BCA.
// ============================================================

db.Students.updateMany(
    { Department: "BCA" },
    { $set: { Semester: 6 } }
)

// Verify the update.
db.Students.find({ Department: "BCA" })


// ============================================================
// Q11. Replace an existing student document using replaceOne().
// ============================================================

db.Students.replaceOne(
    { RollNo: 103 },
    {
        RollNo: 103,
        Name: "Rahul Kumar",
        Department: "MCA",
        Semester: 4,
        CGPA: 8.1
    }
)

// Verify replacement.
db.Students.findOne({ RollNo: 103 })


// ============================================================
// Q12. Add Email field to all documents in Students.
// ============================================================

// This adds the same sample email domain/pattern to every document.
// MongoDB update pipeline is used to generate an email from Name.
db.Students.updateMany(
    {},
    [
        {
            $set: {
                Email: {
                    $concat: [
                        { $toLower: "$Name" },
                        "@student.com"
                    ]
                }
            }
        }
    ]
)

// Verify Email field.
db.Students.find(
    {},
    {
        _id: 0,
        RollNo: 1,
        Name: 1,
        Email: 1
    }
)


// ============================================================
// Q13. Remove an existing field from all documents.
//     Here, Email is removed from all student documents.
// ============================================================

db.Students.updateMany(
    {},
    {
        $unset: {
            Email: ""
        }
    }
)

// Verify that Email has been removed.
db.Students.find()


// ============================================================
// Q14. Delete a specific student using deleteOne().
// ============================================================

db.Students.deleteOne({
    RollNo: 107
})

// Verify deletion.
db.Students.findOne({ RollNo: 107 })


// ============================================================
// Q15. Delete multiple records satisfying a condition.
//     Example: delete students with CGPA below 8.0.
// ============================================================

db.Students.deleteMany({
    CGPA: { $lt: 8.0 }
})

// Verify remaining documents.
db.Students.find()


// ============================================================
// Q16. Count total documents in Students.
// ============================================================

db.Students.countDocuments()


// ============================================================
// Q17. Rename Students collection to StudentDetails.
// ============================================================

db.Students.renameCollection("StudentDetails")

// Verify collection name.
show collections


// ============================================================
// Q18. Create Departments collection and insert sample data.
// ============================================================

db.createCollection("Departments")

db.Departments.insertMany([
    {
        DepartmentCode: "BCA",
        DepartmentName: "Bachelor of Computer Applications",
        HOD: "Dr. Sharma"
    },
    {
        DepartmentCode: "MCA",
        DepartmentName: "Master of Computer Applications",
        HOD: "Dr. Verma"
    },
    {
        DepartmentCode: "BBA",
        DepartmentName: "Bachelor of Business Administration",
        HOD: "Dr. Singh"
    }
])

// Display departmental information.
db.Departments.find()


// ============================================================
// Q19. Drop Departments collection and verify deletion.
// ============================================================

db.Departments.drop()

// Verify collections.
show collections


// ============================================================
// Q20. Drop StudentDB database and confirm removal.
// ============================================================

use StudentDB

// Drop the complete database.
db.dropDatabase()

// Verify database removal.
show dbs


// ============================================================
// Q21. Recreate StudentDB and insert sample data after deletion.
// ============================================================

use StudentDB

// Creating a collection and inserting data recreates the database.
db.Students.insertMany([
    {
        RollNo: 201,
        Name: "Anjali",
        Department: "BCA",
        Semester: 5,
        CGPA: 8.6
    },
    {
        RollNo: 202,
        Name: "Vikas",
        Department: "MCA",
        Semester: 3,
        CGPA: 8.3
    },
    {
        RollNo: 203,
        Name: "Pooja",
        Department: "BCA",
        Semester: 5,
        CGPA: 9.0
    }
])

// Verify recreated database and data.
db.getName()
show collections
db.Students.find()


// ============================================================
// Q22. Perform CRUD operations using MongoDB Compass and
//     compare results with MongoDB Shell.
// ============================================================
//
// MongoDB Compass steps:
// 1. Open MongoDB Compass.
// 2. Connect to the same MongoDB server.
// 3. Open StudentDB.
// 4. Open Students collection.
//
// CREATE:
// Add a document using the "Add Data" option.
//
// READ:
// Open the Students collection and view all documents.
//
// UPDATE:
// Open a document, edit a field, and click Update.
//
// DELETE:
// Select a document and use Delete.
//
// The same operations can be performed in Shell using:
//
// db.Students.insertOne({...})
// db.Students.find()
// db.Students.updateOne({...}, {$set: {...}})
// db.Students.deleteOne({...})
//
// Observation:
// Compass provides a graphical interface, while mongosh
// performs the same operations through commands.


// ============================================================
// Q23. Demonstrate MongoDB Shell and MongoDB Compass for
//     managing databases and collections.
// ============================================================
//
// MongoDB Shell examples:
//
// use StudentDB
// show dbs
// show collections
// db.createCollection("Courses")
// db.Courses.find()
//
// MongoDB Compass:
//
// 1. Connect to MongoDB server.
// 2. Select StudentDB.
// 3. Use "Create Collection" to create a collection.
// 4. Open the collection to insert/view/update/delete data.
// 5. Use the database and collection interface to manage data.
//
// Observation:
// Both tools operate on the same MongoDB server and database.
// The main difference is the user interface.


// ============================================================
// Q24. Compare MongoDB CRUD operations with equivalent SQL.
// ============================================================
//
// MongoDB CREATE:
// db.Students.insertOne({
//     RollNo: 204,
//     Name: "Riya",
//     Department: "BCA"
// })
//
// SQL equivalent:
// INSERT INTO Students (RollNo, Name, Department)
// VALUES (204, 'Riya', 'BCA');
//
// ------------------------------------------------------------
//
// MongoDB READ:
// db.Students.find({ Department: "BCA" })
//
// SQL equivalent:
// SELECT * FROM Students
// WHERE Department = 'BCA';
//
// ------------------------------------------------------------
//
// MongoDB UPDATE:
// db.Students.updateOne(
//     { RollNo: 204 },
//     { $set: { CGPA: 8.8 } }
// )
//
// SQL equivalent:
// UPDATE Students
// SET CGPA = 8.8
// WHERE RollNo = 204;
//
// ------------------------------------------------------------
//
// MongoDB DELETE:
// db.Students.deleteOne({ RollNo: 204 })
//
// SQL equivalent:
// DELETE FROM Students
// WHERE RollNo = 204;
//
// ------------------------------------------------------------
//
// Main differences:
//
// MongoDB:
// - NoSQL document-oriented database.
// - Data is stored as BSON documents.
// - Uses collections instead of tables.
// - Uses documents instead of rows.
// - Uses fields instead of columns.
// - Flexible schema.
//
// SQL:
// - Relational database.
// - Data is stored in tables.
// - Uses rows and columns.
// - Generally uses a predefined schema.
// - Uses SQL commands for data manipulation.


// ============================================================
// Q25. Laboratory Report
// ============================================================
//
// OBJECTIVE:
// To understand MongoDB database creation, collection creation,
// document insertion, retrieval, updating, deletion, counting,
// renaming, dropping databases/collections, and CRUD operations
// using MongoDB Shell and MongoDB Compass.
//
// ------------------------------------------------------------
//
// COMMANDS EXECUTED:
// 1. Database creation using use StudentDB.
// 2. Collection creation using createCollection().
// 3. Single document insertion using insertOne().
// 4. Multiple document insertion using insertMany().
// 5. Data retrieval using find() and findOne().
// 6. Filtering using query conditions.
// 7. Field projection using find().
// 8. Updating using updateOne().
// 9. Updating multiple documents using updateMany().
// 10. Complete document replacement using replaceOne().
// 11. Adding fields using $set.
// 12. Removing fields using $unset.
// 13. Deleting one document using deleteOne().
// 14. Deleting multiple documents using deleteMany().
// 15. Counting documents using countDocuments().
// 16. Renaming collections using renameCollection().
// 17. Dropping collections using drop().
// 18. Dropping databases using dropDatabase().
//
// ------------------------------------------------------------
//
// OUTPUT / OBSERVATION:
// The StudentDB database was created successfully.
// Students, Faculty and Courses collections were created.
// Student documents were inserted and retrieved successfully.
// Filtering and projection returned the required records.
// Update and replacement operations modified documents correctly.
// Delete operations removed the specified documents.
// The number of documents was obtained using countDocuments().
// The Students collection was renamed to StudentDetails.
// The Departments collection was created and later dropped.
// StudentDB was dropped and subsequently recreated with sample data.
// CRUD operations were also demonstrated using MongoDB Compass.
//
// ------------------------------------------------------------
//
// SCREENSHOTS TO ADD TO THE LAB REPORT:
// 1. MongoDB Shell showing StudentDB.
// 2. show collections output.
// 3. insertOne() output.
// 4. insertMany() output.
// 5. find() output.
// 6. Filtering by Department.
// 7. Projection output.
// 8. updateOne() output.
// 9. updateMany() output.
// 10. replaceOne() output.
// 11. deleteOne() and deleteMany() output.
// 12. countDocuments() output.
// 13. Renamed StudentDetails collection.
// 14. Departments collection.
// 15. MongoDB Compass database/collection view.
// 16. CRUD operation in Compass.
// 17. Dropped database verification.
// 18. Recreated StudentDB with sample data.
//
// ------------------------------------------------------------
//
// CONCLUSION:
// The experiment successfully demonstrated the basic operations
// of MongoDB using MongoDB Shell and MongoDB Compass. Database
// and collection management, document insertion, retrieval,
// updating, replacement, deletion, counting and renaming were
// performed successfully. The experiment also showed the
// difference between MongoDB's document-oriented approach and
// traditional SQL-based relational database operations.
//
// ============================================================
// END OF MONGODB LAB SHEET 1
// ============================================================
