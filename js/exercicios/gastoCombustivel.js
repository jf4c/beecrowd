const input = require('../node_modules/readline-sync');

const tempoViagem = input.question('Digite o tempo de viagem em horas: ');
const velocidadeMedia = input.question('digite a velocidade media em km/h: ');

const distancia = velocidadeMedia * tempoViagem;
const litros = distancia / 12;

console.log(`${litros.toFixed(3)}`);

