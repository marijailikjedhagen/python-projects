# Apply Discount

`apply_discount(price, discount)` returns the final price after a percentage discount,
or an error message if the inputs are invalid (non-numbers, a price of 0 or less,
or a discount outside 0–100).

```python
apply_discount(50, 20)   # 40.0
```

Run it: `python apply_discount.py`
