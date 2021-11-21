import os.path

from ariadne import load_schema_from_path

__all__ = ("type_defs",)


curr_dir = os.path.dirname(os.path.realpath(__file__))
schema_file = os.path.join(curr_dir, "schema.graphql")
type_defs = load_schema_from_path(schema_file)
