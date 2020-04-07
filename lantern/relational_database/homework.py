
def task_1_add_new_record_to_db(con) -> None:
    """
    Add a record for a new customer from Singapore
    {
        'customer_name': 'Thomas',
        'contactname': 'David',
        'address': 'Some Address',
        'city': 'London',
        'postalcode': '774',
        'country': 'Singapore',
    }

    Args:
        con: psycopg connection

    Returns: 92 records

    """
    crsr = con.cursor()
    crsr.execute(
        "INSERT INTO customers (customername, contactname, address, city, postalcode, country)"
        " VALUES ('Thomas', 'David','Some Address','London','774','Singapore');"
    )
    con.commit()


def task_2_list_all_customers(cur) -> list:
    """
    Get all records from table Customers

    Args:
        cur: psycopg cursor

    Returns: 91 records

    """
    query_to_list = []
    cur.execute("SELECT * FROM customers")
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_3_list_customers_in_germany(cur) -> list:
    """
    List the customers in Germany

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    query_to_list = []
    cur.execute("SELECT * FROM customers WHERE country='Germany'")
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_4_update_customer(cur):
    """
    Update first customer's name (Set customername equal to  'Johnny Depp')
    Args:
        cur: psycopg cursor

    Returns: 91 records with updated customer

    """
    crsr = cur.cursor()
    crsr.execute(
        "UPDATE customers SET customername = 'Johnny Depp' WHERE customerid = 1;"
    )


def task_5_delete_the_last_customer(con) -> None:
    """
    Delete the last customer

    Args:
        con: psycopg connection
    """

    crsr = con.cursor()
    crsr.execute(
        "DELETE FROM customers WHERE customerid  in"
        " (SELECT max(customerid) FROM customers);"
    )


def task_6_list_all_supplier_countries(cur) -> list:
    """
    List all supplier countries

    Args:
        cur: psycopg cursor

    Returns: 29 records

    """
    query_to_list = []
    cur.execute("SELECT country FROM suppliers;")
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_7_list_supplier_countries_in_desc_order(cur) -> list:
    """
    List all supplier countries in descending order

    Args:
        cur: psycopg cursor

    Returns: 29 records in descending order

    """
    query_to_list = []
    cur.execute("SELECT country FROM suppliers ORDER BY country desc;")
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_8_count_customers_by_city(cur):
    """
    List the number of customers in each city

    Args:
        cur: psycopg cursor

    Returns: 69 records in descending order

    """
    query_to_list = []
    cur.execute("SELECT city, count(*) FROM customers GROUP BY city ORDER BY count(*) desc,city asc;")

    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_9_count_customers_by_country_with_than_10_customers(cur):
    """
    List the number of customers in each country. Only include countries with more than 10 customers.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    query_to_list = []
    cur.execute("SELECT country, count(*) FROM customers GROUP BY country having count(*)>10;")

    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_10_list_first_10_customers(cur):
    """
    List first 10 customers FROM the table

    Results: 10 records
    """
    query_to_list = []
    cur.execute("SELECT * FROM customers limit 10;")

    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_11_list_customers_starting_from_11th(cur):
    """
    List all customers starting from 11th record

    Args:
        cur: psycopg cursor

    Returns: 11 records
    """
    query_to_list = []
    cur.execute("SELECT * FROM customers offset 11;")

    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_12_list_suppliers_from_specified_countries(cur):
    """
    List all suppliers from the USA, UK, OR Japan

    Args:
        cur: psycopg cursor

    Returns: 8 records
    """
    query_to_list = []
    cur.execute("SELECT supplierid, suppliername, contactname, city, country"
                " FROM suppliers WHERE country in ('USA','UK','Japan');")
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_13_list_products_from_sweden_suppliers(cur):
    """
    List products with suppliers from Sweden.

    Args:
        cur: psycopg cursor

    Returns: 3 records
    """
    query_to_list = []
    cur.execute("SELECT productname FROM products WHERE supplierID in ("
                "SELECT supplierid FROM suppliers WHERE country in ('Sweden'));")
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_14_list_products_with_supplier_information(cur):
    """
    List all products with supplier information

    Args:
        cur: psycopg cursor

    Returns: 77 records
    """
    query_to_list = []
    cur.execute("SELECT productid, productname, unit, replace(CAST(price as CHAR(11)),' ','') as price, country,"
                " city, suppliername "
                "FROM products LEFT JOIN suppliers on products.supplierID=suppliers.supplierID;"
                )
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_15_list_customers_with_any_order_or_not(cur):
    """
    List all customers, whether they placed any order or not.

    Args:
        cur: psycopg cursor

    Returns: 213 records
    """
    query_to_list = []
    cur.execute(
        "SELECT customername, contactname, country, orderid FROM customers"
        " LEFT JOIN orders on customers.customerid=orders.customerid;"
        )
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list


def task_16_match_all_customers_and_suppliers_by_country(cur):
    """
    Match all customers and suppliers by country

    Args:
        cur: psycopg cursor

    Returns: 194 records
    """
    query_to_list = []
    cur.execute(
        "SELECT customername, customers.address as address,"
        " customers.country as customercountry,"
        " suppliers.country as suppliercountry, suppliername"
        " FROM customers "
        " FULL OUTER JOIN  suppliers on customers.country=suppliers.country "
        " ORDER BY customercountry, suppliercountry;"
    )
    query_customer = cur.fetchall()
    for row in query_customer:
        query_to_list.append(row)
    return query_to_list

