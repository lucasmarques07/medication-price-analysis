import os
from sqlalchemy import create_engine

def dataBaseExport(df, database_path, table_name='medicamentos'):
    folder = os.path.dirname(database_path)
    
    if folder and not os.path.exists(folder):
        os.makedirs(folder)
    
    engine = create_engine(f"sqlite:///{database_path}")
    return df.to_sql(table_name, con=engine, if_exists='replace', index=False)