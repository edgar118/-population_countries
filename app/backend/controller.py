import pandas as pd
import cufflinks as cf
import plotly.offline


def read_file():
    df_population = pd.read_csv('population_total.csv')
    df_population = df_population.dropna()
    countrys = df_population['country'].unique().tolist()

    df_population = df_population.pivot(index='year', columns='country', values='population')

    df_population = df_population[countrys]

    return df_population

def country_mean():
    df_population = read_file()
    media_por_pais = df_population.mean()
    print("Media por país:")
    print(media_por_pais)

def country_median():
    df_population = read_file()
    mediana_por_pais = df_population.median()
    print("\nMediana por país:")
    print(mediana_por_pais)

def country_fad():
    df_population = read_file()
    moda_por_pais = df_population.apply(lambda x: x.mode().iloc[0])
    print("\nModa por país:")
    print(moda_por_pais)

def population_data_to_json():
    df_population = read_file()
    population_json = df_population.to_json()

    return population_json

# Ejemplo de uso
print(population_data_to_json)