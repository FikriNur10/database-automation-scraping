📄 DATABASE TABLE MAPPER - README
🧠 DESCRIPTION
-----------------------------------------------
This Python script automatically maps database table names to their respective database Excel files.

Given:
- A main Excel file (`db_recap.xlsx`) that lists all table names.
- A folder (`table_db_export`) containing exported Excel files, each representing a database with a list of tables.

The script will:
✅ Match each table in `db_recap.xlsx` to its corresponding database.
✅ Add a new column "Database" to `db_recap.xlsx` with the correct database name.
✅ Save the result into a new file: `db_recap_updated.xlsx`.

📁 FOLDER STRUCTURE
-----------------------------------------------
project-folder/
├── db_recap.xlsx               <- Main file containing a list of tables
├── table_db_export/           <- Folder with exported Excel files (named as databases)
│   ├── db1.xlsx
│   ├── db2.xlsx
│   └── ...
├── db_recap_updated.xlsx      <- Output file (generated)
└── map_tables.py              <- Python script

⚙️ REQUIREMENTS
-----------------------------------------------
- Python 3.x
- pandas
- openpyxl (recommended for Excel support)

You can install the requirements with:
> pip install pandas openpyxl

🚀 HOW TO USE
-----------------------------------------------
1. Place your `db_recap.xlsx` in the root project folder.
2. Ensure it contains a column named **"Table"**.
3. Place all database export files (Excel format) inside the `table_db_export/` folder.
   Each file should have a column named **"Name"** listing table names.
4. Run the script:
> python map_tables.py

5. Check the output file: `db_recap_updated.xlsx`

📌 NOTES
-----------------------------------------------
- Table name matching is **case-insensitive**.
- Files without the required columns will be skipped.
- Tables that are not found in any database will be left blank in the "Database" column.

🛠️ AUTHOR
-----------------------------------------------
Created by: Fikri Nur Diega  
GitHub: https://github.com/FikriNur10  
Portfolio: https://fikrinurdiega.vercel.app

