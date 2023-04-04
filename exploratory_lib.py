# exploratory_lib.py

import pandas as pd
#=====================
# Se Cargan los datos 
#=====================
def extract_csv(folder_direct_in,file_name,sep_str=';'):
    file_direct_in=f"{folder_direct_in}/{file_name}.csv"
    col_names=pd.read_csv(file_direct_in,
                        encoding="utf-8",sep=sep_str,nrows=0).columns
    types_dict = {col: str for col in list(col_names)}

    data_out = pd.read_csv(file_direct_in,
                    encoding="utf-8",sep=sep_str,dtype=types_dict)
    print("Dimensiones:",data_out.shape)
    print(f"Columnas \n {', '.join(col_names)}")
    return data_out

#===================================
# Dicionario 
#===================================
array_mes_name=['Enero','Febrero','Marzo','Abril',
'Mayo','Junio','Julio','Agosto',
'Septiembre','Octubre',
'Noviembre','Diciembre']
class class_diccionarios:
    def __init__(self):
        self.array_numbers = []
        self.array_name= []
        self.name_dic = {}
        self.name_dic_upper = {}
        self.int_dic = {}
    #===================================
    # Fecha
    #===========================================
    def set_list_num(self,array_n_int):
        self.array_numbers = array_n_int
    def set_list_name(self,array_n_str):
        self.array_name = array_n_str
    def set_dictionary(self):
        self.int_dic = { self.array_numbers[i] : self.array_name[i] for i in range(len(self.array_name))}
        self.name_dic = { self.int_dic[i] : i for i in self.array_numbers}
        self.name_dic_upper = { self.int_dic[i].upper() : i   for i in self.array_numbers}

    def int_to_name(self,int_x):
        """
        Transforma el numero del 'mes' en una etiqueta con nombre
        """
        return(self.int_dic[int_x])
    
    def name_to_num(self,string_x):
        """
        Transforma el nombre del 'mes' en una etiqueta con nombre
        """
        return(self.name_dic_upper[string_x.upper()])
    def list_name(self):
        return self.array_name
    def list_number(self):
        return self.array_numbers
    def dic_names(self):
        return self.name_dic
    def dic_numbers(self):
        return self.int_dic

# ================================
# Transformacion de los datos
# ================================
def convert_to_date(datetime_str):
    return pd.to_datetime(datetime_str, format='%Y-%m-%d %H:%M:%S')

# HIGH_SEASON
def col_high_season(date_x):
    """
    Retorna un binario 1 en el caso que la fecha sea de temporada alta 
    0 en el caso de un escenario normal.
    """
    Año_actual= date_x.year
    # Between Dec-15 and Mar-3
    verano_start = convert_to_date( f"{Año_actual}-12-15 00:00:00") 
    verano_end = convert_to_date( f"{Año_actual}-3-4 00:00:00")
    bool_verano = (
            (verano_end > date_x )
            |(date_x >verano_start)
            )
    # Jul-15 and Jul-31, 
    invierno_start = convert_to_date( f"{Año_actual}-7-15 00:00:00") 
    invierno_end = convert_to_date( f"{Año_actual}-8-1 00:00:00")
    bool_invierno = (invierno_end > date_x >invierno_start)
    # Sep-11 and Sep-30
    sep_start = convert_to_date( f"{Año_actual}-9-11 00:00:00") 
    sep_end = convert_to_date( f"{Año_actual}-10-1 00:00:00")
    bool_sep = (sep_end > date_x >sep_start)
    if bool_verano | bool_invierno | bool_sep:
        return 1
    else:
        return 0
def period_day_func(hora_in):
    """
    morning (between 5:00 and 11:59)
    afternoon (between 12:00 and 18:59) 
    night (between 19:00 and 4:59)
    """
    if 5<=hora_in<12:
        return "morning"
    elif 12<=hora_in<19:
        return "afternoon"
    elif (19<=hora_in) | (hora_in <5):
        return "night"
    else:
        return "error"

# Transforma los datos y entrega la fecha
def additional_columns(df_in,col_name_i ="Fecha-I",col_name_0 ="Fecha-O"):
    # ==============
    # HIGH_SEASON
    # 1 if Date-I is between Dec-15 and Mar-3, or Jul-15 and Jul-31, or Sep-11 and Sep-30, 0 otherwise.
    # ==============
    # col_name_i ="Fecha-I"
    # col_name_0 ="Fecha-O"
    df_out = df_in.copy()
    df_out["date_i"] = df_out[col_name_i].apply(convert_to_date)
    df_out["date_o"] = df_out[col_name_0].apply(convert_to_date)
    df_out["high_season"] = df_out["date_i"].apply(col_high_season)
    # ==============
    # PERIOD_DAY
    # ==============
    df_out["period_day"] = df_out["date_i"].dt.hour.apply(period_day_func)
    # =====================
    # MIN_DIFF
    # =====================
    df_out["min_diff"] = (df_out["date_o"] - df_out["date_i"]).dt.total_seconds() / 60
    # =====================
    # delay_15
    # =====================
    df_out["delay_15"] = df_out["min_diff"].apply( lambda x: 1 if x >15 else 0 )
    return df_out