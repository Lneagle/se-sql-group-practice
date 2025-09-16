import pandas as pd
import sqlite3


conn = sqlite3.connect('data.sqlite')

products = pd.read_sql("""
SELECT *
 FROM products;
""", conn)
print(products)

step1 = pd.read_sql("""
SELECT productLine, COUNT(*) AS count
    FROM products
    GROUP BY productLine
    ORDER BY count DESC;
""", conn)
print(step1)

step2 = pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice
    FROM products
    GROUP BY productLine
    ORDER BY avgPrice DESC;
""", conn)
print(step2)

step3 = pd.read_sql("""
SELECT productLine, min(MSRP) AS minMSRP, max(MSRP) AS maxMSRP
    FROM products
    GROUP BY productLine;
""", conn)
print(step3)

step4 = pd.read_sql("""
SELECT productLine, min(MSRP) AS minMSRP, max(MSRP) AS maxMSRP
    FROM products
    WHERE MSRP >= 50
    GROUP BY productLine;
""", conn)
print(step4)

step5 = pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice
    FROM products
    GROUP BY productLine
    HAVING avgPrice > 50
    ORDER BY avgPrice DESC;
""", conn)
print(step5)

step6 = pd.read_sql("""
SELECT productLine, AVG(buyPrice) AS avgPrice, AVG(MSRP) AS avgMSRP
    FROM products
    WHERE MSRP >= 50
    GROUP BY productLine
    HAVING avgPrice >= 50
    ORDER BY avgPrice ASC;
""", conn)
print(step6)

conn.close()