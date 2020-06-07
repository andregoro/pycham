import sys
from arquivo import *
from exec import *
# print(sys.argv[1])
s = sys.argv

# print(s)
l = sys.argv
if s.__contains__('-p') and len(sys.argv) > 2:
    arq=l[sys.argv.index('-p') + 1]
    processos=arquivo(arq)
    #print(arq)
    # ---------------------------------------------------------
    if s.__contains__('-s') and sys.argv[sys.argv.index('-s')+1]== 'interativo':
        print('interativo', l[sys.argv.index('-s') + 1])
        # ====================================================
        if s.__contains__('-a'):
            print('algoritimo', l[sys.argv.index('-a') + 1])
            # ==================================================
            if s.__contains__('-q'):
                print('com tempo',l[sys.argv.index('-q') + 1])
                # ==============================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
            # ==================================================
            else:
                print('sem tempo')
                # ==================================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
        # ==================================================
        else:
            print('sem algoritmo')
            # ==================================================
            if s.__contains__('-q'):
                print('com tempo',l[sys.argv.index('-q') + 1])
                # ==============================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
            # ==================================================
            else:
                print('sem tempo')
                # ==================================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
        # ==================================================
    elif s.__contains__('-s') and sys.argv[sys.argv.index('-s') + 1] == 'lote':
        print('lote', l[sys.argv.index('-s') + 1])
    # ====================================================
        if s.__contains__('-a'):
            print('algoritimo', l[sys.argv.index('-a') + 1])
        # ==================================================
            if s.__contains__('-q'):
                print('com tempo', l[sys.argv.index('-q') + 1])
            # ==============================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
            # ==================================================
            else:
                print('sem tempo')
            # ==================================================
            if s.__contains__('-steps'):
                print('com passo a passo')
        else:
            print('sem algoritmo')
            if s.__contains__('-q'):
                print('com tempo', l[sys.argv.index('-q') + 1])
            # ==============================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
            else:
                print('sem tempo')
                if s.__contains__('-steps'):
                    print('com passo a passo')
    else:
        print('lote')
        algoritmo(processos,"fifo")
        if s.__contains__('-a'):
            print('algoritimo', l[sys.argv.index('-a') + 1])
            if s.__contains__('-q'):
                print('com tempo',l[sys.argv.index('-q') + 1])
                # ==============================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
            else:
                print('sem tempo')
                if s.__contains__('-steps'):
                    print('com passo a passo')
        else:
            print('sem algoritmo')
            if s.__contains__('-q'):
                print('com tempo',l[sys.argv.index('-q') + 1])
                # ==============================================
                if s.__contains__('-steps'):
                    print('com passo a passo')
            else:
                print('sem tempo')
                if s.__contains__('-steps'):
                    print('com passo a passo')
else:
    raise Exception('Falta -p')