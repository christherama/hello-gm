from ariadne import ObjectType, QueryType
from graphql import GraphQLResolveInfo
from patient import domain, service as patient_service

query = QueryType()


@query.field("patient")
def resolve_patient(*_, id: int):
    patient = patient_service.get_patient_by_id(id)
    return patient


patient = ObjectType("Patient")


@patient.field("first_name")
def resolve_first_name(patient: domain.Patient, info: GraphQLResolveInfo):
    return patient.first_name


@patient.field("last_name")
def resolve_last_name(patient: domain.Patient, info: GraphQLResolveInfo):
    return patient.last_name


resolvers = [
    query,
    patient,
]

