Project Brief
1. Online store capabilities selling various branded merchandise.
2. Customer interactions - products comments / reviews
3. Website keywords search form with robust search and filter functionality. (ES)
4. Live chat help desk
5. Customer coupon system
6. Customer portal


Database Tables

- User
- Product
- Helpdesk
- Comments
- ....

Design DB forming 
![db_design.png](imgs%2Fdb_design.png)

Practice

- Test first approach
- Django
- Django
- Django Templating system
- PSQL

Mission Statement
1.a. The porpuse of the inventory app database is to maintan the data that is needed to support online retail sales ans stock inventory management.
1.b.(рус). Назначение базы данных приложения инвентаризации заключается в хранении данных, необходимых для поддержки розничных продаж в Интернете и управления запасами.
Mission Objectives
- maintain information on multiple types of products;
- keep track of stock levels.
- keep track of user's interaction 

Think about
- what needs to apeat on the website
- what do customers need to know about a product
  - Preliminary field list(base):
    - Name
    - description
    - SKU (Stock Keeping Unit): number unique identifies a product (size, color, brand)  - his uuid in warehouse
    - type
    - image 
    - color
    - size
    - brand
    - wight
    - category
    - RR_price (retail recommended - product manufacture may give guidance to sellers) 
    - stock price
    - sale_price
    - stock_qty
    - created
    - updated
* У вас есть разные модели обуви, разные размеры, разные цвета. Каждая комбинация модели, размера и цвета будет иметь свой уникальный SKU.

Например, ботинки Nike Air Force, размер 42, цвет черный, могут иметь SKU "NAF-42-BLK". Это позволит вам точно знать, сколько у вас на складе именно таких пар обуви, какие продажи были, какой товар нужно заказать и т.д.

- what daa is need to record stock level / management  (уровень запасов/управление запасами)


Resolve any multivalued field you encounter in a table
1. Remove the field from the table and use it as the basis of new table.
2. Select connecting fields that will relate the PRODUCT table to the new table and add them to the structure of the new table.
3. Give the new table name, compose a suitable description.
1. Удалите поле из таблицы и используйте его в качестве основы новой таблицы.
2. Выберите соединительные поля, которые будут связывать таблицу PRODUCT с новой таблицей, и добавьте их в структуру новой таблицы.
3. Дайте новой таблице имя, составьте подходящее описание.

Resolve any multivalued field you encounter in a table

- single-or multivalued field depends on a particular multivalued field
  - fix this problem by including the dependent field in the structure of the new table you build to resolve the multivalued field
- одно- или многозначное поле зависит от конкретного многозначного поля
  - устраните эту проблему, включив зависимое поле в структуру новой таблицы, которую вы создаете для разрешения многозначного поля

- так же то что повторяется, как напрмер, color и сайз - могут также отнестись к отдельным полям - decompose of redundancy
- а то что является уникальным или динамически изменяемый - пусть отностятся как уикальное к продукту


Ideal Fields

- representing a distinct characteristic of the subject of the table
- should contains a single value
- cannot be deconstructed into smaller components
- avoid a calculated or concatenated values
- unique within the entire database structure
- (ru)
- представляющий собой отдельную характеристику субъекта таблицы
- должно содержать единственное значение
- не может быть разложена на более мелкие компоненты
- избегать вычисленных или конкатенированных значений
- уникальным в рамках всей структуры базы данных







