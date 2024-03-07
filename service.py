from requests import HTTPError, get
import random
import os
from dotenv import load_dotenv

load_dotenv()

api_url = os.getenv("CHARACTERS_API_URL")
api_key = os.getenv("CHARACTERS_API_KEY")
characters_list_api_url = os.getenv("CHARACTERS_LIST_URL")

url = f"{api_url}{api_key}/"


def get_ids_of_characters(number_of_characters: int) -> list[str]:
    try:
        response = get(characters_list_api_url)
        response.raise_for_status()
        character_ids = random.sample(
            [character["id"] for character in response.json()],
            number_of_characters,
        )
        return character_ids
    except HTTPError as error:
        print("An error has occurred fetching characters list", error)


def get_characters_info(number_of_characters: int) -> dict:
    try:
        characters_ids = get_ids_of_characters(number_of_characters)
        characters_info = []
        for character_id in characters_ids:
            response = get(f"{url}{character_id}")
            response.raise_for_status()
            data = response.json()
            characters_info.append(
                {
                    "id": data["id"],
                    "name": data["name"],
                    "alignment": data["biography"]["alignment"],
                    "powerstats": data["powerstats"],
                }
            )
        return characters_info
    except HTTPError as error:
        print("An error has occurred fetching character info", error)
