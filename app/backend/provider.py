import pandas as pd
from fastapi import Response, HTTPException
from fastapi.responses import StreamingResponse
import io

class Provider():
    def read_file(country: list = None):
        df_population = pd.read_csv('./backend/population_total.csv')
        df_population = df_population.dropna()

        df_population['year'] = df_population['year'].astype(int)
        
        if country:
            df_population = df_population[df_population['country'].isin(country)]
            if df_population.empty:
                return None

        df_population = df_population.pivot(index='year', columns='country', values='population')
        
        return df_population
    def all_data_by_country(country: str = None):
        
        media = Provider.country_mean(country)
        mediana = Provider.country_median(country)
        moda = Provider.country_fad(country)

        data = {
            "country": country,
            "media": media[-1],
            "mediana": mediana[-1],
            "moda": moda[-1]
        }

        return data
    
    def country_mean(country: list = None):
        df_population = Provider.read_file(country)
        media_por_pais = df_population.mean()
        
        return media_por_pais

    def country_median(country: list = None):
        df_population = Provider.read_file(country)
        mediana_por_pais = df_population.median()
        return mediana_por_pais

    def country_fad(country: list = None):
        df_population = Provider.read_file(country)
        moda_por_pais = df_population.apply(lambda x: x.mode().iloc[0])
        return moda_por_pais

    def population_data_to_json(country: list = None):
        df_population = Provider.read_file(country)
        population_json = df_population.to_json()

        return Response(content=population_json, media_type="application/json")
    
    def export_excel(country: list = None):
        df_population = Provider.read_file(country.countries)
    
        if df_population is None or df_population.empty:
            raise HTTPException(status_code=404, detail=f"Countries '{country}' not found.")
        
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            # Exportar datos de población
            df_population.to_excel(writer, sheet_name='Population Data')
        
        output.seek(0)
        
        headers = {
            'Content-Disposition': f'attachment; filename="population_data_{country if country else "all"}.xlsx"'
        }
        return StreamingResponse(output, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers=headers)
