import models
from cls.sql_composer import SqlComposer
from cls.sqlite_client import Liter


if __name__ == '__main__':
    cls = Liter("test")

    for model in models.get_list_of_all_models():
        sqler = SqlComposer(model)
        cls.exec_sql(sqler.sql_create_table)
        data = sqler.generate_sample_data()
        cls.exec_sql(sqler.get_sql_insert_table(), data)
        res = cls.exec_sql(sqler.sql_select())
        print(res)

    cls.commit()
    cls.close()
