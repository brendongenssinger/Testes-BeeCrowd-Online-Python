"use strict";
// Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos 
//([0,25], (25,50], (50,75], (75,100]) este valor se encontra. 
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
// Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
// O símbolo ( representa "maior que". Por exemplo:
// [0,25]  indica valores entre 0 e 25.0000, inclusive eles.
// (25,50] indica valores maiores que 25 Ex: 25.00001 até o valor 50.0000000
//25.01 Intervalo (25,50]
//25.00 Intervalo [0,25]
//100.00 Intervalo (75,100]
//-25.02
// ( indica que é maior
// ] está entre
const readline = __importStar(require("readline"));
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
const arrayValues = [0, 25, 50, 75, 100];
rl.question('', (input) => {
    const textIntervalo = 'Intervalo';
    const inputNumber = Number(input);
    console.log(inputNumber);
    arrayValues.forEach((item, index) => {
        if (inputNumber < 0) {
            console.log('Fora do intervalo');
            return;
        }
        else if (inputNumber == item) {
            console.log(`${textIntervalo} [${arrayValues[index - 1]},${item})`);
            return;
        }
        else if (inputNumber > item) {
            console.log(`${textIntervalo} (${arrayValues[index - 1]},${item})`);
            return;
        }
    });
    rl.close();
});
