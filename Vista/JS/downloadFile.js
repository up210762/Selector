export function downloadFile(filename, textInput) {
    let element = document.createElement('a')
    element.setAttribute('href', 'data:text/plain;charset=utf-8, ' + encodeURIComponent(textInput))
    element.setAttribute('download', filename)
    document.body.appendChild(element)
    element.click()
}