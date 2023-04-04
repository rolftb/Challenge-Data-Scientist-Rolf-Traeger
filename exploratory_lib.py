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