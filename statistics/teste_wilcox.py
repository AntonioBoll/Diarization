import scipy.stats as stats
 
# para a acuracia na sentenca
novo_acc_sentences = [0.918918918918919, 0.9259259259259259, 1.0, 0.9487179487179487, 0.95, 0.918918918918919, 0.9090909090909091, 1.0]
oracle_acc_sentences = [0.43478260869565216, 0.5, 0.3103448275862069, 0.7941176470588235, 0.4411764705882353, 0.8717948717948718, 0.41935483870967744, 0.06451612903225806]
assembly_acc_sentences = [0.7222222222222222, 0.64, 0.9642857142857143, 0.9512195121951219, 0.4411764705882353, 0.8648648648648649, 0.9032258064516129, 1.0] 

# novo x oracle 
stats.wilcoxon(novo_acc_sentences, oracle_acc_sentences, alternative='greater')

# novo x assembly 
stats.wilcoxon(novo_acc_sentences, assembly_acc_sentences, alternative='greater')

# assembly x oracle 
stats.wilcoxon(assembly_acc_sentences, oracle_acc_sentences, alternative='greater')

# para o f1 na sentenca
novo_f1_sentences = [0.9444658944658945, 0.95679012345679, 1.0, 0.9511599511599511, 0.9574074074074075, 0.9276667972320146, 0.9090909090909091, 1.0]
oracle_f1_sentences = [0.4647611259305412, 0.515114709851552, 0.3256704980842912, 0.7164705882352941, 0.35, 0.9028749028749028, 0.45717234262125905, 0.12121212121212122]
assembly_f1_sentences = [0.8028337403337402, 0.6953846153846155, 0.9807692307692307, 0.9600736592882106, 0.33998757874190394, 0.8932983564562512, 0.9165632754342431, 1.0]

# novo x oracle 
stats.wilcoxon(novo_f1_sentences, oracle_f1_sentences, alternative='greater')

# novo x assembly 
stats.wilcoxon(novo_f1_sentences, assembly_f1_sentences, alternative='greater')

# assembly x oracle 
stats.wilcoxon(assembly_f1_sentences, oracle_f1_sentences, alternative='greater')

##############################################################################################################

# para a acuracia na palavra
novo_acc_palavra = [0.9669211195928753, 0.9136276391554703, 1.0, 0.9938144329896907, 0.9880478087649402, 0.974308300395257, 0.9957716701902748, 1.0]
oracle_acc_palavra = [0.38362068965517243, 0.40080160320641284, 0.3923444976076555, 0.9174664107485605, 0.374749498997996, 0.9817444219066938, 0.30786516853932583, 0.02901023890784983]
assembly_acc_palavra = [0.7268817204301076, 0.5009671179883946, 0.9738095238095238, 0.9939024390243902, 0.4153543307086614, 0.8900414937759336, 0.9652777777777778, 1.0]

# novo x oracle 
stats.wilcoxon(novo_acc_palavra, oracle_acc_palavra, alternative='greater')

# novo x assembly 
stats.wilcoxon(novo_acc_palavra, assembly_acc_palavra, alternative='greater')

# assembly x oracle 
stats.wilcoxon(assembly_acc_palavra, oracle_acc_palavra, alternative='greater')

# para o f1 na sentenca
novo_f1_palavra = [0.9774425735460257, 0.9491324831389923, 1.0, 0.9938544467225006, 0.9891224742971846, 0.9735888564679976, 0.9957716701902748, 1.0]
oracle_f1_palavra = [0.4006802355233451, 0.4150221768588938, 0.4049193463741069, 0.8790299099309462, 0.2751872914185369, 0.9875000467680598, 0.31491520432802256, 0.05638474295190713]
assembly_f1_palavra = [0.7900492969009472, 0.5189179410823372, 0.9863398692810458, 0.9958286209116578, 0.31207976345271593, 0.8951550844161575, 0.96919810468969, 1.0]

# novo x oracle 
stats.wilcoxon(novo_f1_palavra, oracle_f1_palavra, alternative='greater')

# novo x assembly 
stats.wilcoxon(novo_f1_palavra, assembly_f1_palavra, alternative='greater')

# assembly x oracle 
stats.wilcoxon(assembly_f1_palavra, oracle_f1_palavra, alternative='greater')

