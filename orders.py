operator = ({"name": "Marina", "mail": "test@test.com"})

orders = {
    "state": 0,
    "data": [
        {
            "_id": "3d8c861f-e2c0-442a-9d82-810ae5eb5f52",
            "count": 1,
            "brand_id": 84375,
            "delay": 1,
            "startedAt": "2024-03-21T16:48:03.513Z",
            "completedAt": "2024-03-21T16:48:03.513Z",
            "completed": 0,
            "wait_refund": 0,
            "refunded": 0
        },
        {
            "_id": "4816385b-a5a5-4341-aedf-6f80bedbdce4",
            "count": 2,
            "brand_id": 88339,
            "delay": 2,
            "startedAt": "2024-03-21T16:27:32.062Z",
            "completedAt": "2024-03-21T16:28:32.062Z",
            "completed": 0,
            "wait_refund": 2,
            "refunded": 0
        },
        {
            "_id": "7e0882b5-38b8-4dcb-9825-625158a92314",
            "count": 16,
            "brand_id": 88339,
            "delay": 3,
            "startedAt": "2024-03-21T16:17:04.723Z",
            "completedAt": "2024-03-21T16:17:04.723Z",
            "completed": 7,
            "wait_refund": 3,
            "refunded": 6
        }
    ]
}

completed_cnt = 0
wait_refund_cnt = 0
refunded_cnt = 0

all_ids = []
for order in orders["data"]:
    all_ids.append(order["_id"])
    completed_cnt += order["completed"]
    wait_refund_cnt = wait_refund_cnt + order["wait_refund"]
    refunded_cnt = refunded_cnt + order["refunded"]

all_ids.append("326b23a1-e6ab-4b4a-84a1-a3ecb33afc97")

orders_info = {
    "completed": completed_cnt,
    "wait_refund": wait_refund_cnt,
    "refunded": refunded_cnt
}

report = {
    "order_ids": all_ids,
    "orders_info": orders_info
}

print(operator, report)

assert len(orders["data"]) > 0
assert(orders["data"][0]["delay"] <= 6 and orders["data"][1]["delay"] <= 6)
assert((orders["data"][2]["count"] == orders["data"][2]["completed"] + orders["data"][2]["wait_refund"] + orders["data"][2]["refunded"])
       and ((orders["data"][2]["count"] / 2 <= orders["data"][2]["completed"])
       or (orders["data"][2]["completed"] > orders["data"][2]["refunded"] > orders["data"][2]["wait_refund"])))


