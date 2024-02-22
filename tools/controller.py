from tools import modal

database_name = "deneme1"
database = modal.Database(database_name)

############################################################################
# CREATE A TABLE NAME PRODUCTS
table_name = "products_table"

table_columns = {
    "product_name": "TEXT",
    "product_unit_quantity": "REAL",
    "product_unit": "TEXT",
    "product_unit_price": "REAL",
    "product_location": "TEXT",
    "product_unit_price_date": "TEXT",
    "product_picture": "TEXT"
}

database.createTable(table_name, table_columns)
products_table = database.getTable(table_name)

############################################################################
# CREATE A TABLE NAME PRODUCTS LIST
table_name = "product_name_table"

table_columns = {
    "product_name": "TEXT"
}

database.createTable(table_name, table_columns)
products_name_table = database.getTable(table_name)

############################################################################
# CREATE A TABLE NAME UNITS LIST
table_name = "product_unit_table"

table_columns = {
    "product_unit": "TEXT"
}

datas = [
    ["kg"],
    ["g"],
    ["adet"]
]

database.createTable(table_name, table_columns)
database.insertTable(table_name, datas)
products_unit_table = database.getTable(table_name)

############################################################################
# NOTES:
#
#     # CREATE DATABASE AND TABLE
#     # Define database name without extention and create database object
#         database_name = "sample"
#         database = md.Database(database_name)
#
#     # Create table like as sample
#         table_name = "sample_table"
#         table_columns = {
#             "sample1": "TEXT",
#             "sample2": "REAL",
#             "sample3": "TEXT"
#         }
#         database.createTable(table_name, table_columns)
#
#     # DEFINE DATABASE VALUES
#
#     # Define datas like matris as sample for one column tables
#         table_name = "sample_table"
#         datas = [
#             ("value1",),
#             ("value2",),
#             ("value3",)
#             ]
#         database.insertTable(table_name, datas)
#
#     # Define datas like matris as sample for two or more columns tables
#         table_name = "sample_table"
#         datas = [
#             ("value1 1/2", "value1 2/2"),
#             ("value2 1/2", "value2 2/2"),
#             ("value3 1/2", "value3 2/2")
#         ]
#         database.insertTable(table_name, datas)
#
#
#
#
#
############################################################################
