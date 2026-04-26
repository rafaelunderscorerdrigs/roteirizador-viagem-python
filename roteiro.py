import folium
from geopy.distance import geodesic

# 1. Definição dos Locais (Dados)
locais = [
    {"nome": "1. Início: Rodoviária", "coord": [-27.2144, -49.6433], "desc": "Ponto de encontro do BlaBlaCar"},
    {"nome": "2. Check-in: Airbnb", "coord": [-27.2255, -49.6385], "desc": "R. Leopoldo Ledra, 532 - Santana"},
    {"nome": "3. Catedral São João Batista", "coord": [-27.2161, -49.6441], "desc": "Turismo e arquitetura no centro"},
    {"nome": "4. Mirante Parque de Exposições", "coord": [-27.2285, -49.6275], "desc": "Foto oficial do feriado"},
    {"nome": "5. Toca da Onça (Lontras)", "coord": [-27.1661, -49.5447], "desc": "Cachoeira e trilha anti-abandono"},
    {"nome": "6. Observatório Pub / General", "coord": [-27.2115, -49.6350], "desc": "Happy hour de encerramento"}
]

# 2. Cálculo das distâncias para a legenda
texto_legenda = "<b>📏 Distâncias Estimadas (Trechos):</b><br>"
for i in range(len(locais) - 1):
    ponto_a = locais[i]["coord"]
    ponto_b = locais[i+1]["coord"]
    distancia = geodesic(ponto_a, ponto_b).km
    texto_legenda += f"{locais[i]['nome'].split(':')[0]} ➔ {locais[i+1]['nome'].split(':')[0]}: <b>{distancia:.2f} km</b><br>"

# 3. Criar a legenda visual (HTML)
legenda_html = f'''
     <div style="
     position: fixed; 
     bottom: 30px; left: 30px; width: 320px; height: auto; 
     background-color: white; border:2px solid #333; z-index:9999; font-size:12px;
     padding: 12px;
     border-radius: 15px;
     box-shadow: 4px 4px 10px rgba(0,0,0,0.4);
     font-family: sans-serif;
     ">
     {texto_legenda}
     <br><small><i>*Distância em linha reta</i></small>
     </div>
     '''

# 4. Criar o mapa (Com Tiles que não bloqueiam)
mapa = folium.Map(location=[-27.2000, -49.6000], zoom_start=12, tiles='CartoDB positron')

# 5. Adicionar Marcadores e a Linha do Roteiro (PolyLine)
caminho = []
for local in locais:
    caminho.append(local["coord"])
    
    # Define a cor do ícone
    cor = 'blue'
    if "Início" in local["nome"]: cor = 'green'
    if "Airbnb" in local["nome"]: cor = 'orange'
    if "Pub" in local["nome"]: cor = 'red'

    folium.Marker(
        location=local["coord"],
        popup=f"<b>{local['nome']}</b><br>{local['desc']}",
        tooltip=local["nome"],
        icon=folium.Icon(color=cor, icon='info-sign')
    ).add_to(mapa)

# Desenha a linha conectando os pontos
folium.PolyLine(caminho, color="blue", weight=3, opacity=0.6, dash_array='10').add_to(mapa)

# 6. Inserir a Legenda no HTML do mapa
mapa.get_root().html.add_child(folium.Element(legenda_html))

# 7. Salvar o arquivo final
mapa.save("meu_roteiro_rio_do_sul.html")

print("✅ Mapa com legenda gerado com sucesso!")