const handleFormSubmission = (event) => {
    event.preventDefault();

    const fileInput = document.querySelector('input[type=file]')
    const newFile = document.getElementById('txt-new-name')
    const groupsToCreate = document.getElementById('txt-groups')
    const quantityByGroup = document.getElementById('txt-alumnos-grupo')
    const alertContent = document.getElementById('alert')
    const errorMessage = document.createElement('p')

    if (!fileInput.files.length) {
        alertContent.className = 'error'
        errorMessage.innerText = 'Por favor selecciona un archivo.'
        alertContent.appendChild(errorMessage) 
        return
    }

    if (!newFile.value || !groupsToCreate.value || !quantityByGroup.value) {
        alertContent.className = 'error'
        errorMessage.innerText = 'Todos los campos son obligatorios.'
        alertContent.appendChild(errorMessage) 
        return
    }

    const allowedExtensions = ['.csv']
    const fileName = fileInput.files[0]
    console.log(fileName)
    const fileExtension = 'csv'

    if (allowedExtensions.indexOf('.' + fileExtension) === -1) {
        alertContent.className = 'alert'
        errorMessage.innerText = `La extensión del archivo no es válida. solo se permiten archivos ${allowedExtensions[0]}`
        alertContent.appendChild(errorMessage) 
        return
    }

    alertContent.className = ''

    const formData = new FormData()
    formData.append('file', fileInput.files[0])
    formData.append('txt-new-name', newFile.value)
    formData.append('txt-groups', groupsToCreate.value)
    formData.append('txt-alumnos-grupo', quantityByGroup.value)

    fetch('http://localhost:5000/upload', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const alertContent = document.getElementById('alert')
        alertContent.className = "success"
        alertContent.innerText = data
    })
    .catch(error => {
        console.error("Error al enviar el archivo: ", error)
    })
}