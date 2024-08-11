Inventory Management System 🛠️📦
This project is a technical test that utilizes Tkinter for the front-end and CSV files as the database backend in Python. The system is designed to manage inventory items by allowing users to perform Create, Read, Update, and Delete (CRUD) operations on inventory data.

Features 🌟
SKU Validation: Upon entering the SKU, the system will validate whether it exists in the database.

If the SKU does not exist:
Add New Item: The user can input details such as Article, Brand, Model, Department, Class, Family, Quantity, and Stock. Other fields will either be hidden or disabled. ✍️
If the SKU exists:
Delete: The system will display a delete button, which will prompt for confirmation before deletion. 🗑️
Update: The system will allow updating of fields such as Article, Brand, Model, Department, Class, Family, Quantity, Stock, and Discontinued status. 🔄
View Details: The system will display details such as Article, Brand, Model, Department, Class, Family, Date Added, Stock, Quantity, Discontinued status, and Date Removed. 📋
Hierarchical Data Management:

Separate tables for Departments, Classes, and Families, each with corresponding data. 🗂️
Selection of Class and Family is dependent on the Department and Class selection, respectively. 📊
Business Rules:

Quantity cannot exceed Stock. ⚠️
Department is filled automatically upon entering a valid SKU. 🏢
Class selection is only possible if a Department is selected, and it only shows classes belonging to that department. 📚
Family selection is only possible if a Class is selected, and it only shows families belonging to that Department-Class combination. 🏷️
Date Removed is automatically updated to the current date when the Discontinued status is turned on. 📅
Stored Procedures:

All CRUD operations are executed through stored procedures. 🔄
All database objects are stored in a file for individual or collective review. 📂