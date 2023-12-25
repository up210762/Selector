const handleFormSubmission = (event) => {
    event.preventDefault();

    const fileInput = document.querySelector('input[type=file]')
    const newFile = document.getElementById('txt-new-name')
    const groupsToCreate = document.getElementById('txt-groups')
    const quantityByGroup = document.getElementById('txt-alumnos-grupo')
    const alertContent = document.getElementById('alert')
    const errorMessage = document.createElement('p')
    if (alertContent.childElementCount > 0){
        alertContent.removeChild(document.getElementById('alert-text'))
    }

    if (!fileInput.files.length) {
        alertContent.className = 'error'
        errorMessage.id = 'alert-text'
        errorMessage.innerText = 'Por favor selecciona un archivo.'
        alertContent.appendChild(errorMessage) 
        return
    }

    if (!newFile.value || !groupsToCreate.value || !quantityByGroup.value) {
        alertContent.className = 'error'
        errorMessage.id = 'alert-text'
        errorMessage.innerText = 'Todos los campos son obligatorios.'
        alertContent.appendChild(errorMessage) 
        return
    }

    const allowedExtensions = 'csv'
    const fileName = fileInput.files[0].name
    const fileNameParts = fileName.split(".")
    const extension = fileNameParts[fileNameParts.length - 1]

    if (!(extension.toLowerCase() === allowedExtensions)) {
        alertContent.className = 'error'
        errorMessage.id = 'alert-text'
        errorMessage.innerText = `La extensión del archivo no es válida. solo se permiten archivos ${allowedExtensions}`
        alertContent.appendChild(errorMessage) 
        return
    }

    alertContent.className = ''

    const formData = new FormData()
    formData.append('file', fileInput.files[0])
    formData.append('txt-new-name', newFile.value)
    formData.append('txt-groups', groupsToCreate.value)
    formData.append('txt-alumnos-grupo', quantityByGroup.value)

    fetch('http://192.168.100.44:5000/upload', {
        method: 'POST',
        body: formData
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
        alertContent.className = 'success'
        errorMessage.id = 'alert-text'
        errorMessage.innerText = `Archivo procesado.`
        alertContent.appendChild(errorMessage) 
    })
    .catch(error => {
        alertContent.className = 'error'
        errorMessage.id = 'alert-text'
        errorMessage.innerText = error
        alertContent.appendChild(errorMessage)
    })
}
