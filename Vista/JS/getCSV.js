import { downloadFile } from "./downloadFile.js"
export function getCSV(id, archivo){
    document.getElementById(id).addEventListener('click', ()=>{
        fetch(`http://localhost:3000/uploads/${archivo}`, {
            method:'GET'
        })
        .then(response=>response.json())
        .then(data=>{
            downloadFile(archivo, data)
        })
        .catch(err=>{
            return err
        })
    })
}




// export function downloadFile(id, filename) {
//     document.getElementById(id).addEventListener('click', async () => {
//         let data = getCSV(filename, ()=>download(filename, data))
//         console.log("Esto va después ",data)
//     })
// }

// function download(filename, textInput) {
//     let element = document.createElement('a')
//     element.s
// setAttribute('href', 'data:text/plain;charset=utf-8, ' + encodeURIComponent(textInput))
//     element.setAttribute('download', filename)
//     document.body.appendChild(element)
//     element.click()
// }