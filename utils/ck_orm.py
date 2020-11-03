from clickhouse_driver import connect, Client
from utils.config_loader import Config


class Connection(Config):

    def __init__(self):
        super(Config, self).__init__() # 暂时没啥用，仅规范代码调用
        self.connection = None

    def initial(self):
        self.load_config(config_file='db.ini')

    def get_connection(self, new_connect=False):
        if not new_connect:
            if self.connection and not self.connection.is_closed:
                return self.connection
            else:
                self.connection = connect(
                    host=self.CONFIG.CK.host,
                    password=self.CONFIG.CK.password,
                    database=self.CONFIG.CK.database,
                    user=self.CONFIG.CK.user
                )
                return self.connection
        else:
            return connect(
                host=self.CONFIG.CK.host,
                password=self.CONFIG.CK.password,
                database=self.CONFIG.CK.database,
                user=self.CONFIG.CK.user
            )

    def execute(self, sql='', params=[], new_connect=False):
        conn = self.get_connection() if not new_connect else self.get_connection(new_connect=True)
        assert isinstance(params, list) or isinstance(params, dict)
        with conn.cursor() as cursor:
            cursor.execute(sql, params)
            result = cursor.fetchall()




if __name__ == '__main__':
    instance = Connection()
    instance.initial()