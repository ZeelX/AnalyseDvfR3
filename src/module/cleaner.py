import pandas as pd

class Cleaner:
    
    def __init__(self) -> None:
        pass
    
    
    def initialize(self, files: list[str]) -> pd.DataFrame:
        self.df = pd.concat([pd.read_csv(file, sep='|', decimal=',') for file in files])
        
        return self.df
        

    def clean(self):  
        self.df.isnull().sum()   
        self.df.dropna(axis=1, how="all", inplace=True)  
           
        self.df['Date mutation'] = pd.to_datetime(self.df['Date mutation'], format="%d/%m/%Y")
        self.df['Nature mutation'] = self.df['Nature mutation'].astype('category')
        self.df['Valeur fonciere'] = self.df['Valeur fonciere'].astype('float64')
        self.df['B/T/Q'] = self.df['B/T/Q'].astype('category')
        self.df['Type de voie'] = self.df['Type de voie'].astype('category')
        self.df['Code voie'] = self.df['Code voie'].astype('string')
        self.df['Voie'] = self.df['Voie'].astype('string')
        self.df['Commune'] = self.df['Commune'].astype('category')
        self.df['Code departement'] = self.df['Code departement'].astype('category')
        self.df['Section'] = self.df['Section'].astype('category')
        self.df['No Volume']= self.df['No Volume'].astype('string')
        self.df['1er lot'] = self.df['1er lot'].astype('string')
        self.df['2eme lot'] = self.df['2eme lot'].astype('string')
        self.df['3eme lot'] = self.df['3eme lot'].astype('string')
        self.df['Surface Carrez du 1er lot'] = self.df['Surface Carrez du 1er lot'].astype('float64')
        self.df['Surface Carrez du 2eme lot'] = self.df['Surface Carrez du 2eme lot'].astype('float64')
        self.df['Surface Carrez du 3eme lot'] = self.df['Surface Carrez du 3eme lot'].astype('float64')
        self.df['Surface Carrez du 4eme lot'] = self.df['Surface Carrez du 4eme lot'].astype('float64')       
        self.df['Surface Carrez du 5eme lot'] = self.df['Surface Carrez du 5eme lot'].astype('float64')
        self.df['Type local'] = self.df['Type local'].astype('string')
        self.df['Nature culture'] = self.df['Nature culture'].astype('string')
        self.df['Nature culture speciale'] = self.df['Nature culture speciale'].astype('string')
           