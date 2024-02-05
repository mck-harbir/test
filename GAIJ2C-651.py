import datetime
import logging
from typing import Any, Dict, List, Optional



"""
This is a class representing a JiraAccount object. It contains attributes such as id, name, username, password, url, token, refresh_token, expires_at, created_at, updated_at, deleted_at, and is_active.

Attributes:
    id (int): The unique ID of the JiraAccount object.
    name (str): The name of the JiraAccount object.
    username (str): The username used to authenticate with Jira.
    password (str): The password used to authenticate with Jira.
    url (str): The URL of the Jira server.
    token (str): The OAuth2 access token.
    refresh_token (str): The OAuth2 refresh token.
    expires_at (datetime.datetime): The expiration date/time of the access token.
    created_at (datetime.datetime): The creation date/time of the JiraAccount object.
    updated_at (datetime.datetime): The last update date/time of the JiraAccount object.
    deleted_at (Optional[datetime.datetime]): The deletion date/time of the JiraAccount object.
    is_active (bool): Whether the JiraAccount object is active or not.
"""
class JiraAccount(BaseModel):
    id: int
    name: str
    username: str
    password: str
    url: str
    token: str
    refresh_token: str
    expires_at: datetime.datetime
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: Optional[datetime.datetime] = None
    is_active: bool

    @validator('expires_at', always=True)
    def set_expires_at(cls, v, values):
        if 'created_at' in values and isinstance(values['created_at'], datetime.datetime):
            return values['created_at'] + timedelta(seconds=v)
        else:
            raise ValueError("JiraAccount.expires_at must be provided when creating a new JiraAccount.")