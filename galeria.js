function audioDescricao(idAudio, botao) {
    const audio = document.getElementById(idAudio);
    const icone = botao.querySelector('.icone');
    const texto = botao.querySelector('.texto');
    
    if (!audio) return;
    
    // SE ESTIVER TOCANDO → PAUSA
    if (!audio.paused) {
        audio.pause();
        icone.textContent = '🔊';
        texto.textContent = 'Ouvir audiodescrição';
        return;
    }
    
    // SE NÃO ESTIVER TOCANDO → REINICIA DO COMEÇO E TOCA
    // Para todos os outros áudios
    pausarTodosAudios();
    
    // Reinicia do começo
    audio.currentTime = 0;
    
    // Toca
    audio.play()
        .then(() => {
            icone.textContent = '⏸️';
            texto.textContent = 'Pausar audiodescrição';
        })
        .catch(erro => {
            console.log("Erro ao reproduzir:", erro);
        });
    
    // Quando o áudio terminar naturalmente
    audio.onended = function() {
        icone.textContent = '🔊';
        texto.textContent = 'Ouvir audiodescrição';
    };
}

function pausarTodosAudios() {
    const audios = document.querySelectorAll('.audio-player');
    audios.forEach(audio => {
        audio.pause();
        audio.currentTime = 0; // Reseta todos os outros
    });
    
    // Resetar ícones de todos os botões
    const botoes = document.querySelectorAll('.btn-audio');
    botoes.forEach(botao => {
        botao.querySelector('.icone').textContent = '🔊';
        botao.querySelector('.texto').textContent = 'Ouvir audiodescrição';
    });
}