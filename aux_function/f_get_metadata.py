from os import listdir
import pandas as pd

def f_get_metadata(path):
    
    df = pd.DataFrame(columns=('name', 'Fecha', 'hora', 'name_file'))
    pd.to_datetime(df['Fecha'])
    pd.to_timedelta(df['hora'])

    for file in listdir(path):
        if file.endswith(".jpg") or file.endswith(".png"):
            f = file.replace('.', '_')
            metadata = f.split('_')
            time = metadata[2][0:2] + ':' + metadata[2][2:4] + ':' + metadata[2][4:6]
            new_row = {'name':metadata[0], 'Fecha':metadata[1], 'hora':time, 'name_file' :file}
            df = df.append(new_row, ignore_index=True)

    df = df.sort_values(by=['hora']).reset_index(drop=True) # Ordeno los valores por HORA

    return df