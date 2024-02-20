import modal as md

database_name = "asd"

##########################################
# CREATE A TABLE NAME PRODUCTS
table_name = "products"
table_columns = {
    "product_name" : "TEXT",
    "product_unit_quantity" : "REAL",
    "product_unit" : "TEXT",
    "product_unit_price" : "REAL",
    "location" : "TEXT",
    "date" : "TEXT",
    "product_picture" : "TEXT"
}

md.Database(database_name,table_name).createTable(table_columns)

##########################################
# CREATE A TABLE NAME PRODUCTS LIST
table_name = "product_list"
table_columns = {
    "product_name" : "TEXT",
}

md.Database(database_name,table_name).createTable(table_columns)

##########################################