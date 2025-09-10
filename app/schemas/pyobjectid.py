from typing import Any
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        from pydantic_core import core_schema

        def validate_objectid(v, field):
            if not ObjectId.is_valid(v):
                raise ValueError("Invalid ObjectId")
            return ObjectId(v)

        def serialize_objectid(v):
            return str(v)

        return core_schema.json_or_python_schema(
            python_schema=core_schema.with_info_plain_validator_function(validate_objectid),
            json_schema=core_schema.str_schema(),
            serialization=core_schema.plain_serializer_function_ser_schema(serialize_objectid, when_used='json'),
        )