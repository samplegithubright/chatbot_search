INSERT INTO departments (name) VALUES
('HR'), 
('Engineering'), 
('Sales');

INSERT INTO employees (name, department_id, email, salary) VALUES
('Alice', 2, 'alice@company.com', 80000),
('Bob', 3, 'bob@company.com', 60000),
('Charlie', 2, 'charlie@company.com', 75000),
('David', 1, 'david@company.com', 55000),
('Eve', 3, 'eve@company.com', 62000),
('Frank', 2, 'frank@company.com', 72000),
('Grace', 1, 'grace@company.com', 58000),
('Hannah', 2, 'hannah@company.com', 77000),
('Ian', 3, 'ian@company.com', 61000),
('Jack', 2, 'jack@company.com', 70000);

INSERT INTO orders (customer_name, employee_id, order_total, order_date) VALUES
('John Doe', 2, 1200.50, '2024-01-10'),
('Jane Smith', 1, 500.00, '2024-02-01'),
('Mike Brown', 3, 1500.75, '2024-03-15'),
('Sara White', 5, 2500.00, '2024-04-20'),
('Tom Green', 4, 800.00, '2024-05-05');

INSERT INTO products (name, price) VALUES
('Laptop', 75000),
('Wireless Mouse', 1500),
('Keyboard', 2000),
('Monitor', 12000),
('USB Hub', 800);