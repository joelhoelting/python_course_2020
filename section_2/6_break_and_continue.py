# -- break --
# Exits out of the loop, so that no more iterations occur.
#
# cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]
#
# for status in cars:
#     print(f"This car is {status}")
#     if status == "faulty":
#         print("Stopping the production line")
#         continue
#     print(f"This car is {status}")
#     print("Shipping car to customer")
#
#     cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Stopping the production line")
        all_successful = False
        break
    print(f"This car is {status}")
    print("Shipping car to customer")
else:
    print("All Cards built successfully")