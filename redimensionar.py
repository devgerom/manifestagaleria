from PIL import Image
import os

# Pasta onde estão suas imagens (ajuste se necessário)
pasta_imagens = "obras-otimizadas/otimizadas/"

# Tamanho máximo (largura em pixels)
TAMANHO_MAXIMO = 1200

# Qualidade da imagem (80-85 é bom para web)
QUALIDADE = 85

print("🚀 Iniciando redimensionamento...")
print(f"📁 Pasta: {pasta_imagens}")
print(f"📏 Tamanho máximo: {TAMANHO_MAXIMO}px")
print(f"🎨 Qualidade: {QUALIDADE}%")
print("-" * 50)

# Verifica se a pasta existe
if not os.path.exists(pasta_imagens):
    print(f"❌ ERRO: Pasta '{pasta_imagens}' não encontrada!")
    print("Verifique se o caminho está correto.")
    exit()

# Contadores
total_imagens = 0
imagens_redimensionadas = 0
imagens_puladas = 0

# Percorre todos os arquivos da pasta
for arquivo in os.listdir(pasta_imagens):
    # Verifica se é imagem
    if arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.webp', '.bmp', '.gif')):
        total_imagens += 1
        caminho_completo = os.path.join(pasta_imagens, arquivo)
        
        try:
            # Abre a imagem
            img = Image.open(caminho_completo)
            
            # Verifica se precisa redimensionar
            if img.width > TAMANHO_MAXIMO:
                # Calcula nova altura mantendo proporção
                proporcao = TAMANHO_MAXIMO / img.width
                nova_altura = int(img.height * proporcao)
                
                # Mostra tamanho original
                print(f"📐 {arquivo}")
                print(f"   Original: {img.width}x{img.height}")
                
                # Redimensiona (LANCZOS é o algoritmo de melhor qualidade)
                img_redimensionada = img.resize((TAMANHO_MAXIMO, nova_altura), Image.Resampling.LANCZOS)
                
                # Salva com otimização
                img_redimensionada.save(caminho_completo, optimize=True, quality=QUALIDADE)
                
                imagens_redimensionadas += 1
                print(f"   ✅ Nova: {TAMANHO_MAXIMO}x{nova_altura}")
                print(f"   💾 Economia: ~{int((1 - (TAMANHO_MAXIMO * nova_altura)/(img.width * img.height)) * 100)}%")
            else:
                # Se já for pequena, apenas otimiza
                print(f"⏭️ {arquivo} - já está ok ({img.width}x{img.height})")
                img.save(caminho_completo, optimize=True, quality=QUALIDADE)
                imagens_puladas += 1
                
        except Exception as e:
            print(f"❌ Erro ao processar {arquivo}: {e}")

print("-" * 50)
print(f"📊 RESUMO FINAL:")
print(f"   📸 Total de imagens: {total_imagens}")
print(f"   ✨ Redimensionadas: {imagens_redimensionadas}")
print(f"   👍 Mantidas originais: {imagens_puladas}")
print(f"   ❌ Erros: {total_imagens - imagens_redimensionadas - imagens_puladas}")
print("✨ Finalizado com sucesso!")