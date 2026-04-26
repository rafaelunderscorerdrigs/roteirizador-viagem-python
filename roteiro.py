import folium
from folium.plugins import Search, Geocoder
import pandas as pd
import requests

# 1. Configuração dos Dados do seu Roteiro
data = {
    'Local': ['Airbnb (Início)', 'Catedral São João Batista', 'Ponte dos Arcos', 'Parque Centenário', 'Nardelli Gastronomia'],
    'Lat': [-27.2145, -27.2158, -27.2112, -27.2210, -27.2105],
    'Lon': [-49.6420, -49.6435, -49.6485, -49.6350, -49.6410],
    'Tipo': ['Hospedagem', 'Turismo', 'Turismo', 'Lazer', 'Alimentação']
}
df = pd.DataFrame(data)

# 2. Inicialização do Mapa (Focado em Rio do Sul)
# Usando tiles do CartoDB para evitar erros de bloqueio local (403)
mapa = folium.Map(
    location=[df['Lat'].mean(), df['Lon'].mean()], 
    zoom_start=14, 
    tiles='cartodbpositron'
)

# 3. Função para traçar Rota via OSRM (Motor de busca de ruas)
def traçar_rota(ponto_a, ponto_b, mapa_obj):
    url = f"http://router.project-osrm.org/route/v1/driving/{ponto_a[1]},{ponto_a[0]};{ponto_b[1]},{ponto_b[0]}?overview=full&geometries=geojson"
    try:
        r = requests.get(url)
        dados = r.json()
        if 'routes' in dados and len(dados['routes']) > 0:
            linhas = [[c[1], c[0]] for c in dados['routes'][0]['geometry']['coordinates']]
            folium.PolyLine(linhas, color='#3388ff', weight=5, opacity=0.7, tooltip="Trajeto Estimado").add_to(mapa_obj)
    except Exception as e:
        print(f"Erro ao calcular rota: {e}")

# Exemplo: Traçando a rota do Airbnb até a Catedral
traçar_rota([df.iloc[0]['Lat'], df.iloc[0]['Lon']], [df.iloc[1]['Lat'], df.iloc[1]['Lon']], mapa)

# 4. Criação de Grupos para Controle de Camadas
grupo_pontos = folium.FeatureGroup(name="📍 Meus Locais").add_to(mapa)
grupo_legenda = folium.FeatureGroup(name="📝 Exibir Legenda", show=True).add_to(mapa)

# 5. Adicionando Marcadores do Roteiro
for _, row in df.iterrows():
    cor = 'red' if row['Tipo'] == 'Hospedagem' else 'blue'
    folium.Marker(
        location=[row['Lat'], row['Lon']],
        popup=row['Local'],
        name=row['Local'],
        icon=folium.Icon(color=cor, icon='info-sign')
    ).add_to(grupo_pontos)

# 6. INTEGRAÇÃO: Busca Global + Busca Interna
# Busca qualquer lugar no mundo (focado em Rio do Sul pelo centro do mapa)
Geocoder(
    position='topleft', 
    add_marker=True, 
    placeholder="Pesquisar em Rio do Sul...",
    zoom=15
).add_to(mapa)

# Busca rápida apenas nos itens do seu roteiro (Airbnb, etc)
Search(
    layer=grupo_pontos, 
    geom_type='Point', 
    placeholder="Buscar no meu roteiro...", 
    search_label='name'
).add_to(mapa)

# 7. CSS e HTML da Legenda Responsiva
legenda_html = f'''
<div id="minha-legenda" class="map-legend">
    <h4 style="margin-top:0">🗺️ Roteiro Rio do Sul</h4>
    <p><span style="color:red">●</span> <b>Hospedagem</b></p>
    <p><span style="color:blue">●</span> <b>Turismo / Lazer</b></p>
    <small>Use o ícone de camadas (topo dir.) para ocultar.</small>
</div>
<style>
    .map-legend {{
        position: fixed; bottom: 30px; left: 20px; width: 220px; z-index: 9999; 
        background-color: white; padding: 15px; border-radius: 8px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2); font-family: sans-serif;
    }}
    @media (max-width: 768px) {{
        .map-legend {{ width: 180px; font-size: 11px; bottom: 80px; left: 10px; }}
    }}
</style>
'''
mapa.get_root().html.add_child(folium.Element(legenda_html))

# 8. Controle de Camadas e Salvamento
folium.LayerControl(collapsed=False).add_to(mapa)

mapa.save('index.html')
print("✅ Sucesso! O arquivo index.html foi gerado com Busca Global e Rotas.")
