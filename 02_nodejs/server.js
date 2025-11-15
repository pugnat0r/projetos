import { createServer } from 'node:http'

const server = createServer ( () => {
    console.log ( 'Servidor rodando...')
} )

server.listen ( 3333 )