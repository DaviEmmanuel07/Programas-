import os
import shutil


def criar_pasta_se_necessario(caminho):
    if not os.path.exists(caminho):
        os.makedirs(caminho)
        print(f"Pasta criada: {caminho}")

def organizar_todos_os_ficheiros(pasta_trabalho):
    
    pasta_videos = pasta_trabalho + "/Videos_Brutos"
    pasta_imagens = pasta_trabalho + "/Imagens"
    pasta_audios = pasta_trabalho + "/Audios"
    
    
    criar_pasta_se_necessario(pasta_videos)
    criar_pasta_se_necessario(pasta_imagens)
    criar_pasta_se_necessario(pasta_audios)
    
    ficheiros = os.listdir(pasta_trabalho)
    
    for ficheiro in ficheiros:
        caminho_antigo = pasta_trabalho + "/" + ficheiro
        
        
        if os.path.isfile(caminho_antigo):
            
            
            if ficheiro.endswith(".mp4") or ficheiro.endswith(".mov"):
                shutil.move(caminho_antigo, pasta_videos + "/" + ficheiro)
                print(f"Vídeo movido: {ficheiro}")
                
            elif ficheiro.endswith(".png") or ficheiro.endswith(".jpg"):
                shutil.move(caminho_antigo, pasta_imagens + "/" + ficheiro)
                print(f"Imagem movida: {ficheiro}")
                
            elif ficheiro.endswith(".mp3") or ficheiro.endswith(".wav"):
                shutil.move(caminho_antigo, pasta_audios + "/" + ficheiro)
                print(f"Áudio movido: {ficheiro}")

caminho_da_sua_pasta = "SEU_CAMINHO_AQUI" 
organizar_todos_os_ficheiros(caminho_da_sua_pasta)
