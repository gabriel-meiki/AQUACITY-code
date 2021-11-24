import PySimpleGUI as sg

def janela_inicial(): # PÁGINA DA TELA INICIAL
    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('        AQUACITY        '), sg.Button(' ⚙ ')],
        [sg.Text('__________________________')],
        [sg.Button('        COMEÇAR        ')],
        [sg.Button('       CONTINUAR       ')]
    ]
    return sg.Window('PÁGINA INICIAL', layout=layout, finalize=True)

def janela_começar(): # PÁGINA DA TELA NOVO PROGRESSO
    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('VOCÊ DESEJA COMEÇAR UM NOVO PROGRESSO ?')],
        [sg.Button('SIM'), sg.Button('NÃO')],
        [sg.Output(size=(50,0))]
    ]
    return sg.Window('PÁGINA NOVO PROGRESSO', layout=layout, finalize=True)

def janela_começar2(): # PÁGINA DA TELA DO NOME DO NOVO PROGRESSO
    sg.theme('DarkBlue16')
    layout = [
        [sg.Button(' <<< '), sg.Text('          DIGITE AQUI O NOME DO       ')],
        [sg.Text('                     SEU NOVO PROGRESSO          ')],
        [sg.Input()],
        [sg.Button('CONTINUAR')],
        [sg.Output(size=(30,0))]
    ]
    return sg.Window('PÁGINA DO NOME DO NOVO PROGRESSO', layout=layout, finalize=True)

def janela_continuar(): # PÁGINA CONTINUAR
    sg.theme('DarkBlue16')
    layout = [
        [sg.Button(' <<< '),sg.Text('    🔍|    Digite o seu progresso ...............|')],
        [sg.Button('SAVE1')],
        [sg.Button('SAVE2')],
        [sg.Button('SAVE3')],
        [sg.Output(size=(50,0))]
    ]
    return sg.Window('PÁGINA CONTINUAR', layout=layout, finalize=True)

def janela_continuar2(): # PÁGINA CONFIRMAÇÃO PARA CONTINUAR TAL PROGRESSO
    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('VOCÊ DESEJA VOLTAR AO \nPROGRESSO "SAVE1" ?')],
        [sg.Text(' ')],
        [sg.Button('SIM'), sg.Button('NÃO')],
        [sg.Text(' ')],
        [sg.Output(size=(50,0))]
    ]
    return sg.Window('PÁGINA CONFIRMAÇÃO PARA CONTINUAR TAL PROGRESSO', layout=layout, finalize=True)

def janela_configurações(): # PÁGINA DAS CONFIGURAÇÕES
    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('CONFIGURAÇÕES|')],
        [sg.Button(' <<< '), sg.Text('GRÁFICO')],
        [sg.Text(' ')],
        [sg.Button('  LEVE  '), sg.Button('  MÉDIO  '), sg.Button('  ALTO  ')],
        [sg.Text('MÚSICA: 90')],
        [sg.Text('🎵  ------------------------------------------------|     🎵')],
        [sg.Text('SONS DO JOGO: 50')],
        [sg.Text('🔈   ---------------------------|                            🔊')],
        [sg.Button('SALVAR')],
        [sg.Output(size=(50,0))]
    ]
    return sg.Window('PÁGINA DAS CONFIGURAÇÕES', layout=layout, finalize=True)


def janela_mapa(): # PÁGINA DO MAPA
    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('( 👨‍🏭 )'), sg.Text('⭐_____²¹°_____'), sg.Text('( 💲 ) |_³°°_____|')],
        [sg.Text('________________________________________|')],
        [sg.Text('...................................................................')],
        [sg.Text('...................................................|......|')],
        [sg.Text('...................................................|......|')],
        [sg.Text('___________________________|')],
        [sg.Text('________________________➡➡')],
        [sg.Text('________________________➡➡                   MAPA DO JOGO')],
        [sg.Text(' ')],
        [sg.Button('OK')],
        [sg.Output(size=(50,0))]
    ]
    return sg.Window('PÁGINA DO MAPA', layout=layout, finalize=True)

def janela_sair(): # PÁGINA PARA SAIR
    sg.theme('DarkBlue16')
    layout = [
        [sg.Text('                VOCÊ REALMENTE DESEJA SAIR DO JOGO ?')],
        [sg.Button('SIM'), sg.Button('NÃO')],
        [sg.Output(size=(50,0))]
    ]
    return sg.Window('PÁGINA PARA SAIR', layout=layout, finalize=True)

janela1, janela2, janela3, janela4, janela5, janela6, janela7 = janela_inicial(), None, None, None, None, None, None

while True:
    window,event,values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        janela1.hide()
        janela7 = janela_sair()
    if window == janela7 and event == 'SIM':
        break
    if window == janela7 and event == 'NÃO':
        janela7.hide()
        janela1.un_hide()

    if window == janela1 and event == '        COMEÇAR        ':
        janela2 = janela_começar()
        janela1.hide()

    if window == janela2 and event == 'NÃO':
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'SIM':
        janela3 = janela_começar2()
        janela2.hide()

    if window == janela3 and event == ' <<< ':
        janela3.hide()
        janela1.un_hide()

    if window == janela3 and event == 'CONTINUAR':
        janela3.hide()
        sg.popup_ok('OLÁ JOGADOR! BEM VINDO AO \nAQUACITY! MEU NOME É MARI E \nESTOU AQUI PARA TE DAR\n UMA MÃOZINHA')
        sg.popup_ok('ESTA É UMA VISÃO GERAL DAS FASES \nE DO SEU PERFIL. PASSE POR MISSÕES \nE RESOLVA PROBLEMAS SANITÁRIOS \nPARA AJUDAR A POPULAÇÃO E AVANÇAR \nEM SUA JORNADA!')
        janela7 = janela_mapa()
    
    if window == janela7 and event == 'OK':
        break


    # QUANDO APERTAR EM CONTINUAR
    if window == janela1 and event == '       CONTINUAR       ':
        janela4 = janela_continuar()
        janela1.hide()
    
    if window == janela4 and event == ' <<< ':
        janela4.hide()
        janela1.un_hide()

    
    if window == janela4 and event == 'SAVE1':
        janela5 = janela_continuar2()
        janela4.hide()

    if window == janela5 and event == 'SIM':
        janela5.hide()
        sg.popup_ok('RETOMANDO AO PROGRESSO "SAVE1"')
        janela7 = janela_mapa()

    if window == janela5 and event == 'NÃO':
        janela5.hide()
        janela4.un_hide()

    # FUNÇÕES CONFIGURAÇÕES
    if window == janela1 and event == ' ⚙ ':
        janela6 = janela_configurações()
        janela1.hide()
    
    if window == janela6 and event == ' <<< ':
        janela6.hide()
        janela1.un_hide()
    
    if window == janela6 and event == 'SALVAR':
        janela6.hide()
        janela1.un_hide()