from fastapi_pagination import Page
from pydantic import Field

# TODO: add pagination params from env
__page_size = 10
__minimum_size = 1
__maximum_size = 50
PaginateOutput = Page.with_custom_options(size=Field(__page_size, ge=__minimum_size, le=__maximum_size))
