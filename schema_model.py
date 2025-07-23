from pydantic import BaseModel, Field
from typing import List, Optional


class EnabledValidator(BaseModel):
    enabled: bool


class FieldValidator(BaseModel):
    required: Optional[EnabledValidator] = None
    unique: Optional[EnabledValidator] = None


class Metadata(BaseModel):
    change_id: Optional[str] = None
    release: Optional[str] = None
    versions_count: Optional[int] = None
    impact_title: Optional[str] = None
    change_source: Optional[str] = None
    type: Optional[str] = None


class FieldDefinition(BaseModel):
    name: str
    description: Optional[str] = None
    item_ref: Optional[str] = None
    type: Optional[str] = None
    primary_key: Optional[bool] = False
    foreign_key: Optional[str] = None
    validators: Optional[List[FieldValidator]] = []
    guidance: Optional[str] = None
    categories: Optional[List[str]] = []
    constraints: Optional[List[str]] = []
    returns: Optional[List[str]] = []
    cms: Optional[List[str]] = []
    cms_field: Optional[List[str]] = []
    cms_table: Optional[List[str]] = []
    metadata: Optional[Metadata] = None


class Node(BaseModel):
    name: str
    fields: List[FieldDefinition]


class NodeFile(BaseModel):
    nodes: List[Node]


class Relationship(BaseModel):
    parent_object: str
    parent_key: str
    child_object: str
    child_key: str
    relation: Optional[str] = "1:M"


class RelationshipFile(BaseModel):
    relationships: List[Relationship]
