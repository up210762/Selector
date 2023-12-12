export function quitarExtension(archivo) {
    return archivo.split('.').slice(0,-1).join('.')
}