import pytest
from ariadne import make_executable_schema
from ariadne import graphql_sync
from unittest.mock import patch, Mock

from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=10000))
def test__get_patient__responds_with_patient_if_exists(schema, patient_id: int):
    with patch("api.controller.patient_service") as mock_patient_service:
        mock_patient = Mock(first_name="Chris", last_name="Ramacciotti")
        mock_patient_service.get_patient_by_id.return_value = mock_patient
        query = f"""
            {{
                patient(id: {patient_id}) {{
                    first_name
                    last_name
               }}
            }}
        """
        data = {
            "query": query
        }
        success, response = graphql_sync(schema, data)
    assert success


@pytest.fixture(scope="module")
def schema():
    from ..schema import type_defs
    from ..controller import resolvers

    return make_executable_schema(type_defs, *resolvers)

