import pickle

comptesBanque = {}

pickle.dump(comptesBanque, open('comptesBanqueFile', 'wb'))

print ('Fichier comptesBanqueFile reset')

