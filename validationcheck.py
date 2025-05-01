import datetime

# Get product ID list from DataFrame
def get_product_ids(df):
    return df["product_id"].astype(str).to_list()

# Check if product ID exists in product list
def product_id_check(pid, products):
    return str(pid) in products

# Check if city name is valid
def city_check(city):
    return city.strip() in ["Mumbai", "Bangalore"]

# Check if order date is today or in the past
def order_date_check(date):
    try:
        order_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        today_date = datetime.date.today()
        return (today_date - order_date).days >= 0
    except ValueError:
        return False

# Check for any empty values in order dictionary
def empty_values_check(order):
    empty_col = [k for k, v in order.items() if k != "rejected_reason" and (not v or v == "")]
    return empty_col

# Create a dictionary mapping product_id to price
def get_product_dict(df_products):
    return df_products.set_index(df_products["product_id"].astype(str))["price"].astype(int).to_dict()

# Check if sales value matches price * quantity
def sales_values_check(order, product_dict):
    pid = str(order.get("product_id"))
    if pid in product_dict:
        try:
            price = int(product_dict[pid])
            quantity = int(order["quantity"])
            sales = int(order["sales"])
            return sales == price * quantity
        except (ValueError, KeyError):
            return False
    return False




