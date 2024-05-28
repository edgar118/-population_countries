from fastapi import APIRouter,HTTPException, Path, Depends, Request
from backend.provider import Provider
from backend.schema import Country_schema

router = APIRouter()


@router.get('/data')
def data(
    countries: list = None
    ):
    return Provider.country_mean(countries)

@router.get('/data/countries')
def data_by_country(
    countries: Country_schema = None
    ):
    return Provider.country_fad(countries)

@router.get('/data_json')
def data_json(
    ):
    return Provider.population_data_to_json()

@router.get('/export')
def export(
    countries: Country_schema = None
    ):
    return Provider.export_excel(countries)
