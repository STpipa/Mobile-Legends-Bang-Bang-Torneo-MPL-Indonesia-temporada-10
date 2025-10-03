# src/etl.py
import pandas as pd
import os
from sqlalchemy import create_engine, text 
from datetime import datetime

# Rutas de entrada/salida
RAW_PATH = os.path.join("data", "raw", "MPL_ID_S10.csv")
PARQUET_OUT = os.path.join("data", "processed", f"MPL_ID_S10_{datetime.now().strftime('%Y%m%d_%H%M')}.parquet")
DB_PATH = os.path.join("mlbb_mpl_s10.db")
print("\n--- INICIO DEPURACIÓN DB ---") # Mensaje para destacarse
print("Ruta absoluta donde se intenta guardar la base SQLite:", os.path.abspath(DB_PATH))
print("--- FIN DEPURACIÓN DB ---\n")

def clean_percent_column(series):
    """
    Limpia una columna de porcentajes:
    - Convierte a string
    - Quita '%'
    - Reemplaza '-' por 0
    - Cambia comas por puntos
    - Convierte a float
    """
    return (series.astype(str)
                 .str.replace("%", "", regex=False)
                 .replace("-", "0")
                 .str.replace(",", ".", regex=False)
                 .astype(float))

def main():
    print("📥 Leyendo CSV...")
    df = pd.read_csv(RAW_PATH)

    # Identificar columnas que tienen porcentajes
    pct_cols = [c for c in df.columns if any(k in c.lower() for k in [
        "winrate", "pickpercentage", "ban_percentage", "ban percentage", "pick&ban"
    ])]

    # Limpiar porcentajes
    for col in pct_cols:
        try:
            df[col] = clean_percent_column(df[col])
        except Exception as e:
            print(f"⚠️ No pude convertir {col}: {e}")

    # Crear columna Presence si existen pickrate y banrate
    if "T_pickpercentage" in df.columns and "Ban_percentage" in df.columns:
        df["Presence"] = df["T_pickpercentage"] + df["Ban_percentage"]
    else:
        df["Presence"] = 0.0
        print("ℹ️ No encontré columnas T_pickpercentage / Ban_percentage → Presence = 0")

    # Guardar en Parquet (procesado)
    os.makedirs(os.path.dirname(PARQUET_OUT), exist_ok=True)
    df.to_parquet(PARQUET_OUT, index=False)
    print(f"💾 Guardado Parquet en: {PARQUET_OUT}")

    # Guardar en base SQLite
    engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
    df.to_sql("hero_meta_stats", con=engine, if_exists="replace", index=False)
    print(f"🗄️ Tabla 'hero_meta_stats' cargada en DB: {DB_PATH}")

    # Chequeo rápido
    with engine.connect() as conn:
        n = conn.execute(text("SELECT COUNT(*) FROM hero_meta_stats")).fetchone()[0]
        print(f"✅ Registros en hero_meta_stats: {n}")

if __name__ == "__main__":
    main()
