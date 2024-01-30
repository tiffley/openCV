import models
from cls.sql_composer import SqlComposer
from cls.sqlite_client import Liter


di = {
    models.ORGANIZATION_DATA: [(1, "A", 1), (2, "B", 1), (3, "C", 1), (4, "D", 1)],
    models.EMPLOYEE_DATA: [(1, 1, "Taka", 1), (2, 1, "Vicky", 1), (3, 2, "Ai", 1), (4, 3, "Will", 1)],
    models.SURVEY_MASTER: [(1, "1on1", 1), (2, "feedback", 1), (3, "etc", 1)],
    models.SURVEY_RESPONSE_META_DATA: [(1, 1, 1, 9), (2, 1, 2, 9), (3, 1, 3, 9), (4, 1, 4, 9)],
    models.SURVEY_DATA: [(1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1)]
}

cls = Liter("test")

def run(model, li_data):
    sql = SqlComposer(model)
    cls.exec_sql(sql.sql_create_table)
    for data in li_data:
        cls.exec_sql(sql.get_sql_insert_table(), data)
    res = cls.exec_sql(sql.sql_select())
    print(res)

if __name__ == '__main__':
    for model, data in di.items():
        run(model, data)
    cls.commit()
    cls.close()


exit()

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
