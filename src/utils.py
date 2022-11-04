import os



def dict_to_string(d):
    fin_row = ''
    for el in d:
        fin_row += ";".join(
            map(
                lambda v: f"{v[0]}: {v[1]}", 
                el._asdict().items()
            )
        ) + "\n"
    return fin_row


def get_query(request_type):
    with open(os.path.join("sql_scripts",  request_type + ".sql"), "r") as f:
        query =  f.read()
    return query
