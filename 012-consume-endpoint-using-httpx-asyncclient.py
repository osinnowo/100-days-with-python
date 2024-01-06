import asyncio
from dataclasses import dataclass
from http import HTTPStatus
from typing import Optional, List
import httpx


@dataclass
class Person:
    id: int
    name: int



class InternalServerException(Exception):
    def __init__(self, message):
        super().__init__(message)


async def consume() -> Optional[List[Person]]:
    async with httpx.AsyncClient() as httpClient:
        response = await httpClient.get("https://jsonplaceholder.typicode.com/users")
        if response.status_code == HTTPStatus.OK:
            people = [Person(id=person["id"], name=person["name"]) for person in response.json()]
            print(len(people))
            print(people)
            return people
        else:
            raise InternalServerException("Something went wrong!")
    return None


asyncio.run(consume())
