# Film Greenlight Recommender
*Desafio Cientista de Dados*

---

## Sumário
- [Objetivo](#objetivo)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Pipeline do Projeto](#pipeline-do-projeto)
- [Resultados Resumidos](#resultados-resumidos)
- [Como Executar](#como-executar)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Autores](#autores)

---

## Objetivo
O objetivo é analisar um banco de dados cinematográfico e responder:

1. Qual filme recomendar para uma pessoa desconhecida?  
2. Quais fatores influenciam no faturamento?  
3. Quais insights podem ser obtidos a partir do texto de *Overview*?  
4. Como prever a nota do IMDB?  
5. Qual seria a nota prevista para *The Shawshank Redemption*?  

Este projeto combina **análise exploratória**, **processamento de linguagem natural** e **machine learning** para responder às perguntas de negócio propostas no desafio.

---

## Estrutura do Repositório

film-greenlight-recommender
├── data/
│   └── raw/                 # Dados brutos (imdb.csv)
├── models/                  # Artefatos treinados e pré-processadores (.pkl)
├── notebooks/               # Jupyter Notebooks (EDA, NLP, Preprocess, Modelagem)
│   ├── 01_eda.ipynb
│   ├── 02_overview.ipynb
│   ├── 03_preprocessing.ipynb
│   └── 04_modeling.ipynb
├── reports/                 # Relatórios finais (PDF/CSV) e figuras
│   ├── figures/
│   ├── model_selection.csv
│   └── cv_scores.csv
├── requirements.txt         # Dependências
└── README.md


---

## Pipeline do Projeto
1. **Exploração dos Dados (EDA)**  
   - Panorama das variáveis, correlações, outliers e hipóteses iniciais.  

2. **Análise de Texto (Overview)**  
   - Insights de linguagem e classificação de gênero a partir do texto.  

3. **Pré-processamento**  
   - Tratamento de valores faltantes, encoding de categóricas, scaling de numéricas e vetorização de texto.  

4. **Modelagem**  
   - Modelos de regressão para prever `IMDB_Rating`.  
   - Métricas comparadas: **MAE** e **RMSE**.  
   - Modelo final salvo como `.pkl`.  

5. **Resultados**  
   - Respostas às perguntas do desafio + insights adicionais.  

---

## Resultados Resumidos
- Recomendação baseline: filmes com ranking ponderado IMDb (nota + nº votos).  
- Fatores de faturamento: gênero (Action, Adventure, Sci-Fi ↑), popularidade (`No_of_Votes`), década de lançamento.  
- Overview: textos permitem classificar gênero com acurácia razoável via TF-IDF + Logistic Regression.  
- Melhor modelo para IMDB_Rating: GradientBoostingRegressor (MAE ≈ 0.15, RMSE ≈ 0.19).  
- Previsão para Shawshank Redemption: ~8.80 (coerente com a realidade).  

---

## Como Executar
### 1. Clone o repositório
```bash
git clone https://github.com/nalugomesv/film-greenlight-recommender
cd film-greenlight-recommender
```

### 2. Crie um ambiente virtual e ative
```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

### 3. Instale dependências
```
pip install -r requirements.txt
```
### 4. Execute os notebooks
```
jupyter notebook notebooks/01_eda.ipynb
```
## Autora:

Desenvolvido por Ana Luiza Gomes Vieira