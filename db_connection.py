from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.creat_connection()

    def creat_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('DBFile/dbortocalc.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, 'Not connected to DB', 'Click Cancel to exit',
                                           QtWidgets.QMessageBox.Cancel)

            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS Patients "
                   "(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,"
                   "Name VARCHAR(50) NOT NULL,"
                   "Date TEXT,"
                   "Info1 TEXT,"
                   "Info2 TEXT)")
        return True

    def execute_query_with_params(self, sql_query, query_values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if query_values is not None:
            for query_value in query_values:
                query.addBindValue(query_value)
        query.exec()
        return query

    def filter_pat(self, f_name, date):
        sql_query = f"SELECT * FROM Patients WHERE name = '{f_name}' AND Date = '{date}'"
        return self.execute_query_with_params(sql_query).first()

    def add_new_patient(self, name, date, info1, info2):
        sql_query = "INSERT INTO Patients (Name, Date, Info1,Info2) VALUES (?, ?, ?, ?)"
        self.execute_query_with_params(sql_query, [name, date, info1, info2])
        # print(name,date,info1,info2)

    def add_box_pat(self):
        sql_query = f"SELECT Name, Date FROM Patients"
        data = self.execute_query_with_params(sql_query)
        lst=[]
        data.first()
        while data.isValid():
            lst.append(f"{data.value('Name')} ({data.value('Date')})")
            data.next()
        return sorted(lst)
