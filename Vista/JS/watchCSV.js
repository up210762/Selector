async function watchCSV(id){
    document.getElementById(id).addEventListener('click', (e)=>{
        e.preventDefault()
        fetch(`http://192.168.100.44:5000/getfiles/${id}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            const tablaContainer = document.getElementById("tabla-container")
            if (tablaContainer.childElementCount > 0){
                tablaContainer.removeChild(document.getElementById("renderizado-csv"))
            }
            const tabla = document.createElement('table')
            tabla.id = 'renderizado-csv'
            const encabezadoTabla = document.createElement('thead')
            const titulos = ['Nombre', 'Matrícula', 'Grupo']

            titulos.forEach(element => {
                let tituloColumna = document.createElement('th')
                tituloColumna.innerText = element
                tituloColumna.id = element.toLowerCase()
                encabezadoTabla.appendChild(tituloColumna)
            });
            tabla.appendChild(encabezadoTabla)

            data.forEach(element => {
                let contenidos = new Array(element[0], element[1], element[2])
                let cuerpoTabla = document.createElement('tbody')
                contenidos.forEach(element => {
                    let contenidoTabla = document.createElement('td')
                    contenidoTabla.innerText = element
                    cuerpoTabla.appendChild(contenidoTabla)
                });
                tabla.appendChild(cuerpoTabla)
            });
            tablaContainer.appendChild(tabla)
            const alertContent = document.createElement('div')
            alertContent.className = 'success'
            const errorMessage = document.createElement('div')
            errorMessage.id = 'alert-text'
            errorMessage.innerText = `Archivo procesado.`
            alertContent.appendChild(errorMessage) 
        })
        .catch(error => {
            alertContent.className = 'error'
            errorMessage.innerText = error
            alertContent.appendChild(errorMessage)
        })
    })
}