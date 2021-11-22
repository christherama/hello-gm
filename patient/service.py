from conf.db import Session
from patient import domain, errors, models
from sqlalchemy.exc import NoResultFound


def get_patient_by_id(id: int) -> domain.Patient:
    """
    Gets a patient by id
    :param id: Unique id of patient
    :return: domain.Patient representing the underlying patient retrieved

    :raises errors.PatientNotFound if no patient with the given id was found
    """
    session = Session()
    try:
        patient_model = (
            session.query(models.Patient).filter(models.Patient.id == id).one()
        )
    except NoResultFound:
        raise errors.PatientNotFound

    return _patient_from_model(patient_model)


def _patient_from_model(patient: models.Patient) -> domain.Patient:
    return domain.Patient(
        id=patient.id,
        first_name=patient.first_name,
        last_name=patient.last_name,
    )
