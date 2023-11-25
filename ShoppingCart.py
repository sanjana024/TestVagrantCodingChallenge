
basket = {
    "Leather wallet": {"quantity": 1, "unit_price": 1100},
    "Cigarette": {"quantity": 4, "unit_price": 900},
    "Umbrella": {"quantity": 12, "unit_price": 200},
    "Honey": {"quantity": 28, "unit_price": 100},
}

max_gst_product = None
max_gst_amount = 0

for product, details in basket.items():
    quantity = details["quantity"]
    unit_price = details["unit_price"]
    gst_amount = 0.18 * (quantity * unit_price)  #18% GST

    if gst_amount > max_gst_amount:
        max_gst_amount = gst_amount
        max_gst_product = product

#total amount to be paid to the shopkeeper
total_amount = sum(details["quantity"] * details["unit_price"] for details in basket.values())

max_gst_product, max_gst_amount, total_amount