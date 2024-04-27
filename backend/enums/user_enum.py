import enum


class Status(str, enum.Enum):
    active = "active"
    deleted = "deleted"
    banned = "banned"
