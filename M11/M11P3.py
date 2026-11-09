def calculate_sales(sales):
    if sales > 100000:
        commission_rate = 0.10
    else:
        commission_rate = 0.05

    commission = sales * commission_rate
    next_year_target = sales * 1.05

    if next_year_target > 100000:
        next_year_rate = 0.10
    else:
        next_year_rate = 0.05

    next_year_commission = next_year_target * next_year_rate

    return commission, next_year_target, next_year_commission


def main():
    last_name = input("Enter salesperson's last name: ")
    sales = float(input("Enter total sales: "))

    commission, target, future_commission = calculate_sales(sales)

    print("Salesperson:", last_name)
    print("Commission: $", format(commission, ".2f"))
    print("Next year's sales target: $", format(target, ".2f"))
    print("Next year's commission: $", format(future_commission, ".2f"))


main()
