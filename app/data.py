import sqlite3
import json

# 讀取JSON數據
with open('data.json', 'r') as file:
    data = json.load(file)

# 連接到SQLite數據庫
conn = sqlite3.connect('../mydatabase.db')
cursor = conn.cursor()

# 插入Users數據
for item in data["Users"]:
    cursor.execute('''
        INSERT INTO Users (Username, Email, PasswordHash, CreateDate)
        VALUES (:Username, :Email, :PasswordHash, :CreateDate)
    ''', item)

# 插入Transactions數據
for item in data["Transactions"]:
    cursor.execute('''
        INSERT INTO Transactions (UserID, CategoryID, Amount, TransactionDate, Description, PaymentMethodID)
        VALUES (:UserID, :CategoryID, :Amount, :TransactionDate, :Description, :PaymentMethodID)
    ''', item)

# 提交事務並關閉連接
conn.commit()
conn.close()
