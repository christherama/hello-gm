from conf.db import Session
from patient import domain, models


def get_patient_by_id(id: int) -> domain.Patient:
    """
    Gets a patient by id
    :param id: Unique id of patient
    :return: domain.Patient representing the underlying patient retrieved
    """
    session = Session()
    patient_model = session.query(models.Patient).one()
    return _patient_from_model(patient_model)


def _patient_from_model(patient: models.Patient) -> domain.Patient:
    return domain.Patient(
        id=patient.id,
        first_name=patient.first_name,
        last_name=patient.last_name,
    )
