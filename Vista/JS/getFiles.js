import { getCSV } from "./getCSV.js";
import { quitarExtension } from "./quitarExtension.js";

export function getFiles(data) {
    const container = document.getElementById('downloads-container')
    const links = document.createElement('div')
    links.id = 'links-zone'
    links.className = 'links-zone'
    data.forEach(element => {
        let link = document.createElement('div')
        link.className = 'link'
        
        let nameFile = document.createElement('div')
        nameFile.className = 'name-file'
        let pharagraph = document.createElement('p')
        pharagraph.innerText = element
        nameFile.appendChild(pharagraph)
        let watch = document.createElement('div')
        watch.id = element
        let watchContent = document.createElement('div')
        watchContent.innerHTML = `<i class="fa-regular fa-eye" onclick="watchCSV('${element}')"></i>`
        watch.appendChild(watchContent)
        
        let download = document.createElement('div')
        download.className = 'download'
        let referencia = document.createElement('a')
        referencia.download = element
        referencia.href = `http://192.168.100.44:3000/uploads/${element}`
        let button = `
        <button>
            <p>Descargar</p>
            <i class="fa-solid fa-download"></i>
        </button>
        `
        referencia.innerHTML = button
        download.appendChild(referencia)
        link.appendChild(nameFile)
        link.appendChild(watch)
        link.appendChild(download)
        
        links.appendChild(link)

        container.appendChild(links)
    });
}