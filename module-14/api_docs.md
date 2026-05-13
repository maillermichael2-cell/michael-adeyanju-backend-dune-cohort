API DOCUMENTATION

AUTHENTICATION ENDPOINTS

### 1. obtain JWT Token pair 
* **URL:** '/api/token/'
* **METHOD:** 'POST'
* **Auth Required:** No
* **Request Body (JSON):**
        ```
            {
                "username": "User username",
                "password": "user password"
            }
        ```
* **Success Response (200 OK):**   *NOTE THE REFRESH AND ACCESS TOKEN ARE EXPIRED THIS IS JUST AN EXAMPLE*
        ```
            {
                "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3ODY3NTYzMCwiaWF0IjoxNzc4NTg5MjMwLCJqdGkiOiI2NDY1YTQyMGVjOGY0YjY1OWQ1MTRkMmQyODJkMTFkYiIsInVzZXJfaWQiOiIzIn0.HejJtTpkX1acjqFLGRc1MqjrFqKunaVHDv2cpo8dsgg",
                "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NTkwMTkwLCJpYXQiOjE3Nzg1ODkyMzAsImp0aSI6ImQwNDI3ZTBiM2RiNTRiODc4MjExMmE0ZDdlNGVkN2JlIiwidXNlcl9pZCI6IjMifQ.gPA9aZCurbyLso35YEzwBBw_5sqvwPj9ZN-wqBGMdGM"
            }
        ```

### 2. Refresh JWT Token 
* **URL:** '/api/token/refresh/'
* **METHOD:** 'POST'
* **Auth Required:** No
* **Request Body (JSON):**
        ```
            {
                "refresh": "yoru refresh token here"
            }
        ```
* **Success Response (200 OK):**   *NOTE THE ACCESS TOKEN IS EXPIRED THIS IS JUST AN EXAMPLE*
        ```
            {
                "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NTkwMTkwLCJpYXQiOjE3Nzg1ODkyMzAsImp0aSI6ImQwNDI3ZTBiM2RiNTRiODc4MjExMmE0ZDdlNGVkN2JlIiwidXNlcl9pZCI6IjMifQ.gPA9aZCurbyLso35YEzwBBw_5sqvwPj9ZN-wqBGMdGM"
            }
        ```

### 3. List Products with pagination 
* **URL:** '/api/products/'
* **METHOD:** 'GET'
* **Auth Required:** No
* **Query parameteres:**
  * `page`: Integer (Page number)
  * `category`: String (filter)
  * `is_available`: Boolean (filter)
  * `search`: String (Searches with `namme` and `category_name` fields)
  * `ordering`: String(`-created_at`)
* **Success Response (200 OK):**   *NOTE THIS IS JUST AN EXAMPLE*
        ```
           {
        "count": 12,
        "next": "http://127.0.0.1:3000/api/products/?page=2",
        "previous": null,
        "results": [
            {
                "id": 21,
                "name": "lenovo-gaming-laptop",
                "price": "500000.00",
                "stock": 5,
                "is_available": true,
                "created_at": "2026-04-29T11:24:22.460378Z",
                "category": {
                    "id": 3,
                    "name": "Gadgets",
                    "product_count": 6
                },
                "created_by": null
            },
            {
                "id": 20,
                "name": "samsung 25inch tv",
                "price": "400000.00",
                "stock": 10,
                "is_available": true,
                "created_at": "2026-04-28T14:08:16.353986Z",
                "category": {
                    "id": 3,
                    "name": "Gadgets",
                    "product_count": 6
                },
                "created_by": null
            },
            {
                "id": 18,
                "name": "golden phoenix fires 2kg",
                "price": "16500.00",
                "stock": 10,
                "is_available": true,
                "created_at": "2026-04-24T19:37:20.565882Z",
                "category": {
                    "id": 7,
                    "name": "food",
                    "product_count": 1
                },
                "created_by": null
            },
            {
                "id": 17,
                "name": "armani foundation",
                "price": "3500.00",
                "stock": 2,
                "is_available": true,
                "created_at": "2026-04-24T15:11:52.381213Z",
                "category": {
                    "id": 1,
                    "name": "Cosmetics",
                    "product_count": 3
                },
                "created_by": null
            },
            {
                "id": 13,
                "name": "nivea lip balm",
                "price": "6500.00",
                "stock": 10,
                "is_available": true,
                "created_at": "2026-04-24T14:24:43.595250Z",
                "category": {
                    "id": 1,
                    "name": "Cosmetics",
                    "product_count": 3
                },
                "created_by": null
            },
            {
                "id": 12,
                "name": "oraimo head of charger",
                "price": "2500.00",
                "stock": 10,
                "is_available": true,
                "created_at": "2026-04-24T14:19:28.297673Z",
                "category": {
                    "id": 3,
                    "name": "Gadgets",
                    "product_count": 6
                },
                "created_by": null
            }
        ]
    } 
        ```

### 4. Create Product 
* **URL:** '/api/products/'
* **METHOD:** 'POST'
* **Auth Required:** Yes (`Bearer your_access_token`)
* **Headers:**
 * `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NTkwMTkwL `
* **Request Body (JSON):**
        ```
            {
                "name":"wireless speaker",
                "description": "speaker",
                "price":"130000",
                "stock":15,
                "category_id":1
            }
        ```
* **Success Response (200 CREATED):**   *NOTE IS JUST AN EXAMPLE*
        ```
            {
                "id": 17,
                "name":"wireless speaker",
                "description": "speaker",
                "price":"130000",
                "stock":15,
                "category_id":1
                "created_at": "2026-05-13T11:27:002"
                "created_by": 1 
            }
        ```

### 5. Update Product Details 
* **URL:** '/api/products/<id>/'
* **METHOD:** 'PUT'
* **Auth Required:** Yes (`Must be the specific authenticated account that created the product`)
* **Headers:**
 * `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NTkwMTkwL `
* **Request Body (JSON):**
        ```
            {
                "name":"oraimo wireless speaker",  `<-- the edited field`
                "description": "speaker",
                "price":"130000",
                "stock":15,
                "category_id":1
            }
        ```
* **Success Response (200 CREATED):**   *NOTE IS JUST AN EXAMPLE*
        ```
            {
                "id": 18,
                "name":"oraimo wireless speaker",  `new change `
                "description": "speaker",
                "price":"130000",
                "stock":15,
                "category_id":1
                "created_at": "2026-05-13T11:27:002"
                "created_by": 1 
            }
        ```

### 4. Delete Product  
* **URL:** '/api/products/<id>/'
* **METHOD:** 'DELETE'
* **Auth Required:** Yes (`Must be the specific authenticated account that created the product`)
* **Headers:**
 * `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzc4NTkwMTkwL `
* **Request Body (JSON):**
        ```
            {
                "name":"oraimo wireless speaker",  `<-- the edited field`
                "description": "speaker",
                "price":"130000",
                "stock":15,
                "category_id":1
            }
        ```
* **Success Response (200 CREATED):**   *NOTE IS JUST AN EXAMPLE*
        * **Success Response (204 No content):** Record wiped successfully
        * **Error Response (403 forrbidden):** Action rejected to non owner request token manipulation 
        














