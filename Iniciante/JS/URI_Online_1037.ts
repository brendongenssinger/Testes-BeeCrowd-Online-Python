// Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos 
//([0,25], (25,50], (50,75], (75,100]) este valor se encontra. 

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



import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const arrayValues = [0,25,50,75,100]
const arrayValuesSort = arrayValues.sort((a,b)=> b-a);
const maxValue = Math.max(...arrayValues);
const minValue = Math.min(...arrayValues);

rl.question('', (input: string) => {

    const textIntervalo = 'Intervalo'
    const inputNumber = Number(input);    
    let stop = false;

    arrayValuesSort.forEach((item,index)=>{        
        if(stop)return;        
        // -0.00 e > 100.01
        if(inputNumber < minValue || inputNumber>maxValue){
            console.log('Fora de intervalo');
            stop = true;
            showConsole('if 1')
        }
        
        else if(inputNumber==item && arrayValues[index+1] == minValue){
            console.log(`${textIntervalo} [${arrayValues[index+1]},${item}]`);
            stop = true;
            showConsole('if 2')
        }
        else if (inputNumber==item && inputNumber == maxValue){
            console.log(`${textIntervalo} (${arrayValues[index+1]},${item}]`);
            stop = true;
            showConsole('if 3')
        }       
        else if(inputNumber==item && inputNumber== minValue){
            console.log(`${textIntervalo} [${item},${arrayValues[index-1]}]`);
            stop = true;            
            showConsole('if 4')
        }
        else if(inputNumber==item){
            console.log(`${textIntervalo} (${arrayValues[index+1]},${item}]`);
            stop = true;            
            showConsole('if 4')
        }
        else if (inputNumber>item && inputNumber <= maxValue && inputNumber >= minValue){
            console.log(`${textIntervalo} (${arrayValues[index]},${arrayValues[index-1]}]`);
            stop = true;            
            showConsole('if 5')
            
        }
        
       
    });
    
    rl.close();

    
});



function showConsole(message: string) {
    //console.log(message)
}

