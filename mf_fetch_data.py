# importing necessary libraries
from bs4 import BeautifulSoup
import requests
import datetime

# mf_info = []

all_mfs_info = []
database_all_mf_info = []


# dummy uRL?
def getting_mf_info(urls):
    for URL in urls:
        #url = "https://www.moneycontrol.com/mutual-funds/nav/aditya-birla-sun-life-frontline-equity-fund-direct-plan/MBS813"
        url = URL
        print("blah")
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html5lib')

        mf_info = []
        database_mf_info = []
        category_name = ""
        mf_name = ""

        # all the divs that contain the required span tags have class = percentage
        # so i'm counting the no of divs i've come across that has the class = percentage
        # based on that class, i'm getting the values between the span tags to get the req values
        def get_mf_name():
            mf_name_full = soup.find("h1", {"class": "page_heading navdetails_heading"}).get_text()
            #mf_name_full = mf_name_full.partition('-')
            #mf_name_req = mf_name_full[0]
            print(mf_name_full)
            database_mf_info.append(mf_name_full)

        def get_cat_name():
            cat_full_name = soup.find("span", {"class": "hidden-xs hidden-sm"}).get_text()
            cat_name = cat_full_name[:-2]
            print(cat_name)
            database_mf_info.append(cat_name)

        def risk_ratios():  # 6
            for name_val in soup.findAll("h3", {"class": "list TAC"}):
                if "Standard Deviation" in name_val.get_text():
                    std_dev = name_val.find_parent('li').findChildren()[7].get_text()
                    std_dev_category_avg = name_val.find_parent('li').findChildren()[9].get_text()
                    std_dev = float(std_dev)
                    std_dev_category_avg = float(std_dev_category_avg)
                    # print(std_dev, std_dev_category_avg)
                if "Beta" in name_val.get_text():
                    beta = name_val.find_parent('li').findChildren()[7].get_text()
                    beta_category_avg = name_val.find_parent('li').findChildren()[9].get_text()
                    beta = float(beta)
                    beta_category_avg = float(beta_category_avg)
                    # print(beta, beta_category_avg)
                if "Sharpe Ratio" in name_val.get_text():
                    sharpe_ratio = name_val.find_parent('li').findChildren()[7].get_text()
                    sharpe_ratio_category_avg = name_val.find_parent('li').findChildren()[9].get_text()
                    sharpe_ratio = float(sharpe_ratio)
                    sharpe_ratio_category_avg = float(sharpe_ratio_category_avg)
                    # print(sharpe_ratio, sharpe_ratio_category_avg)
                if "Treynor's Ratio" in name_val.get_text():
                    treynor_ratio = name_val.find_parent('li').findChildren()[7].get_text()
                    treynor_ratio_category_avg = name_val.find_parent('li').findChildren()[9].get_text()
                    treynor_ratio = float(treynor_ratio)
                    treynor_ratio_category_avg = float(treynor_ratio_category_avg)
                    # print(treynor_ratio, treynor_ratio_category_avg)
                if "Jension's Alpha" in name_val.get_text():
                    alpha = name_val.find_parent('li').findChildren()[7].get_text()
                    alpha_category_avg = name_val.find_parent('li').findChildren()[9].get_text()
                    alpha = float(alpha)
                    alpha_category_avg = float(alpha_category_avg)
                    # print(alpha, alpha_category_avg)

            # print("standard deviation = ", std_dev, "standard deviation average value", std_dev_category_avg)
            # print("beta  = ", beta, "beta average value", beta_category_avg)
            # print("jension's alpha  = ", alpha, "alpha average value", alpha_category_avg)
            # print("sharpe ratio  = ", sharpe_ratio, "sharpe ratio average value", sharpe_ratio_category_avg)
            # print("treynor's ratio  = ", treynor_ratio, "treynor's ratio average value", treynor_ratio_category_avg)
            mf_info.extend(
                [std_dev, std_dev_category_avg, beta, beta_category_avg, alpha, alpha_category_avg, sharpe_ratio,
                 sharpe_ratio_category_avg, treynor_ratio, treynor_ratio_category_avg])

        # parent div class= crisil_rank_block, needed div is the fifth child and have to access the span class in that
        # so first the parent div whose class is crisil_rank_block is located
        # then i used the method findChildren() which finds all the children of a certain tag and you can extract the required
        #       child by mentioning which child it is in []
        # after finding the required div, i used the same method again so that i can iterate through the children
        #       of that child div and count the no of tags which is the no of stars that are printed in the
        #       website
        # the no of tags in req_child_crisil_rank is the no of stars of crisil rank
        def crisil_rank():
            count_stars = 0
            parent_div_crisil_rank = soup.find("div", {"class": "crisil_rank_block"})
            req_child_crisil_rank = parent_div_crisil_rank.findChildren()[5]
            content_in_div = req_child_crisil_rank.findChildren()
            for child_span_star in content_in_div:
                count_stars += 1
            crisil_rank_val = count_stars
            # print("crisil rank = ", crisil_rank_val, " stars")
            mf_info.append(crisil_rank_val)  # ranking - 1

        # def Portfolio_Turnover_Ratio():
        #     div_ratio_req = soup.find("div", {"class": "subheading"})
        #     ratio_req = div_ratio_req.findChild()
        #     turnover_ratio = ratio_req.get_text()
        #     turnover_ratio = float(turnover_ratio[:-1])
        #     # print(type(turnover_ratio))   # 5- turnover ratio
        #     mf_info.append(turnover_ratio)

        # i searched for the tag span which has class = status
        # then the value in the value in the span tag was extracted in the variable risk_o_meter_val
        def risk_o_meter():  # 7
            for val_meter in soup.select("span.status"):  # working
                risk_o_meter_val = val_meter.get_text()
            print("risk o meter = ", risk_o_meter_val)
            mf_info.append(risk_o_meter_val)

        # the table with class = navdetails contains the expense and fund size values
        # based on the count of span tags that have the class = amt, both teh values are extracted
        def table_navdetails():
            count_table_navdetails = 0
            for val_table_navdetails in soup.select("span.amt"):  # working
                count_table_navdetails += 1
                if count_table_navdetails == 3:
                    expense_ratio = val_table_navdetails.get_text()
                if count_table_navdetails == 2:
                    fund_size = val_table_navdetails.get_text()

            # changing to req data types
            fund_size = int(fund_size[2:][:-6])
            expense_ratio = float(expense_ratio[:-1])
            print("fund size = ", fund_size)  # 4 - assets under management
            print("expense ratio = ", expense_ratio)  # 3
            mf_info.append(expense_ratio)
            mf_info.append(fund_size)

        # Function to convert string to datetime
        def convert_time(date_time):
            format = '%d-%b-%y'  # The format
            datetime_str = datetime.datetime.strptime(date_time, format)

            return datetime_str

        # since multiple tables had the class = mctable1, i used the parent div of the table to get the req table\
        # the findChild() function gives the first child that's found
        # stored all the details of the table in a 2D array called data
        # i only iterated through the body of the table since the table head wasn't necessary
        # the strip() method removes and whitespace or special characters at the end of a string
        # the values are then taken by getting the data from the specific row and column

        def returns():  # 2
            div_parent_table = soup.find("div", {"class": "data_container returns_table table-responsive"})
            child_table = div_parent_table.findChild()

            data = []
            table_body = child_table.find('tbody')

            rows = table_body.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]  # ele = element
                data.append([ele for ele in cols if ele])  # Get rid of empty values

            annualised_return_1yr = data[5][4]
            annualised_return_2yr = data[6][4]
            annualised_return_3yr = data[7][4]
            annualised_return_5yr = data[8][4]
            since_inception_return = data[9][4]
            inception_date = data[9][1]

            # converting all the vals apart frominception date to integers
            annualised_return_1yr = float(annualised_return_1yr[:-1])
            annualised_return_2yr = float(annualised_return_2yr[:-1])
            annualised_return_3yr = float(annualised_return_3yr[:-1])
            annualised_return_5yr = float(annualised_return_5yr[:-1])
            since_inception_return = float(since_inception_return[:-1])

            # converting inception date to datetime type
            inception_date = convert_time(inception_date)

            # print("inception date = ", inception_date)
            # print("1st yr annualised returns = ", annualised_return_1yr)
            # print("2nd yr annualised returns = ", annualised_return_2yr)
            # print("3rd yr annualised returns = ", annualised_return_3yr)
            # print("5th yr annualised returns = ", annualised_return_5yr)
            # print("since inception return = ", since_inception_return)
            mf_info.extend(
                [inception_date, annualised_return_1yr, annualised_return_2yr, annualised_return_3yr,
                 annualised_return_5yr,
                 since_inception_return])

        get_mf_name()
        get_cat_name()
        crisil_rank()
        returns()
        table_navdetails()
        # Portfolio_Turnover_Ratio()
        risk_ratios()
        risk_o_meter()

        #print(mf_info)
        print("one url done")

        all_mfs_info.append(mf_info)
        database_all_mf_info.append(database_mf_info)
    print(database_all_mf_info)
    #print(all_mfs_info)
    return all_mfs_info
    # def call_functions():
    #     crisil_rank()
    #     returns()
    #     table_navdetails()
    #     # Portfolio_Turnover_Ratio()
    #     risk_ratios()
    #     risk_o_meter()
    #
    #     return mf_info

# print(*mf_info, sep="\n")
# ls = [type(item) for item in mf_info]
# print(ls)
