#################################################################
##Richard Jansen HAN University of Applied Sciences 24-03-2015###
##Afvinkopdracht 5 blok 3a#######################################
#################################################################

def main():
    class gen():


    
        def eig(self, seq, naam):
            self.seq = seq
            self.naam = naam 
            self.rna = ""
            self.eiwit = ""
            self.dna = ""

        def getproperties(self):
            print ("Name:  "+ str(self.naam) +"\nRNA:   "+ str(self.rna)+"\nDNA:   "+ str(self.dna) +"\nProtein: "+ str(self.eiwit))
           
        def Transcript(self):
            a = self.seq.index("atg")
            sequ = self.seq[a:]
            t = len(sequ)
            rna = sequ.replace("t","u")
            c = ""
            d = ""
            seq = ""
            while a < t: 
                codon1 = rna[a:a+3]
                codon2 = sequ[a:a+3]
                a += 3
                if codon1 == "uaa"or codon1 == "uag" or codon1 == "uga":
                    c += str(codon1)
                    d += str(codon2)
                    seq += str(codon2)
                    self.rna = c
                    self.dna = d
                    self.seq = seq
                else:
                    c += str(codon1) + " "
                    d += str(codon2) + " "
                    seq += str(codon2)           

        def Translate(self):
            codonlijst = {'ttt': 'F', 'tct': 'S', 'tat': 'Y', 'tgt': 'C',
    'ttc': 'F', 'tcc': 'S', 'tac': 'Y', 'tgc': 'C',
    'tta': 'L', 'tca': 'S', 'taa': '*', 'tga': '*',
    'ttg': 'L', 'tcg': 'S', 'tag': '*', 'tgg': 'W',
    'ctt': 'L', 'cct': 'P', 'cat': 'H', 'cgt': 'R',
    'ctc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
    'cta': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
    'ctg': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
    'att': 'I', 'act': 'T', 'aat': 'N', 'agt': 'S',
    'atc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
    'ata': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
    'atg': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
    'gtt': 'V', 'gct': 'A', 'gat': 'D', 'ggt': 'G',
    'gtc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
    'gta': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
    'gtg': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G'}

            a = self.seq.index("atg")
            t = len(self.seq)
            lijst = ""
            b = self.seq.replace(" ", "")
            
            while a < t:        
                codon = b[a:a+3]             
                a += 3
                lijst = lijst +" "+str(codonlijst[codon])+ "  "
            self.eiwit = lijst
    g = gen()
    seq = "atggctgagagacgttgaggg"
    naam = "p53"
    genzelf = g.eig(seq, naam)
    rnastr = g.Transcript()
    eiwit = g.Translate()
    g.getproperties()
    
main()