const nombreInput = document.getElementById('nombreCompleto')
const pesoInput = document.getElementById('peso')
const guardarBtn = document.getElementById('guardarBtn')
const mensajeDiv = document.getElementById('mensajeGuardado')

const peso_maximo = 30
const peso_minimo = 300

guardarBtn.onclick = function(){
    const nombre = nombreInput.value.trim()
    const peso = parseFloat(pesoInput.value)

    if (nombre === "" | isNaN(peso)){
        mensajeDiv.style.color = 'red'
        mensajeDiv.textContent = 'Escribe un nombre y un peso'
        return
    }

    if (peso < peso_minimo || peso > peso_maximo){
        mensajeDiv.style.color = 'orange'
        mensajeDiv.textContent = `El peso debe estar entre ${peso_minimo} kg y ${peso_maximo} kg`
    }

    mensajeDiv.style.color = 'green'
    mensajeDiv.innerHTML = `
    Datos guardados<br>
    Nombre: ${nombre}<br>
    Peso: ${peso} kg
    `
}