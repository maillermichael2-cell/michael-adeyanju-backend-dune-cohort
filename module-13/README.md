### PROJECT DESCRIPTION 
        PRODUCT API ENDPOINTS :
            | Method                | Endpoint                  | Description
            |-----------------------|---------------------------|--------------------------------------------------------|
            | **GET**               | '/api/products/'          | list all products with nested category details         
            | **POST**              | '/api/products/'          | Create a new product.
            | **GET**               | '/api/products/{id}/'     | retrive a specific product details.
            | **PUT**               | '/api/products/{id}/'     | update all fields of an exisiting product.
            | **DELETE**            | '/api/products/{id}/'     | Remove a product from the database.
        
        CATEGORY API ENDPOINTS :
            | METHOD                | ENDPOINT                  | DESCRIPTION
            |-----------------------|---------------------------|----------------------------------------------------------|
            | **GET**               | '/api/categories'         | List all categories including a dynamic 'product-count'.

## SETUP INSTRUCTIONS
    MOVING IN DIRECTORIES: 
        a. cd into the assignments folder
        b. cd into module-13 folder
        c. then cd into torilo shop 
        d. then install pillow pip install pillow or py -m pip install pillow
1. CREATE A VIRTUAL ENVRONMENT: py -m venv env would create a virtual env 
2. ACTIVATE THE VIRTUAL ENVIRONMENT: env\Scripts\Activate would activate the virtual env
3. INSTALL DJANGO:  pip install django would install django in your vitual env 
4. MAKE MIGRATIONS AND MIGRATE: py manage.py makemigrations then py manage.py migrate
5. CREATE SUPERUSER : py manage.py createsuperuser 
6. RUN SERVER : py manage.py runserver - this would start the development server note default port is 8000


# SCREEN SHOTS 
1. GET PRODUCTS  ![GET PRODUCTS](screenshots/01_get_products.png)
2. POST CREATE PRODUCT ![POST CREATE PRODUCT](screenshots/02_post_create_product.png)
3. GET SINGLE PRODUCT ![GET SINGLE PRODUCT](screenshots/03_get_single_product.png)
4. PUT UPDATE PRODUCT ![PUT UPDATE PRODUCT](screenshots/04_put_update_product.png)
5. DELETE PRODUCT ![DELETE PRODUCT](screenshots/05_delete_product.png)
6. GET CATEGROIES ![GET CATEGORIES](screenshots/06_get_categories.png)


## POST MAN 
a. POST MAN [DOWNLOAD POSTMAN COLLECTION](./postman_collection.json)