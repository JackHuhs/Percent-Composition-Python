print("This is a program which finds the percentage composition of an element in a compound by mass.\n")
compound = input("Type in the chemical formula for the compound (Capitalize the first letter in a chemical symbol and you don't need superscript for element quantities):\n")
element = input("Type in the element that you want to find the percentage of (a singular element with the first letter capitalized):\n")
elementDictionary = {"H":1.00794,"He":4.002602,"Li":6.941,"Be":9.012182,"B":10.811,"C":12.0107,"N":14.0067,"O":15.9994,"F":18.9984032,"Ne":20.1797,"Na":22.98976928,"Mg":24.305,"Al":26.9815386,"Si":28.0855,"P":30.973762,"S":32.065,"Cl":35.453,"Ar":39.948,"K":39.0983,"Ca":40.078,"Sc":44.955912,"Ti":47.867,"V":50.9415,"Cr":51.9961,"Mn":54.938045,"Fe":55.845,"Co":58.933195,"Ni":58.6934,"Cu":63.546,"Zn":65.38,"Ga":69.723,"Ge":72.64,"As":74.9216,"Se":78.96,"Br":79.904,"Kr":83.798,"Rb":85.4678,"Sr":87.62,"Y":88.90585,"Zr":91.224,"Nb":92.90638,"Mo":95.96,"Tc":98,"Ru":101.07,"Rh":102.9055,"Pd":106.42,"Ag":107.8682,"Cd":112.411,"In":114.818,"Sn":118.71,"Sb":121.760,"Te":127.6,"I":126.90447,"Xe":131.293,"Cs":132.9054519,"Ba":137.327,"Hf":178.49,"Ta":180.94788,"W":183.84,"Re":186.207,"Os":190.23,"Ir":192.217,"Pt":195.084,"Au":196.966569,"Hg":200.59,"Ti":204.3833,"Pb":207.2,"Bi":208.9804,"Po":209,"At":210,"Rn":222,"Fr":223,"Ra":226,"Rf":265,"Db":268,"Sg":271,"Bh":272,"Hs":277,"Mt":276,"Ds":281,"Rg":280,"Cn":285,"Uut":284,"Uuq":289,"Uup":288,"Uuh":293,"Uus":294,"Uuo":294,"La":138.90547,"Ce":140.116,"Pr":140.90765,"Nd":144.242,"Pm":145,"Sm":150.36,"Eu":151.964,"Gd":157.25,"Tb":158.92535,"Dy":162.5,"Ho":164.93032,"Er":167.259,"Tm":168.93421,"Yb":173.054,"Lu":174.9668,"Ac":227,"Th":232.03806,"Pa":231.03588,"U":238.02891,"Np":237,"Pu":244,"Am":243,"Cm":247,"Bk":247,"Cf":251,"Es":252,"Fm":257,"Md":258,"No":259,"Lr":262}
compoundDiagnosis = {}
elementsInDiagnosis = []
symbolStorer = ''
numberStorer = 0
for i in range(0,len(compound)):
  if ord(compound[i])>64 and ord(compound[i])<91:
    if symbolStorer == '':
      symbolStorer=symbolStorer+compound[i]
    else:
      if symbolStorer in elementDictionary:
        if numberStorer > 1:
          compoundDiagnosis[symbolStorer] = numberStorer
          elementsInDiagnosis.append(symbolStorer)
          numberStorer = 0
        else:
          compoundDiagnosis[symbolStorer] = 1
          elementsInDiagnosis.append(symbolStorer)
          numberStorer = 0
      else:
        print("Error: '"+symbolStorer+"' is not an element symbol, please make sure you capitalize correctly.")
        exit()
      symbolStorer = compound[i]
  if ord(compound[i])>96 and ord(compound[i])<123:
    symbolStorer=symbolStorer+compound[i]
  if ord(compound[i])>47 and ord(compound[i])<58:
    numberStorer=(numberStorer*10)+int(compound[i])
  if i > len(compound)-2:
    if symbolStorer in elementDictionary:
      if numberStorer > 1:
        compoundDiagnosis[symbolStorer] = numberStorer
        elementsInDiagnosis.append(symbolStorer)
      else:
        compoundDiagnosis[symbolStorer] = 1
        elementsInDiagnosis.append(symbolStorer)
    else:
      print("Error: '"+symbolStorer+"' is not an element symbol, please make sure you capitalize correctly.")
      exit()
totalMass = 0
for a in elementsInDiagnosis:
  for j in range(0,compoundDiagnosis[a]):
    totalMass += elementDictionary[a]
elementMass = 0
if element in compoundDiagnosis:
  elementMass = elementDictionary[element]*compoundDiagnosis[element]
else:
  print("Error: Element '"+element+"' is not in the compound.")
  exit()
result = '~'+str(round((elementMass/totalMass)*100,2))+'%'
print("\nThe percent composition of '"+element+"' in '"+compound+"' is "+result)