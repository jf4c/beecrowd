const input = require('readline-sync');

const x1 = input.question('Escreva o valor de x1: ');
const y1 = input.question('Escreva o valor de y1: ');
const x2 = input.question('Escreva o valor de x2: ');
const y2 = input.question('Escreva o valor de y2: ');

// const distancia = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
const distancia = Math.sqrt((x2 - x1)**2 + (y2 - y1)**2);

console.log(`A distancia entre os dois pontos é: ${distancia.toFixed(4)}`);