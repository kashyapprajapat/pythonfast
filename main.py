from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import random
from database import collection

app = FastAPI()

# Pydantic model for request body validation
class SaveRequest(BaseModel):
    name: str
    age: int


@app.get("/", response_class=HTMLResponse)
async def read_home():
    html_content = """
    <html>
        <head>
            <title>FastAPI MongoDB App</title>
        </head>
        <body>
            <h1>Welcome to the FastAPI MongoDB App</h1>
            <p>Use the following routes to interact with the app:</p>
            <ul>
                <li><strong>/saver</strong> (POST): Save data into the MongoDB database. Send a JSON body with "name" and "age".</li>
                <li><strong>/whoisfast</strong> (GET): Calculates the sum of numbers from 1 to 1,00,00,000 and returns the result.</li>
                <li><strong>/secondfast</strong> (GET): Calculates the sum of numbers from 1 to 10,00,00,000 and returns the result.</li>
            </ul>
            <p>Test the API endpoints using tools like <a href="https://www.postman.com/" target="_blank">Postman</a> or <a href="https://swagger.io/tools/swagger-ui/" target="_blank">Swagger UI</a>.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)



@app.post("/saver")
async def save_data(data: SaveRequest):
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    
    # Create a document to store in MongoDB
    document = {
        "name": data.name,
        "age": data.age,
        "random_number": random_number
    }
    
    # Insert the document into MongoDB
    result = await collection.insert_one(document)
    
    if result.acknowledged:
        return {
            "message": "Data saved successfully",
            "random_number": random_number
        }
    else:
        raise HTTPException(status_code=500, detail="Failed to save data")

# To run the server, use: uvicorn main:app --reload


@app.get("/whoisfast")
async def who_is_fast():
    total = sum(range(1, 100000001))  # Sum from 1 to 1,00,00,000
    return {"route": "whoisfast", "sum": total}

@app.get("/secondfast")
async def second_fast():
    total = sum(range(1, 1000000001))  # Sum from 1 to 10,00,00,000
    return {"route": "secondfast", "sum": total}
