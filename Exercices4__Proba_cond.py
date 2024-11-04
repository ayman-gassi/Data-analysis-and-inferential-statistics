import seaborn as sns
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import tips
tips = sns.load_dataset('tips')
print('Tableau de donnees :')
print(tips.head())
print(' ')

# Digramme de Venn
# venn2([set(tips[tips['sex'] == 'Male'].index), set(tips[tips['smoker'] == 'Yes'].index)], ('Male', 'smoker'))
# plt.title("Venn Diagram")
# plt.show()

# Arbre pondere
print("Arbre pondere :")
prob_Male =  round(len(tips[tips['sex'] == 'Male']) / len(tips),2)
print("Probabilite Male : ", prob_Male)
prob_Male_Smoker = round(len(tips[(tips['sex'] == 'Male') &  (tips['smoker'] == 'Yes')]) / len(tips[tips['sex'] == 'Male']) ,2)
print("-> Male & Smoker : ", prob_Male_Smoker)
prob_Male_No_Smoker = round(len(tips[(tips['sex'] == 'Male') &  (tips['smoker'] == 'No')]) / len(tips[tips['sex'] == 'Male']) ,2)
print("-> Male & no Smoker : ", prob_Male_No_Smoker)
prob_Female =  round(len(tips[tips['sex'] == 'Female']) / len(tips),2)
print("Probabilite Female : ", prob_Female)
prob_Female_Smoker = round(len(tips[(tips['sex'] == 'Female') &  (tips['smoker'] == 'Yes')]) / len(tips[tips['sex'] == 'Male']) ,2)
print("-> Female & Smoker : ", prob_Female_Smoker)
prob_Female_No_Smoker = round(len(tips[(tips['sex'] == 'Female') &  (tips['smoker'] == 'No')]) / len(tips[tips['sex'] == 'Male']) ,2)
print("-> Female & no Smoker : ", prob_Female_No_Smoker)
print(' ')

# Theoreme de Bayes
print("Theoreme de Bayes :")
prob_Smoker = round(len(tips[(tips['sex'] == 'Male') &  (tips['smoker'] == 'Yes')]) / len(tips[tips['smoker'] == 'Yes']),2)
print("P(Homme/Smoker) = ", prob_Smoker)
print(' ')

# Tableau de contingence
print("Tableau de contingence :")
tableau_de_contingence = pd.crosstab(index=tips['sex'], columns=tips['smoker'], margins=True) 
print(tableau_de_contingence)
print(' ')

# Probabilite totale
print("Probabilite totale :")
print((prob_Female_Smoker * prob_Female) + (prob_Male_Smoker * prob_Male))


