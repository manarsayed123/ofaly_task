from typing import Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from utility import translate_location, get_location_current_weather

app = FastAPI()


@app.get("/")
async def get_translated_weather(city: str, country: str, q: Optional[str] = None):
    translated_str = await translate_location(city, country)
    weather = await get_location_current_weather(f'{city},{country}')
    result = {'location_in_en': translated_str, 'weather': weather

              }
    return JSONResponse(content=result)
