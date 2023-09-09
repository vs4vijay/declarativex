from typing import List, Optional, Union

from src.declarativex import (
    BaseClient,
    declare,
    Path,
    Query,
    BodyField,
    Json,
)
from tests.fixtures.models import BaseTodo, Comment, Todo, BaseTodoDataClass


class TodoClient(BaseClient):
    base_url = "https://jsonplaceholder.typicode.com"

    @declare("GET", "/todos/{id}")
    async def get_todo_by_id_raw(self, id: int) -> dict:
        ...  # pragma: no cover

    @declare("GET", "/todos/{id}")
    async def get_todo_by_id_pydantic(self, id: int = Path(...)) -> Todo:
        ...  # pragma: no cover

    @declare("GET", "/comments")
    async def get_comments_raw(
        self, post_id: int = Query(field_name="postId")
    ) -> List[dict]:
        ...  # pragma: no cover

    @declare("GET", "/comments")
    async def get_comments_pydantic(
        self, post_id: int = Query(field_name="postId")
    ) -> List[Comment]:
        ...  # pragma: no cover

    @declare("POST", "/posts")
    async def create_post(
        self,
        title: str = BodyField(...),
        body: str = BodyField(...),
        user_id: int = BodyField(field_name="userId"),
    ) -> dict:
        """
        It will produce a request:
        POST /posts
        {
            "title": "foo",
            "body": "bar",
            "userId": 1
        }
        """
        ...  # pragma: no cover

    @declare("POST", "/posts")
    async def misconfigured_create_post(
        self,
        body: Union[BaseTodo, dict] = Json(...),
    ) -> dict:
        ...  # pragma: no cover

    @declare("POST", "/posts")
    async def misconfigured_create_post_without_default(
        self,
        body: BaseTodo = Json(...),
    ) -> dict:
        ...  # pragma: no cover

    @declare("POST", "/posts")
    async def misconfigured_create_post_but_with_default(
        self,
        body: Union[BaseTodo, dict, None] = Json(default={"data": "test"}),
    ) -> dict:
        ...  # pragma: no cover

    @declare("POST", "/posts")
    async def create_post_pydantic(
        self,
        body: BaseTodo = Json(...),
    ) -> dict:
        ...  # pragma: no cover

    @declare("POST", "/posts")
    async def create_post_dataclass(
        self,
        body: BaseTodoDataClass = Json(...),
    ) -> dict:
        ...  # pragma: no cover

    @declare("PATCH", "/posts/{postId}")
    async def update_post_mixed(
        self,
        post_id: int = Path(field_name="postId"),
        body: dict = Json(...),
        user_id: int = BodyField(field_name="userId"),
    ) -> dict:
        ...  # pragma: no cover

    @declare("PUT", "/posts/{postId}")
    async def update_post(
        self, post_id: int = Path(field_name="postId"), body: dict = Json(...)
    ) -> dict:
        ...  # pragma: no cover

    @declare("DELETE", "/posts/{postId}")
    async def delete_post(
        self, post_id: int = Path(field_name="postId")
    ) -> dict:
        ...  # pragma: no cover


class SlowClient(BaseClient):
    base_url = "https://httpbin.org"

    @declare("GET", "/delay/{delay}", timeout=2)
    def get_data_from_slow_endpoint(
        self, delay: int, query_delay: Optional[int]
    ) -> dict:
        ...  # pragma: no cover

    @declare("GET", "/delay/{delay}", timeout=1)
    async def async_get_data_from_slow_endpoint(
        self,
        delay: int = Path(...),
        query_delay: Optional[int] = Query(field_name="delay"),
    ) -> dict:
        ...  # pragma: no cover


@declare("GET", "/todos/{id}", base_url="https://jsonplaceholder.typicode.com")
async def get_todo_by_id_raw(id: int) -> dict:
    ...  # pragma: no cover


@declare("GET", "/todos/{id}", base_url="https://jsonplaceholder.typicode.com")
def sync_get_todo_by_id_raw(id: int) -> Todo:
    ...  # pragma: no cover
