//Bloco do menu
function hasClass(elementId, className) {
    const element = document.getElementById(elementId);
    return element.classList.contains(className);
};

function sideOn (){
    document.getElementById('sidebar').classList.remove('collapse');
    document.getElementById('content').classList.add('sideOn');
    document.getElementById('content').classList.remove('sideOff');
    document.getElementById('nav-logo').classList.remove('sideOff');
    const btn = document.getElementById('btn-toggle');
    btn.classList.remove('sideOff');
    btn.innerHTML = '<i class="fa fa-times fa-lg"></i>'
};

function sideOff (){
    document.getElementById('sidebar').classList.add('collapse');
    document.getElementById('content').classList.remove('SideOn');
    document.getElementById('content').classList.add('sideOff');
    document.getElementById('nav-logo').classList.add('sideOff');
    const btn = document.getElementById('btn-toggle');
    btn.classList.add('sideOff');
    btn.innerHTML = '<i class="fa fa-bars fa-lg"></i>'
}


function toggleSidebar() {
    const chk = hasClass('sidebar', 'collapse'); 
    if (chk) {
        sideOn()
    } else {
        sideOff()
    }
}

// Verifica o tamanho da tela ao carregar a página
document.addEventListener('DOMContentLoaded', function() {
    if (window.innerWidth <= 768) {
        sideOff()
    } else {
        sideOn()
    }
});

// Adiciona um listener para ajustar o menu ao redimensionar a janela
window.addEventListener('resize', function() {
    if (window.innerWidth > 768) {
        sideOn()
    } else {
        sideOff()
    }
});