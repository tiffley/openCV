from functools import cached_property
import random
from datetime import datetime, timedelta

# generate SQL with dataclass
class SqlComposer:
    def __init__(self, model_cls):
        self.model_cls = model_cls
        self.table_name = model_cls.__name__

    @cached_property
    def di_cols(self) -> dict:
        """
        :return: {col_name: {py_type:xxx, db_type:xxx}}
        {'organization_id': <class 'int'>, 'organization_name': <class 'str'>, ...}
        """
        output = {}
        for col_name, py_data_type in self.model_cls.__annotations__.items():
            db_type = self._convert_data_type(py_data_type)
            output[col_name] = {"py_type":py_data_type, "db_type":db_type}
        return output

    @cached_property
    def li_col_names(self) -> list:
        cols = []
        for col, di in self.di_cols.items():
            cols.append(col)
        return cols

    def _convert_data_type(self, d_type):
        if d_type == int:
            return "INTEGER"
        if d_type == str:
            return "VARCHAR"
        if d_type == datetime:
            return "DATETIME"

    def _li_to_str(self, li):
        return ', '.join(li)

    @cached_property
    def sql_create_table(self):
        cols = []
        for col, di in self.di_cols.items():
            cols.append(f"{col} {di.get('db_type')}")
        return f"CREATE TABLE IF NOT EXISTS {self.table_name} ({self._li_to_str(cols)})"

    def get_sql_insert_table(self):
        """
        usage
        cls.exec_sql(model.get_sql_insert_table(), ('john', 'john@example.com'))
        :return: INSERT INTO xxx (cols) VALUES (?,?,?,...)
        """
        # assume insert data to all cols
        vals = ["?"]*len(self.li_col_names)
        return f"INSERT INTO {self.table_name} ({self._li_to_str(self.li_col_names)}) VALUES ({self._li_to_str(vals)})"

    def sql_select(self):
        return f"SELECT * FROM {self.table_name}"

    def generate_sample_data(self) -> tuple:
        li = []
        for col, di in self.di_cols.items():
            if di.get('py_type') == int:
                li.append(random.randint(1, 100))
            if di.get('py_type') == str:
                li.append(f"random_{random.randint(1, 100)}")
            if di.get('py_type') == datetime:
                current_datetime = datetime.now()
                one_year_ago = current_datetime - timedelta(days=365)
                created_at = random.uniform(one_year_ago.timestamp(), current_datetime.timestamp())
                li.append(datetime.utcfromtimestamp(created_at))
        return tuple(li)

