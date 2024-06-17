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

rl.question('', (input: string) => {

    const textIntervalo = 'Intervalo'
    const inputNumber = Number(input);
    //console.log(inputNumber);
    let stop = false;

    if(arrayValues.find((item,index)=> item==inputNumber)){

    }
    arrayValues.forEach((item,index)=>{
        //console.log(item)
        if(stop)return;
        if()
        if(inputNumber < 0){
            console.log('Fora do intervalo');
            stop = true;
            
        }
        else if(inputNumber==item){
            console.log(`${textIntervalo} [${item},${arrayValues[index+1]})`);
            stop = true;
            
        }
        else if (inputNumber>item){
            console.log(`${textIntervalo} (${arrayValues[index-1]},${item})`);
            stop = true;
            
        }
       
    });
    
    rl.close();
});

