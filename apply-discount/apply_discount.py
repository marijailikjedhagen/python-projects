def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return 'The price should be a number'
    if not isinstance(discount, (int, float)):
        return 'The discount should be a number'
    if price <= 0:
        return 'The price should be greater than 0'
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'

    discount_amount = price * discount / 100
    return price - discount_amount


if __name__ == '__main__':
    print(apply_discount(50, 20))     # 40.0
    print(apply_discount('50', 20))   # The price should be a number
    print(apply_discount(50, 150))    # The discount should be between 0 and 100
