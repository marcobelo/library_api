from fastapi_pagination import Page
from pydantic import Field

from src.config.environemnt import env

PaginateOutput = Page.with_custom_options(size=Field(env.page_size, ge=env.page_min_size, le=env.page_max_size))
