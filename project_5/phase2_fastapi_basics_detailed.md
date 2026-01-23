# Phase 2: FastAPI Basics - Complete In-Depth Guide
## From Installation to Building Your First API

---

## **Table of Contents**
1. [Introduction & Setup](#introduction)
2. [Part 1: Installation & Environment Setup](#part-1-setup)
3. [Part 2: Your First FastAPI Application](#part-2-first-app)
4. [Part 3: Path Operations Deep Dive](#part-3-path-operations)
5. [Part 4: Pydantic Models & Validation](#part-4-pydantic)
6. [Part 5: Response Models & Error Handling](#part-5-responses)
7. [Part 6: First Project - Blog API](#part-6-project)
8. [Summary & Next Steps](#summary)

---

## **Introduction** {#introduction}

### **What is FastAPI?**

**FastAPI** is a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.

**Created by:** Sebastián Ramírez in 2018

**Why FastAPI?**
- ⚡ **Fast:** Very high performance, on par with NodeJS and Go
- 🚀 **Fast to code:** Increases development speed by 200-300%
- 🐛 **Fewer bugs:** Reduces human errors by about 40%
- 💡 **Intuitive:** Great editor support with autocomplete everywhere
- 📚 **Easy:** Designed to be easy to learn and use
- 🔒 **Robust:** Production-ready code with automatic docs
- 📖 **Standards-based:** Based on OpenAPI and JSON Schema

### **What Makes FastAPI Special?**

#### **1. Type Hints (Python 3.6+)**
```python
# Without type hints (old Python)
def greet(name):
    return "Hello " + name

# With type hints (modern Python)
def greet(name: str) -> str:
    return "Hello " + name
```

FastAPI uses these type hints for:
- Automatic data validation
- Automatic documentation
- Editor autocomplete
- Type checking

#### **2. Automatic Documentation**
FastAPI automatically generates:
- **Swagger UI** at `/docs`
- **ReDoc** at `/redoc`
- **OpenAPI schema** at `/openapi.json`

You write the code once, get docs for free!

#### **3. Async Support**
```python
# Synchronous (blocking)
def read_file():
    with open("file.txt") as f:
        return f.read()

# Asynchronous (non-blocking)
async def read_file():
    async with aiofiles.open("file.txt") as f:
        return await f.read()
```

FastAPI supports both sync and async!

### **Prerequisites for This Phase**

✅ Python 3.7+ installed on Windows 11
✅ Understanding of Phase 1 (HTTP & REST)
✅ Basic Python knowledge (variables, functions, dictionaries)
✅ VS Code or PyCharm installed
✅ Terminal/Command Prompt familiarity

**Time Required:** 14-21 days (2-3 hours daily)

---

## **PART 1: Installation & Environment Setup** {#part-1-setup}

### **1.1 Verify Python Installation**

Open **Command Prompt** or **Windows Terminal** (recommended):

```cmd
python --version
```

You should see something like:
```
Python 3.11.5
```

If not installed:
1. Go to https://www.python.org/downloads/
2. Download Python 3.11 or later
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Install

### **1.2 Understanding Virtual Environments**

#### **What is a Virtual Environment?**

Think of it like a separate room in your house:
- Each project gets its own room (virtual environment)
- Each room has its own furniture (packages)
- Changes in one room don't affect others

**Why Use Virtual Environments?**
```
Project A needs FastAPI 0.95
Project B needs FastAPI 0.100
Without virtual env → CONFLICT!
With virtual env → Both work perfectly
```

#### **Creating a Virtual Environment on Windows 11**

**Step 1: Create a project folder**
```cmd
cd C:\Users\YourName\Desktop
mkdir fastapi_learning
cd fastapi_learning
```

**Step 2: Create virtual environment**
```cmd
python -m venv venv
```

This creates a `venv` folder with:
```
venv/
├── Scripts/
│   ├── activate.bat      ← Windows activation script
│   ├── python.exe        ← Isolated Python
│   └── pip.exe          ← Isolated pip
├── Lib/
└── Include/
```

**Step 3: Activate the virtual environment**
```cmd
venv\Scripts\activate
```

You'll see:
```cmd
(venv) C:\Users\YourName\Desktop\fastapi_learning>
```

The `(venv)` indicates you're inside the virtual environment!

**Step 4: Deactivate (when done)**
```cmd
deactivate
```

**Important Notes:**
- ✅ ALWAYS activate before working on your project
- ✅ Each project should have its own venv
- ❌ Don't commit venv to Git (add to .gitignore)

---

### **1.3 Installing FastAPI and Dependencies**

Make sure your virtual environment is activated:

```cmd
(venv) pip install fastapi
```

This installs FastAPI, but you also need a server:

```cmd
(venv) pip install "uvicorn[standard]"
```

**What is Uvicorn?**
- **Uvicorn** = ASGI server (runs your FastAPI app)
- **ASGI** = Asynchronous Server Gateway Interface
- Think of it as the engine that powers your API

**Verify installation:**
```cmd
pip list
```

You should see:
```
Package         Version
--------------- -------
fastapi         0.104.1
uvicorn         0.24.0
pydantic        2.5.0
...
```

---

### **1.4 Setting Up VS Code**

#### **Install VS Code Extensions**

1. Open VS Code
2. Go to Extensions (Ctrl+Shift+X)
3. Install:
   - **Python** (by Microsoft)
   - **Pylance** (advanced IntelliSense)
   - **Thunder Client** (API testing, alternative to Postman)
   - **Better Comments** (optional, for better code comments)

#### **Configure Python Interpreter**

1. Open your `fastapi_learning` folder in VS Code
2. Press `Ctrl+Shift+P`
3. Type: "Python: Select Interpreter"
4. Choose the one inside your venv:
   ```
   .\venv\Scripts\python.exe
   ```

Now VS Code will use your virtual environment!

---

### **1.5 Project Structure Setup**

Create this structure:
```
fastapi_learning/
├── venv/                    ← Virtual environment (don't touch)
├── main.py                  ← Your main FastAPI app
├── requirements.txt         ← List of dependencies
└── .gitignore              ← Files to ignore in Git
```

**Create .gitignore:**
```gitignore
venv/
__pycache__/
*.pyc
.env
.vscode/
```

**Create requirements.txt:**
```cmd
pip freeze > requirements.txt
```

This creates a file like:
```txt
fastapi==0.104.1
uvicorn==0.24.0
pydantic==2.5.0
...
```

**Why requirements.txt?**
- Others can install same versions: `pip install -r requirements.txt`
- Ensures consistency across machines
- Standard Python practice

---

## **PART 2: Your First FastAPI Application** {#part-2-first-app}

### **2.1 Hello World in FastAPI**

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}
```

**Let's break this down line by line:**

#### **Line 1: Import FastAPI**
```python
from fastapi import FastAPI
```
- Imports the `FastAPI` class
- This is the main class you'll use to create your API

#### **Line 3: Create FastAPI instance**
```python
app = FastAPI()
```
- `app` is your FastAPI application
- You can name it anything, but `app` is conventional
- This object will handle all your routes

#### **Line 5: Path Operation Decorator**
```python
@app.get("/")
```
- `@app.get()` is a **decorator** (we'll explain decorators soon)
- `get` = HTTP GET method
- `"/"` = the path/route/endpoint
- Together: "When someone makes a GET request to `/`, run this function"

#### **Line 6-7: Path Operation Function**
```python
def read_root():
    return {"message": "Hello World"}
```
- `read_root` = function name (can be anything)
- Returns a Python dictionary
- FastAPI automatically converts to JSON!

---

### **2.2 Running Your Application**

In terminal (with venv activated):

```cmd
uvicorn main:app --reload
```

**Breaking down this command:**
- `uvicorn` = The ASGI server
- `main` = The filename (main.py)
- `app` = The FastAPI instance inside main.py
- `--reload` = Auto-restart when code changes (development only!)

You'll see:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [12345] using StatReload
INFO:     Started server process [67890]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Your API is now running!**

---

### **2.3 Testing Your First Endpoint**

#### **Method 1: Browser**
Open your browser and go to:
```
http://127.0.0.1:8000
```

You'll see:
```json
{"message": "Hello World"}
```

#### **Method 2: Thunder Client (in VS Code)**
1. Click Thunder Client icon in VS Code
2. Click "New Request"
3. Enter URL: `http://127.0.0.1:8000`
4. Method: GET
5. Click "Send"

#### **Method 3: Command Line (curl)**
```cmd
curl http://127.0.0.1:8000
```

All three methods should return the same JSON!

---

### **2.4 Automatic Documentation**

This is where FastAPI shines!

#### **Swagger UI**
Go to: `http://127.0.0.1:8000/docs`

You'll see:
- Interactive API documentation
- List of all endpoints
- Try endpoints directly in browser
- Request/response examples

**Try it:**
1. Click on `GET /`
2. Click "Try it out"
3. Click "Execute"
4. See the response!

#### **ReDoc**
Go to: `http://127.0.0.1:8000/redoc`

Alternative documentation style:
- Cleaner, more organized
- Better for reading
- Not interactive (read-only)

#### **OpenAPI Schema**
Go to: `http://127.0.0.1:8000/openapi.json`

The raw OpenAPI specification:
- JSON format
- Used by tools to generate clients
- Industry standard

**You wrote 7 lines of code and got 3 documentation pages for free!**

---

### **2.5 Understanding Python Decorators**

Before we continue, let's understand decorators:

#### **What is a Decorator?**

A decorator is a function that modifies another function.

**Analogy:** Think of gift wrapping:
- Original item = function
- Wrapping paper = decorator
- Wrapped item = modified function

#### **Simple Example**

```python
# Without decorator
def say_hello():
    return "Hello"

result = say_hello()
print(result)  # Hello
```

```python
# Creating a decorator
def make_bold(func):
    def wrapper():
        result = func()
        return f"<b>{result}</b>"
    return wrapper

# Using the decorator
@make_bold
def say_hello():
    return "Hello"

result = say_hello()
print(result)  # <b>Hello</b>
```

**What happened?**
1. `@make_bold` decorates `say_hello`
2. Now `say_hello` is wrapped with bold tags
3. Original function modified without changing its code!

#### **FastAPI Decorators**

```python
@app.get("/")
def read_root():
    return {"message": "Hello"}
```

**This means:**
```python
# FastAPI does this internally:
def get_decorator(path):
    def decorator(func):
        # Register this function to handle GET requests to path
        app.add_route(path, func, methods=["GET"])
        return func
    return decorator

# Your code
@app.get("/")  # Calls get_decorator("/")
def read_root():
    return {"message": "Hello"}
```

**In simple terms:**
- `@app.get("/")` tells FastAPI: "When GET request comes to `/`, call this function"
- The decorator registers your function with the FastAPI app

---

### **2.6 Adding More Endpoints**

Let's expand our `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to my API"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {
        "app": "My First FastAPI App",
        "version": "1.0.0",
        "author": "Your Name"
    }

@app.get("/status")
def status():
    return {
        "status": "active",
        "uptime": "24 hours"
    }
```

Save the file. With `--reload`, the server restarts automatically!

Test each endpoint:
- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/hello`
- `http://127.0.0.1:8000/about`
- `http://127.0.0.1:8000/status`

Check `/docs` - all endpoints are automatically documented!

---

## **PART 3: Path Operations Deep Dive** {#part-3-path-operations}

### **3.1 Path Parameters**

#### **What are Path Parameters?**

Variables in the URL path that capture dynamic values.

**Example:** `/users/123` where `123` is the user ID

#### **Basic Path Parameters**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
```

**Test it:**
- `GET /users/123` → `{"user_id": 123}`
- `GET /users/456` → `{"user_id": 456}`

**Key points:**
- `{user_id}` in path = path parameter
- `user_id: int` = automatic type conversion!
- FastAPI converts string from URL to int

#### **Type Validation**

```python
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
```

Try: `GET /users/abc`

You'll get:
```json
{
  "detail": [
    {
      "loc": ["path", "user_id"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

**FastAPI automatically validates that user_id is an integer!**

#### **Multiple Path Parameters**

```python
@app.get("/users/{user_id}/posts/{post_id}")
def read_user_post(user_id: int, post_id: int):
    return {
        "user_id": user_id,
        "post_id": post_id
    }
```

Test: `GET /users/5/posts/42`
```json
{
  "user_id": 5,
  "post_id": 42
}
```

#### **String Path Parameters**

```python
@app.get("/items/{item_name}")
def read_item(item_name: str):
    return {"item_name": item_name}
```

Test: `GET /items/laptop`
```json
{
  "item_name": "laptop"
}
```

#### **Path Parameter Order Matters!**

```python
# ❌ WRONG - This won't work as expected
@app.get("/users/me")
def read_current_user():
    return {"user": "current user"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
```

**Problem:** `GET /users/me` will match `users/{user_id}` first!

**Solution:** Put specific paths before dynamic ones:

```python
# ✅ CORRECT
@app.get("/users/me")
def read_current_user():
    return {"user": "current user"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}
```

**Rule:** Most specific → Least specific

---

### **3.2 Query Parameters**

#### **What are Query Parameters?**

Key-value pairs after `?` in URL.

**Example:** `/items?skip=0&limit=10`

#### **Basic Query Parameters**

```python
@app.get("/items")
def read_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit
    }
```

**Test:**
- `GET /items` → `{"skip": 0, "limit": 10}` (uses defaults)
- `GET /items?skip=5` → `{"skip": 5, "limit": 10}`
- `GET /items?skip=5&limit=20` → `{"skip": 5, "limit": 20}`

**Key points:**
- Function parameters NOT in path = query parameters
- `= 0` and `= 10` are default values
- Query parameters are optional if they have defaults

#### **Required Query Parameters**

```python
@app.get("/search")
def search(q: str):
    return {"query": q}
```

**No default value = required!**

Test:
- `GET /search` → **ERROR** (422 Unprocessable Entity)
- `GET /search?q=fastapi` → `{"query": "fastapi"}` ✅

#### **Optional Query Parameters**

```python
from typing import Optional

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
```

**Test:**
- `GET /items/5` → `{"item_id": 5}`
- `GET /items/5?q=search` → `{"item_id": 5, "q": "search"}`

#### **Multiple Query Parameters**

```python
@app.get("/products")
def read_products(
    skip: int = 0,
    limit: int = 10,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
):
    return {
        "skip": skip,
        "limit": limit,
        "category": category,
        "min_price": min_price,
        "max_price": max_price
    }
```

**Test:**
```
GET /products?category=electronics&min_price=100&max_price=1000&skip=0&limit=20
```

Response:
```json
{
  "skip": 0,
  "limit": 20,
  "category": "electronics",
  "min_price": 100.0,
  "max_price": 1000.0
}
```

#### **Boolean Query Parameters**

```python
@app.get("/items")
def read_items(available: bool = True):
    return {"available": available}
```

**Test:**
- `GET /items?available=true` → `{"available": true}`
- `GET /items?available=false` → `{"available": false}`
- `GET /items?available=1` → `{"available": true}`
- `GET /items?available=0` → `{"available": false}`

FastAPI recognizes:
- `true`, `True`, `1`, `yes`, `on` → `True`
- `false`, `False`, `0`, `no`, `off` → `False`

---

### **3.3 Request Body (POST, PUT, PATCH)**

#### **What is a Request Body?**

Data sent in the body of HTTP request (not in URL).

**Used with:** POST, PUT, PATCH (usually not with GET)

#### **Simple Request Body Example**

First, let's do it the basic way:

```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items")
def create_item(name: str, price: float, description: str = None):
    return {
        "name": name,
        "price": price,
        "description": description
    }
```

**Test with Thunder Client:**
1. Method: POST
2. URL: `http://127.0.0.1:8000/items`
3. Body → JSON:
```json
{
  "name": "Laptop",
  "price": 50000.99,
  "description": "Gaming laptop"
}
```

**But there's a better way using Pydantic!** (Next section)

---

### **3.4 Combining Path, Query, and Body Parameters**

```python
from typing import Optional

@app.put("/items/{item_id}")
def update_item(
    item_id: int,              # Path parameter
    name: str,                 # Body parameter
    price: float,              # Body parameter
    is_offer: Optional[bool] = None  # Query parameter
):
    return {
        "item_id": item_id,
        "name": name,
        "price": price,
        "is_offer": is_offer
    }
```

**Test:**
```
PUT /items/5?is_offer=true
Body:
{
  "name": "Updated Item",
  "price": 99.99
}
```

**FastAPI automatically knows:**
- `item_id` from path
- `name` and `price` from body
- `is_offer` from query

---

## **PART 4: Pydantic Models & Validation** {#part-4-pydantic}

### **4.1 What is Pydantic?**

**Pydantic** is a data validation library that uses Python type hints.

**Why Pydantic?**
- ✅ Automatic validation
- ✅ Clear error messages
- ✅ Type safety
- ✅ JSON serialization
- ✅ Editor autocomplete

**FastAPI is built on top of Pydantic!**

---

### **4.2 Creating Your First Pydantic Model**

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the model
class Item(BaseModel):
    name: str
    price: float
    description: str = None
    tax: float = None

@app.post("/items")
def create_item(item: Item):
    return item
```

**Let's break this down:**

#### **Line 2: Import BaseModel**
```python
from pydantic import BaseModel
```
All Pydantic models inherit from `BaseModel`

#### **Lines 6-10: Define Model**
```python
class Item(BaseModel):
    name: str
    price: float
    description: str = None
    tax: float = None
```

**This defines:**
- `name` is required, must be string
- `price` is required, must be float
- `description` is optional (default: None)
- `tax` is optional (default: None)

#### **Line 13: Use Model as Type**
```python
def create_item(item: Item):
```

FastAPI will:
1. Read request body
2. Validate against Item model
3. Convert to Item instance
4. Pass to function

**Test it:**

**Valid request:**
```json
{
  "name": "Laptop",
  "price": 50000.99
}
```
✅ Success!

**Invalid request (missing required field):**
```json
{
  "name": "Laptop"
}
```
❌ Error: `field required`

**Invalid request (wrong type):**
```json
{
  "name": "Laptop",
  "price": "expensive"
}
```
❌ Error: `value is not a valid float`

---

### **4.3 Pydantic Field Validation**

Pydantic provides `Field` for advanced validation:

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: float = Field(..., gt=0)
    description: str = Field(None, max_length=500)
    quantity: int = Field(1, ge=1, le=1000)
```

**Field parameters:**
- `...` = Required (Ellipsis means no default)
- `min_length`, `max_length` = String length
- `gt` = Greater than
- `ge` = Greater than or equal
- `lt` = Less than
- `le` = Less than or equal

**Examples:**

**Valid:**
```json
{
  "name": "Laptop",
  "price": 50000.99,
  "quantity": 5
}
```
✅ Success

**Invalid (name too short):**
```json
{
  "name": "PC",
  "price": 50000.99
}
```
❌ Error: `ensure this value has at least 3 characters`

**Invalid (price not > 0):**
```json
{
  "name": "Laptop",
  "price": 0
}
```
❌ Error: `ensure this value is greater than 0`

---

### **4.4 Nested Pydantic Models**

Models can contain other models!

```python
from pydantic import BaseModel, Field
from typing import Optional

class Address(BaseModel):
    street: str
    city: str
    country: str
    postal_code: str

class User(BaseModel):
    username: str = Field(..., min_length=3)
    email: str
    age: int = Field(..., ge=0, le=120)
    address: Address
    bio: Optional[str] = None

@app.post("/users")
def create_user(user: User):
    return user
```

**Test:**
```json
{
  "username": "ali_khan",
  "email": "ali@example.com",
  "age": 22,
  "address": {
    "street": "123 Main St",
    "city": "Peshawar",
    "country": "Pakistan",
    "postal_code": "25000"
  },
  "bio": "Student at UET Peshawar"
}
```

**Access nested data:**
```python
@app.post("/users")
def create_user(user: User):
    return {
        "username": user.username,
        "city": user.address.city,
        "country": user.address.country
    }
```

---

### **4.5 Lists in Pydantic Models**

```python
from typing import List
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

class Order(BaseModel):
    order_id: int
    items: List[Item]
    total: float

@app.post("/orders")
def create_order(order: Order):
    return order
```

**Test:**
```json
{
  "order_id": 123,
  "items": [
    {
      "name": "Laptop",
      "price": 50000
    },
    {
      "name": "Mouse",
      "price": 500
    }
  ],
  "total": 50500
}
```

---

### **4.6 Email Validation**

```python
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    email: EmailStr  # Special email validator

@app.post("/users")
def create_user(user: User):
    return user
```

**Note:** You need to install:
```cmd
pip install pydantic[email]
```

**Test:**

**Valid:**
```json
{
  "username": "ali",
  "email": "ali@example.com"
}
```
✅ Success

**Invalid:**
```json
{
  "username": "ali",
  "email": "not-an-email"
}
```
❌ Error: `value is not a valid email address`

---

### **4.7 Custom Validators**

Create your own validation logic:

```python
from pydantic import BaseModel, validator

class User(BaseModel):
    username: str
    password: str
    
    @validator('username')
    def username_alphanumeric(cls, v):
        if not v.isalnum():
            raise ValueError('must be alphanumeric')
        return v
    
    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('must be at least 8 characters')
        if not any(c.isupper() for c in v):
            raise ValueError('must contain uppercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('must contain digit')
        return v

@app.post("/register")
def register(user: User):
    return {"message": "User registered"}
```

**Test:**

**Invalid username:**
```json
{
  "username": "ali_khan",
  "password": "Password123"
}
```
❌ Error: `must be alphanumeric`

**Weak password:**
```json
{
  "username": "alikhan",
  "password": "weak"
}
```
❌ Error: `must be at least 8 characters`

**Valid:**
```json
{
  "username": "alikhan",
  "password": "SecurePass123"
}
```
✅ Success

---

### **4.8 Model Config and Examples**

Add examples to your models for better documentation:

```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., example="Laptop")
    price: float = Field(..., example=50000.99)
    description: str = Field(None, example="Gaming laptop")
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Gaming Laptop",
                "price": 75000.00,
                "description": "High-performance gaming laptop"
            }
        }

@app.post("/items")
def create_item(item: Item):
    return item
```

Now in `/docs`, you'll see example values pre-filled!

---

## **PART 5: Response Models & Error Handling** {#part-5-responses}

### **5.1 Response Models**

Control what data is returned to the client.

#### **Basic Response Model**

```python
from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str
    email: str

class UserOut(BaseModel):
    username: str
    email: str
    # Note: password is NOT here!

@app.post("/users", response_model=UserOut)
def create_user(user: UserIn):
    # In real app, you'd save to database
    return user
```

**Test:**
```json
{
  "username": "ali",
  "password": "secret123",
  "email": "ali@example.com"
}
```

**Response:**
```json
{
  "username": "ali",
  "email": "ali@example.com"
}
```

**Password is filtered out automatically!**

---

### **5.2 Response Status Codes**

```python
from fastapi import FastAPI, status

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return user

@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    return None
```

**Available status codes:**
- `status.HTTP_200_OK`
- `status.HTTP_201_CREATED`
- `status.HTTP_204_NO_CONTENT`
- `status.HTTP_400_BAD_REQUEST`
- `status.HTTP_404_NOT_FOUND`
- etc.

---

### **5.3 HTTPException - Error Handling**

#### **Raising Exceptions**

```python
from fastapi import FastAPI, HTTPException

# Fake database
fake_db = {
    1: {"name": "Ali", "email": "ali@example.com"},
    2: {"name": "Sara", "email": "sara@example.com"}
}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return fake_db[user_id]
```

**Test:**
- `GET /users/1` → `{"name": "Ali", "email": "ali@example.com"}` ✅
- `GET /users/999` → `{"detail": "User not found"}` with 404 status ❌

---

#### **Custom Error Details**

```python
@app.get("/users/{user_id}")
def read_user(user_id: int):
    if user_id not in fake_db:
        raise HTTPException(
            status_code=404,
            detail={
                "error": "User not found",
                "user_id": user_id,
                "suggestion": "Check the user ID and try again"
            }
        )
    return fake_db[user_id]
```

**Response for invalid ID:**
```json
{
  "detail": {
    "error": "User not found",
    "user_id": 999,
    "suggestion": "Check the user ID and try again"
  }
}
```

---

#### **Different Error Scenarios**

```python
from fastapi import FastAPI, HTTPException, status

@app.post("/users")
def create_user(user: User):
    # Check if username already exists
    if user.username in existing_usernames:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already taken"
        )
    
    # Check if user is underage
    if user.age < 18:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Must be 18 or older to register"
        )
    
    # Success
    return {"message": "User created"}
```

---

### **5.4 Response Model with Status Codes**

```python
from typing import List

class User(BaseModel):
    id: int
    username: str
    email: str

@app.get("/users", response_model=List[User])
def get_users():
    return [
        {"id": 1, "username": "ali", "email": "ali@example.com"},
        {"id": 2, "username": "sara", "email": "sara@example.com"}
    ]

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return user
```

---

### **5.5 Excluding Fields from Response**

```python
class User(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool = True

@app.post("/users", response_model=User, response_model_exclude={"password"})
def create_user(user: User):
    return user
```

**Alternative:**
```python
@app.post("/users", response_model=User, response_model_exclude_unset=True)
def create_user(user: User):
    return user
```

This excludes fields that weren't explicitly set.

---

## **PART 6: First Project - Simple Blog API** {#part-6-project}

### **6.1 Project Overview**

We'll build a simple blog API with:
- Create posts
- Read all posts
- Read single post
- Update post
- Delete post

**Features:**
- In-memory storage (Python list)
- Pydantic validation
- Proper error handling
- Status codes

---

### **6.2 Complete Blog API Code**

Create `blog_api.py`:

```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Simple Blog API",
    description="A simple blog API built with FastAPI",
    version="1.0.0"
)

# Pydantic Models
class PostBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1, max_length=50)

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    content: Optional[str] = Field(None, min_length=1)
    author: Optional[str] = Field(None, min_length=1, max_length=50)

class Post(PostBase):
    id: int
    
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "My First Blog Post",
                "content": "This is the content of my first post",
                "author": "Ali Khan"
            }
        }

# In-memory database (list of posts)
posts_db: List[Post] = []
post_id_counter = 1

# API Endpoints

@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {
        "message": "Welcome to Simple Blog API",
        "endpoints": {
            "docs": "/docs",
            "posts": "/posts"
        }
    }

@app.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED)
def create_post(post: PostCreate):
    """Create a new blog post"""
    global post_id_counter
    
    new_post = Post(
        id=post_id_counter,
        title=post.title,
        content=post.content,
        author=post.author
    )
    
    posts_db.append(new_post)
    post_id_counter += 1
    
    return new_post

@app.get("/posts", response_model=List[Post])
def get_all_posts(skip: int = 0, limit: int = 10):
    """Get all blog posts with pagination"""
    return posts_db[skip : skip + limit]

@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    """Get a single post by ID"""
    for post in posts_db:
        if post.id == post_id:
            return post
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with ID {post_id} not found"
    )

@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post_update: PostUpdate):
    """Update a post (full replacement)"""
    for index, post in enumerate(posts_db):
        if post.id == post_id:
            # Create updated post
            updated_post = Post(
                id=post_id,
                title=post_update.title if post_update.title else post.title,
                content=post_update.content if post_update.content else post.content,
                author=post_update.author if post_update.author else post.author
            )
            posts_db[index] = updated_post
            return updated_post
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with ID {post_id} not found"
    )

@app.patch("/posts/{post_id}", response_model=Post)
def partial_update_post(post_id: int, post_update: PostUpdate):
    """Partially update a post"""
    for index, post in enumerate(posts_db):
        if post.id == post_id:
            # Update only provided fields
            update_data = post_update.dict(exclude_unset=True)
            updated_post = post.copy(update=update_data)
            posts_db[index] = updated_post
            return updated_post
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with ID {post_id} not found"
    )

@app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    """Delete a post"""
    for index, post in enumerate(posts_db):
        if post.id == post_id:
            posts_db.pop(index)
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Post with ID {post_id} not found"
    )

@app.get("/posts/author/{author_name}", response_model=List[Post])
def get_posts_by_author(author_name: str):
    """Get all posts by a specific author"""
    author_posts = [post for post in posts_db if post.author == author_name]
    
    if not author_posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No posts found by author '{author_name}'"
        )
    
    return author_posts

@app.get("/stats")
def get_stats():
    """Get blog statistics"""
    authors = list(set(post.author for post in posts_db))
    
    return {
        "total_posts": len(posts_db),
        "total_authors": len(authors),
        "authors": authors
    }
```

---

### **6.3 Running the Blog API**

```cmd
uvicorn blog_api:app --reload
```

Visit: `http://127.0.0.1:8000/docs`

---

### **6.4 Testing the Blog API**

#### **1. Create a Post**
```
POST /posts
Body:
{
  "title": "Learning FastAPI",
  "content": "FastAPI is an amazing framework for building APIs!",
  "author": "Ali Khan"
}
```

Response (201 Created):
```json
{
  "id": 1,
  "title": "Learning FastAPI",
  "content": "FastAPI is an amazing framework for building APIs!",
  "author": "Ali Khan"
}
```

#### **2. Create More Posts**
```
POST /posts
{
  "title": "Python Tips",
  "content": "Here are some Python tips...",
  "author": "Ali Khan"
}

POST /posts
{
  "title": "Web Development",
  "content": "Web dev is fun!",
  "author": "Sara Ahmed"
}
```

#### **3. Get All Posts**
```
GET /posts
```

Response:
```json
[
  {
    "id": 1,
    "title": "Learning FastAPI",
    "content": "FastAPI is an amazing framework for building APIs!",
    "author": "Ali Khan"
  },
  {
    "id": 2,
    "title": "Python Tips",
    "content": "Here are some Python tips...",
    "author": "Ali Khan"
  },
  {
    "id": 3,
    "title": "Web Development",
    "content": "Web dev is fun!",
    "author": "Sara Ahmed"
  }
]
```

#### **4. Get Single Post**
```
GET /posts/1
```

Response:
```json
{
  "id": 1,
  "title": "Learning FastAPI",
  "content": "FastAPI is an amazing framework for building APIs!",
  "author": "Ali Khan"
}
```

#### **5. Update Post (PUT)**
```
PUT /posts/1
{
  "title": "Learning FastAPI - Updated",
  "content": "FastAPI is the best framework!",
  "author": "Ali Khan"
}
```

#### **6. Partial Update (PATCH)**
```
PATCH /posts/1
{
  "title": "New Title Only"
}
```

Only title changes, content and author remain the same!

#### **7. Get Posts by Author**
```
GET /posts/author/Ali Khan
```

Returns all posts by Ali Khan.

#### **8. Get Statistics**
```
GET /stats
```

Response:
```json
{
  "total_posts": 3,
  "total_authors": 2,
  "authors": ["Ali Khan", "Sara Ahmed"]
}
```

#### **9. Delete Post**
```
DELETE /posts/1
```

Response: 204 No Content (empty body)

#### **10. Try to Get Deleted Post**
```
GET /posts/1
```

Response (404):
```json
{
  "detail": "Post with ID 1 not found"
}
```

---

### **6.5 Code Explanation**

#### **Global Variables**
```python
posts_db: List[Post] = []
post_id_counter = 1
```
- `posts_db`: In-memory storage (list)
- `post_id_counter`: Auto-increment ID

#### **Three Pydantic Models**
```python
PostBase → Common fields
PostCreate → For creating (inherits PostBase)
PostUpdate → For updating (all fields optional)
Post → Complete post with ID
```

#### **CRUD Operations**
- **Create:** `POST /posts`
- **Read:** `GET /posts` and `GET /posts/{post_id}`
- **Update:** `PUT` (full) and `PATCH` (partial)
- **Delete:** `DELETE /posts/{post_id}`

#### **Error Handling**
```python
if post_id not in posts_db:
    raise HTTPException(status_code=404, detail="Not found")
```

#### **Pagination**
```python
def get_all_posts(skip: int = 0, limit: int = 10):
    return posts_db[skip : skip + limit]
```

---

### **6.6 Improvements You Can Make**

1. **Add timestamps:**
```python
from datetime import datetime

class Post(PostBase):
    id: int
    created_at: datetime
    updated_at: datetime
```

2. **Add tags:**
```python
class Post(PostBase):
    id: int
    tags: List[str] = []
```

3. **Search functionality:**
```python
@app.get("/posts/search")
def search_posts(q: str):
    results = [p for p in posts_db if q.lower() in p.title.lower()]
    return results
```

4. **Sorting:**
```python
@app.get("/posts")
def get_posts(sort_by: str = "id", order: str = "asc"):
    # Sort logic here
    pass
```

---

## **Summary & Next Steps** {#summary}

### **What You've Learned**

✅ **Environment Setup**
- Virtual environments
- Installing FastAPI and Uvicorn
- VS Code configuration

✅ **FastAPI Basics**
- Creating FastAPI app
- Path operations (@app.get, @app.post, etc.)
- Running with Uvicorn
- Automatic documentation

✅ **Path Operations**
- Path parameters
- Query parameters
- Request body
- Combining all three

✅ **Pydantic Models**
- Creating models
- Field validation
- Nested models
- Custom validators
- Email validation

✅ **Response & Errors**
- Response models
- Status codes
- HTTPException
- Error handling

✅ **Complete Project**
- Built a full blog API
- CRUD operations
- Validation
- Error handling

---

### **Quick Reference**

#### **Basic FastAPI App**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

#### **Path Parameter**
```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```

#### **Query Parameter**
```python
@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}
```

#### **Request Body with Pydantic**
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item
```

#### **Error Handling**
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id not in database:
        raise HTTPException(status_code=404, detail="Not found")
    return database[item_id]
```

---

### **Self-Assessment Quiz**

#### **1. What command runs FastAPI with auto-reload?**
a) `python main.py`  
b) `fastapi run main.py`  
c) `uvicorn main:app --reload`  
d) `flask run`  

**Answer:** c

#### **2. What's the difference between path and query parameters?**
Path: In URL path like `/users/123`
Query: After `?` like `/users?id=123`

#### **3. What does `response_model` do?**
Filters and validates response data based on Pydantic model

#### **4. When should you use POST vs PUT?**
POST: Create new resource
PUT: Replace entire existing resource

#### **5. What's the purpose of Pydantic's `Field`?**
Add validation constraints (min_length, max_length, gt, etc.)

---

### **Common Mistakes to Avoid**

❌ Forgetting to activate virtual environment
❌ Not using type hints
❌ Returning `None` when you should return data
❌ Forgetting `...` for required Pydantic fields
❌ Using mutable default arguments
❌ Not handling 404 errors
❌ Mixing sync and async incorrectly

---

### **Practice Exercises**

Before moving to Phase 3, build these:

**Exercise 1: Todo API**
```
POST   /todos          Create todo
GET    /todos          List all todos
GET    /todos/{id}     Get single todo
PATCH  /todos/{id}     Mark as complete
DELETE /todos/{id}     Delete todo
```

**Exercise 2: Contact Book API**
```
POST   /contacts       Add contact
GET    /contacts       List contacts
GET    /contacts/{id}  Get contact
PUT    /contacts/{id}  Update contact
DELETE /contacts/{id}  Delete contact
GET    /contacts/search?q=name  Search contacts
```

**Exercise 3: Product Inventory**
```
POST   /products       Add product
GET    /products       List products (with filters)
GET    /products/{id}  Get product
PATCH  /products/{id}  Update stock
DELETE /products/{id}  Delete product
GET    /products/low-stock  Get low stock items
```

---

### **Resources**

**Official Documentation:**
- FastAPI: https://fastapi.tiangolo.com
- Pydantic: https://docs.pydantic.dev
- Uvicorn: https://www.uvicorn.org

**Practice:**
- Build small APIs daily
- Read FastAPI source code
- Study other people's FastAPI projects on GitHub

**Next Phase Preview:**

In **Phase 3: Intermediate FastAPI**, you'll learn:
- File uploads
- Form data
- Headers and cookies
- Dependency injection
- Authentication (JWT)
- Middleware
- CORS

---

### **Final Tips**

1. **Practice daily** - Build something every day
2. **Read error messages carefully** - They're very informative
3. **Use `/docs`** - Test your API as you build
4. **Write clean code** - Use proper naming and structure
5. **Comment your code** - Future you will thank you

**You've completed Phase 2! 🎉**

You now have a solid foundation in FastAPI basics. Make sure you:
- ✅ Built the blog API
- ✅ Understand all concepts
- ✅ Completed practice exercises
- ✅ Feel comfortable creating simple APIs

**When ready, move to Phase 3 for intermediate topics!**

---

*Created for BSCS 3rd Year Students | Windows 11 | Beginner to Advanced*
