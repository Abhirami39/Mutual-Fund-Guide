import mysql.connector
from datetime import datetime
import itertools


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ButterFree10!@#",
    database="mfguide"
)


def database_insertion(all_mfs_info, database_all_mf_info):
    zip_object = zip(all_mfs_info, database_all_mf_info)
    for mf, db_insert_info in zip_object:
        print(mf)
        print(db_insert_info[0])
        print(db_insert_info[1])

        id_category = 0
        id_mutual_fund = 0

        mycursor = mydb.cursor(buffered=True)

        # checking if the category exists
        check_if_exists_cat = "SELECT name FROM category where name = %s"
        vals_to_match_cat = [db_insert_info[1]]
        mycursor.execute(check_if_exists_cat, vals_to_match_cat)
        if_exists = mycursor.fetchall()
        if not if_exists:
            insert_category = "INSERT INTO category (name) VALUES (%s)"
            mycursor.execute(insert_category, vals_to_match_cat)
            mydb.commit()
            print("inserted category")

            # getting the id
            check_if_exists_cat_id = "SELECT id FROM category where name = %s"
            vals_to_match_cat_id = [db_insert_info[1]]
            mycursor.execute(check_if_exists_cat_id, vals_to_match_cat_id)

            id_category = mycursor.fetchall()[0]
        else:
            # getting the id
            check_if_exists_cat_id = "SELECT id FROM category where name = %s"
            vals_to_match_cat_id = [db_insert_info[1]]
            mycursor.execute(check_if_exists_cat_id, vals_to_match_cat_id)

            id_category = mycursor.fetchall()[0]
            print(id_category)
        print(id_category)
        print(id_category[0])
        print(type(id_category[0]))

        # mycursor.execute("SELECT id FROM category")
        # id_category = mycursor.fetchone()
        # print("category id ", id_category[0])

        # cheking if the mutual fund exists
        check_if_exists_mf_name = "SELECT name FROM mutual_fund where name = %s"
        vals_to_match_mf_name = [db_insert_info[0]]
        mycursor.execute(check_if_exists_mf_name, vals_to_match_mf_name)
        if_exists = mycursor.fetchall()
        if not if_exists:
            insert_category = "INSERT INTO mutual_fund (name, category_id) VALUES (%s, %s)"
            # insert_vals = (db_insert_info[0], id_category)
            # insert_vals_list = list(insert_vals)
            mycursor.execute(insert_category, (str(db_insert_info[0]), id_category[0]))  # insert_vals_list)
            mydb.commit()
            print("inserted mutual fund")

            # getting the id
            check_if_exists_mf_name_id = "SELECT id FROM mutual_fund where name = %s"
            vals_to_match_mf_name_id = [db_insert_info[0]]
            mycursor.execute(check_if_exists_mf_name_id, vals_to_match_mf_name_id)
            id_mutual_fund = mycursor.fetchall()[0]
        else:
            print(if_exists)
            check_if_exists_mf_name_id = "SELECT id FROM mutual_fund where name = %s"
            vals_to_match_mf_name_id = [db_insert_info[0]]
            mycursor.execute(check_if_exists_mf_name_id, vals_to_match_mf_name_id)
            id_mutual_fund = mycursor.fetchall()[0]

        # mycursor.execute("SELECT id FROM mutual_fund")
        # id_mutual_fund = mycursor.fetchone()
        # print("mutual_fund id ", id_mutual_fund[0])
        # print(type(id_mutual_fund[0]))

        mycursor.execute("SELECT id FROM data_provider")
        id_data_provider = mycursor.fetchone()
        print("data_provider id ", id_data_provider[0])

        # using now() to get current time
        current_time = datetime.now()

        print("Time now is : ", end="")
        print(current_time)

        mySql_insert_query = """INSERT INTO mfdata (mutual_fund_id, data_provider_id, asof_date, rating, inception_date,
        annualized_returns_1yr, annualized_returns_2yr, annualized_returns_3yr, annualized_returns_5yr,
        annualized_returns_since_inception, expense_ratio, aum, std_deviation, std_deviation_cat_avg, beta, beta_cat_avg,
        alpha, alpha_cat_avg, sharpe_ratio, sharpe_ratio_cat_avg, treynor_ratio, treynor_ratio_cat_avg, risk_o_meter)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s)"""

        # mySql_insert_query = """("INSERT INTO mfdata" "(mutual_fund_id, data_provider_id, asof_date,)"
        # "VALUES (%d, %d, %s)")"""

        # mySql_insert_query = "INSERT INTO mfdata (mutual_fund_id, data_provider_id,asof_date) values(%s, %s, %s)"
        #
        # record = [id_mutual_fund[0], id_data_provider[0], current_time]
        record = []
        record.extend([id_mutual_fund[0], id_data_provider[0], current_time])
        record.extend(mf)

        # print(*record, sep="\n")
        # ls = [type(item) for item in record]
        # print(ls)

        mycursor.execute(mySql_insert_query, record)
        mydb.commit()
        print("Record inserted successfully into Laptop table")


def get_mf_substr_db(sub_str):
    mycursor = mydb.cursor(buffered=True)

    # test_substr = "DSP"

    mycursor.execute("SELECT * FROM mutual_fund WHERE name LIKE %s", ("%" + sub_str + "%",))
    data = mycursor.fetchall()

    i = 0
    mf_names = []
    mf_name_id = []
    for vals in data:
        name = data[i]
        # print(name[1])
        mf_names.append(name[1])
        mf_name_id.append(name[0])
        i += 1

    # print(mf_names)
    # print(mf_name_id)
    return mf_names

def get_all_mf_name():
    mycursor = mydb.cursor(buffered=True)

    mycursor.execute("SELECT name FROM mutual_fund")

    all_mf_names = mycursor.fetchall()
    all_mf_names_single_list = list(itertools.chain.from_iterable(all_mf_names))

    print(all_mf_names_single_list)

    return all_mf_names_single_list

def get_mf_params(mf_name_key):
    mycursor = mydb.cursor(buffered=True)

    # ok so take the name, get the id from the mutual_fund table
    # then with this id go to the mfdata table and get all the vals

    mf_name_key_copy = (mf_name_key,)
    print(type(mf_name_key_copy))

    mf_name_key_id_query = "SELECT id FROM mutual_fund where name = %s"
    mycursor.execute(mf_name_key_id_query, mf_name_key_copy)
    mf_name_key_id = mycursor.fetchall()[0]
    # mf_name_key_id = mycursor.fetchall()
    # mf_name_key_id = mf_name_key_id[0]

    print(mf_name_key_id)

    mf_name_mfdata_query = "SELECT * FROM mfdata where mutual_fund_id = %s"
    mycursor.execute(mf_name_mfdata_query, mf_name_key_id)
    mf_deets = mycursor.fetchall()[0]
    print(mf_deets)
    print(type(list(mf_deets)))

    return list(mf_deets)

get_mf_params("ICICI Prudential Value Discovery Fund  - Growth")