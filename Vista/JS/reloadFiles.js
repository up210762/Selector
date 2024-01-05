import { getFiles } from "./getFiles.js"

document.getElementById('submit-form').addEventListener('click', (e) => {
e.preventDefault()
fetch('http://192.168.100.44:5000/getfiles', {
    method: 'GET',
})
.then(response => response.json())
.then(data => {
    const container = document.getElementById('downloads-container')
    const links = document.getElementById('links-zone')
    if (container.childElementCount > 0){
        container.removeChild(links)
    }
    getFiles(data)
})
})