import pytest
from ariadne import make_executable_schema
from ariadne import graphql_sync
from patient import errors
from unittest.mock import patch, Mock

from hypothesis import given
from hypothesis.strategies import integers


@patch("api.controller.patient_service")
def test__get_patient__responds_with_patient_if_exists(mock_patient_service, schema):
    mock_patient = Mock(first_name="Chris", last_name="Ramacciotti")
    mock_patient_service.get_patient_by_id.return_value = mock_patient
    query = f"""
        {{
            patient(id: 1) {{
                first_name
                last_name
           }}
        }}
    """
    data = {"query": query}
    success, response = graphql_sync(schema, data)

    assert success

    patient = response["data"]["patient"]
    assert patient["first_name"] == mock_patient.first_name
    assert patient["last_name"] == mock_patient.last_name


@patch("api.controller.patient_service")
def test__get_patient__responds_with_404_if_not_exists(mock_patient_service, schema):
    mock_patient_service.get_patient_by_id.side_effect = errors.PatientNotFound

    query = f"""
        {{
            patient(id: 1) {{
                first_name
                last_name
           }}
        }}
    """
    data = {"query": query}
    success, response = graphql_sync(schema, data)

    assert success
    assert response["data"]["patient"] is None


@pytest.fixture(scope="module")
def schema():
    from ..schema import type_defs
    from ..controller import resolvers

    return make_executable_schema(type_defs, *resolvers)
