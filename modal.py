import sqlite3


class Database:

    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name

    def createTable(self, table_columns):
        """
        Create a table

        Args:
        database_name (str) : Name of the database - not include extensions
        table_name (str) : Name of the table
        table_columns (dict) : For column of table - dict must have column name in keys, data type in values

        Returns:
        It only created a table in the database
        """

        conn = sqlite3.connect(f"{self.database_name}.sqlite3")
        c = conn.cursor()
        values = ""
        for k, v in table_columns.items():
            values += f"{k} {v}, "
        values = values[:-2]
        print(values)
        sql_command = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({values})"
        c.execute(sql_command)
        conn.commit()


def insertTable(database_name, table_name, *datas):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    mock_values = ["?"] * len(datas)
    mock_values = ",".join(mock_values)
    sql_command = f"INSERT INTO {table_name} VALUES ({mock_values})"
    c.execute(sql_command, datas)
    conn.commit()


def getTable(database_name, table_name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    sql_command = f"SELECT * FROM {table_name}"
    c.execute(sql_command)
    return c.fetchall()


def getTableWithColumns(database_name, table_name, *columns):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    columns = ",".join(columns)
    sql_command = f"SELECT {columns} FROM {table_name}"
    c.execute(sql_command)
    return c.fetchall()


def getTableWithColumnRow(database_name, table_name, price_column_name, product_name_column, row_value):
    tp = (row_value,)
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    sql_command = f"SELECT {price_column_name} FROM {table_name} WHERE {product_name_column}=?"
    c.execute(sql_command, tp)
    price = c.fetchone()
    return price[0]


class Modificators:

    def __init__(self, input):
        self.input = input

    def correctionForLocation(self):
        input = self.input.replace("°", ".").replace("′", "").replace("″", "").split(" ")
        location = (float(input[0]), float(input[3]))
        return location

    def changerForTurkishLetter(self):
        return (self.input.lower().replace(" ", "").replace('ğ', 'g')
                .replace('ü', 'u').replace('ş', 's').replace('ı', 'i')
                .replace('ö', 'o').replace('ç', 'c'))
