import datetime
import logging
from typing import Any, Dict, List, Optional



"""
This is a class representing a JiraAccount object. It contains attributes such as id, name, username, password, url, token, refresh_token, expires_at, created_at, updated_at, deleted_at, and is_active.

Attributes:
    id (int): The unique identifier of this JiraAccount object.
    name (str): The display name of this JiraAccount object.
    username (str): The username used to authenticate with Jira.
    password (str): The password used to authenticate with Jira.
    url (str): The URL of the Jira server.
    token (str): The OAuth2 access token.
    refresh_token (str): The OAuth2 refresh token.
    expires_at (datetime.datetime): The expiration date/time of the access token.
    created_at (datetime.datetime): The creation date/time of this JiraAccount object.
    updated_at (datetime.datetime): The last update date/time of this JiraAccount object.
    deleted_at (Optional[datetime.datetime]): The deletion date/time of this JiraAccount object.
    is_active (bool): Whether this JiraAccount object is active or not.
"""
class JiraAccount(BaseModel):
    id: int = Field(..., alias='_id')  # type: ignore
    name: str
    username: str
    password: str
    url: str
    token: str
    refresh_token: str
    expires_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime]
    is_active: bool

    @validator('expires_at', pre=True)
    def _parse_date(cls, v: Any) -> datetime.datetime:
        if isinstance(v, str):
            return parse_datetime(v)
        else:
            raise ValueError()