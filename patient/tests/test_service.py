from unittest.mock import patch, Mock

from hypothesis import given
from hypothesis.strategies import integers

from patient import service, domain


@patch("patient.service.Session")
@given(integers(min_value=1))
def test__get_patient_by_id__returns_patient_if_exists(mock_session, patient_id: int):
    patient_model = Mock(
        id=patient_id,
        first_name="Chris",
        last_name="Ramacciotti",
    )
    mock_session.return_value.query.return_value.filter.return_value.one.return_value = patient_model
    patient = service.get_patient_by_id(patient_id)

    assert patient == domain.Patient(
        id=patient_id,
        first_name=patient_model.first_name,
        last_name=patient_model.last_name,
    )
