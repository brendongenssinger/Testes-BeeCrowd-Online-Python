
import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Informe um número: ', (input: string) => {

    const number = Number(input);
    const isPar = number%2 == 0;
    if(isPar)
        console.log('Is Par');
    else{
        console.log('Not is Par');
    }
   rl.close();
});


