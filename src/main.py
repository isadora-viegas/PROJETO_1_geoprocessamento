import geopandas as gpd
import matplotlib.pyplot as plt

print("Iniciando análise geográfica...")

# Ler o GeoJSON
arquivo = "../dados/municipios.json"
gdf = gpd.read_file(arquivo)

print("Colunas disponíveis:", list(gdf.columns))
print("Quantidade de municípios:", len(gdf))

# Converter para projeção em metros (necessário para área)
gdf = gdf.to_crs(epsg=5880)

# Calcular área em km²
gdf["area_km2"] = gdf.geometry.area / 1_000_000

# Mostrar dados básicos
print(gdf[["name", "area_km2"]].head())

# Mapa temático por área
gdf.plot(
    column="area_km2",
    legend=True,
    figsize=(10, 10)
)

plt.title("Municípios do Brasil por Área (km²)")
plt.show()

print("Projeto executado com sucesso!")


