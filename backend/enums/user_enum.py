from enum import Enum


class Status(str, Enum):
    active = "active"
    deleted = "deleted"
    banned = "banned"
