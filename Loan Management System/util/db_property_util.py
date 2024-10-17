class DBPropertyUtil:
    @staticmethod
    def get_db_conn_str():
        return ('Driver={ODBC Driver 17 for SQL Server};'
                'Server=DESKTOP-RJ2AKHB\\SQLEXPRESS;'
                'Database=;'
                'Trusted_Connection=yes;')
            
