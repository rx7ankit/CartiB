from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from blinkit import blinkit_data
from swiggy import swiggy_data
from concurrent.futures import ThreadPoolExecutor

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Store user inputs temporarily
user_data = {"location": None, "stores": []}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/location", response_class=HTMLResponse)
async def location_page(request: Request):
    return templates.TemplateResponse("location.html", {"request": request})


@app.post("/location")
async def handle_location(
    location: str = Form(...), stores: list[str] = Form([])
):
    print(f"Location: {location}")
    print(f"Stores: {stores}")

    # Save data into user_data dictionary
    user_data["location"] = location
    user_data["stores"] = stores

    # Ensure location and at least one store are selected
    if not user_data["location"] or not user_data["stores"]:
        return RedirectResponse("/location", status_code=302)

    return RedirectResponse("/home", status_code=302)


product_name = ""


@app.get("/home", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request,
                      "user_data": user_data, "product_name": product_name}
    )


@app.post("/home")
async def search(request: Request, product: str = Form(...)):
    global product_name
    product_name = product  # Save the product name in the variable
    print(product_name)

    location = "indrapuri bhopal"

    # Execute tasks in parallel
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(blinkit_data, product_name, location)
        future2 = executor.submit(swiggy_data, product_name, location)
        
        # Collect results
        result1 = future1.result()
        result2 = future2.result()

    data = result1 + result2

    return templates.TemplateResponse(
        "home.html", {"request": request,
                      "user_data": user_data, "product_name": product_name, "blinkit_dta": data}
    )
