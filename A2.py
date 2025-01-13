#Q1
products = [
    ("Laptop", 1200, 5),
    ("Smartphone", 700, 10),
    ("Headphones", 150, 15),
    ("Monitor", 300, 7)
]

threshold = 500

above_threshold = [product[0] for product in products if product[1] > threshold]

print("Products above the price threshold:", above_threshold)

#Q2

salaries = {
    101: 50000,
    102: 60000,
    103: 55000
}


increments = [
    (101, 10), 
    (104, 5),   
    (102, 15)
]

for emp_id, percent_inc in increments:
    if emp_id in salaries:
       
        salaries[emp_id] += salaries[emp_id] * percent_inc // 100

print("Updated salaries:", salaries)

