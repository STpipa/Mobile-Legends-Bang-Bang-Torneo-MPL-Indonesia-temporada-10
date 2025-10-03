# 📊 Análisis de Mobile Legends: MPL ID Season 10

Este proyecto es un **análisis de datos aplicado a Mobile Legends: Bang Bang**, utilizando datos del torneo **MPL Indonesia Season 10 (MPL ID S10)**.  

El objetivo fue aplicar técnicas de **ciencia de datos** para entender qué héroes dominaron el meta competitivo, y practicar un flujo de trabajo completo desde la limpieza de datos hasta Machine Learning.

---

## 🚀 Tecnologías utilizadas
- Python 3  
- Jupyter Notebook  
- Pandas, NumPy  
- Matplotlib, Seaborn  
- Scikit-learn  

---

## 📂 Dataset
El dataset proviene de MPL ID S10 e incluye métricas de héroes como:
- **Win Rate (%)**
- **Pick Rate (%)**
- **Ban Rate (%)**
- **Presencia (Pick + Ban)**

---

## 🔍 Análisis realizado
1. **Limpieza de datos:**  
   - Conversión de porcentajes a valores numéricos.  
   - Creación de métricas nuevas como *Presence*.  

2. **Análisis exploratorio (EDA):**  
   - Ranking de héroes por winrate, pickrate y presencia.  
   - Identificación de héroes *overpowered* y *infrautilizados*.  

3. **Comparación por roles:**  
   - Promedio de winrate y pickrate por rol (Mago, Tirador, Tanque, etc.).  

4. **Visualizaciones:**  
   - Scatterplots de winrate vs pickrate.  
   - Barplots de héroes más baneados.  

5. **Machine Learning básico:**  
   - **Clustering (K-Means):** agrupar héroes en arquetipos (*meta stable*, *niche pick*, *outsiders*).  
   - **Clasificación (Logistic Regression):** predecir si un héroe es *Meta* o *No Meta* con 83% de accuracy.  

---

## 📈 Resultados e Insights
- Los héroes con mayor **presencia en meta** no siempre son los de mayor winrate.  
- Los **roles tanque y mago** tuvieron más estabilidad en winrate que los asesinos.  
- El modelo de clasificación predice bien a los héroes *no meta*, pero falla más con los *meta*, mostrando que la definición de "meta" depende de factores contextuales (estrategia, composición, parche).  
