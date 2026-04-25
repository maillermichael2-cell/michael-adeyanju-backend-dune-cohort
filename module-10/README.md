### PROJECT DESCRIPTION 
        CRUD OPERATIONS TORILOSHOP NOW SUPPORTS:
            CREATE : this uses the post method to create a new product
            READ : this use the get method to get all products
            UPDATE : used to update the product info
            DELETE : remove the product from the database
             

## TORILO SHOP FEATURES 
-------------------------------------------------------------------------------------------------------------------------------------|
|   FORM                | URL                           | WHAT IT DOES
|-----------------------|-------------------------------|------------------------------------------------
| A. ProductForm        | product/add/                  | we can add products using the fields provided by the ProductForm
|                       | product/<int:pk>/edit/        | we can edit a paarticular product using the id 
|-----------------------|-------------------------------|------------------------------------------------------------------------------
| B. CategoryForm       | categories/add/               | we can add categories using the fields provided by the CategoryForm
|                       | categories/<int:pk>/edit/     | we can edit a particular product using the id
|______________________________________________________________________________________________________________________________________|


## SETUP INSTRUCTIONS
    MOVING IN DIRECTORIES: 
        a. cd into the assignments folder
        b. cd into module-9 folder
        c. then cd into torilo shop 
1. CREATE A VIRTUAL ENVRONMENT: py -m venv env would create a virtual env 
2. ACTIVATE THE VIRTUAL ENVIRONMENT: env\Scripts\Activate would activate the virtual env
3. INSTALL DJANGO:  pip install django would install django in your vitual env 
4. MAKE MIGRATIONS AND MIGRATE: py manage.py makemigrations then py manage.py migrate
5. CREATE SUPERUSER : py manage.py createsuperuser 
6. RUN SERVER : py manage.py runserver - this would start the development server note default port is 8000


# SCREEN SHOTS 
1. PRODUCT LIST - ![PRODUCT LIST](screenshots/01_product_list.png)
2. ADD PRODUCT - ![ADD PRODUCT](screenshots/02_add_product_form.png)
3. EDIT PRODUCT FORM - ![EDIT PRODUCT FORM](screenshots/03_edit_product_form.png)
4. DELETE CONFIRMATION ![DELETE CONFIRMATION](screenshots/04_delete_confirmation.png)
5. FORM VALIDATION ERROR ![FORM VALIDATION ERROR](screenshots/05_form_validation_error.png)
6. SUCCESS FLASH MESAGE ![SUCCESS FLASH MESSAGE](screenshots/06_success_flash_message.png)
