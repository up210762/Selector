import { getFiles } from "./getFiles.js"

document.addEventListener('DOMContentLoaded', ()=>{
    fetch('http://192.168.100.44:5000/getfiles', {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => getFiles(data))
})