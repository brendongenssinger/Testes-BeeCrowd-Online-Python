// Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.



// Entrada
// O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

// Saída
// O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.



import * as readline from 'readline';

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const arrayValues = [ 
    { codigo: 1, Especificacao: 'Cachorro Quente', Preco: 4.00 },
    { codigo: 2, Especificacao: 'X-SALADA', Preco: 4.50 },
    { codigo: 3, Especificacao: 'X-Bacon', Preco: 5.00 },
    { codigo: 4, Especificacao: 'Torrada Simples', Preco: 2.00 },
    { codigo: 5, Especificacao: 'Refrigerante', Preco: 1.50 }]

rl.question('', (input: string) => {
    const inputs = input.split(' ');
    const codigo = Number(inputs[0]);
    const qtd = Number(inputs[1]);    
    const item = arrayValues.find(item=>item.codigo==codigo);
    if(item){
        const total = item.Preco * qtd;
        console.log('Total: R$ '+total.toFixed(2));
    }
    else{
        console.log('Item não encontrado')
    }
    
    rl.close();
    });
    

