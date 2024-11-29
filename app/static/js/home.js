let monitoramento = document.querySelector('.monitoramento');
let statuss = document.querySelector('.status');



let ocupacaoTexto = monitoramento.querySelector('span').textContent;
let valorNumerico = parseFloat(ocupacaoTexto.replace('%', '').trim());

let porcentagem = monitoramento.querySelector('p');
let disponibilidade = statuss.querySelector('p');

monitoramento.querySelector('input').value = valorNumerico;

let input = monitoramento.querySelector('input');
let min = parseFloat(input.min);  
let max = parseFloat(input.max);  

let porcentagemCalculada = ((valorNumerico - min) / (max - min)) * 100;
console.log("Porcentagem calculada:", porcentagemCalculada);
porcentagem.textContent = ""

if(porcentagemCalculada > 100){
    porcentagem.textContent = `100%`;
    disponibilidade.textContent = 'Indisponivel'

}
else if(valorNumerico === 0){
    porcentagem.textContent = `0%`
    disponibilidade.textContent = 'Disponivel'
    monitoramento.querySelector('input').value = valorNumerico -50;

    
    
}
else if(porcentagemCalculada < 0 ){
    porcentagem.textContent = `0%`;
    disponibilidade.textContent = 'Disponivel'

}
else{
    porcentagem.textContent = `${porcentagemCalculada.toFixed(0)}%`
    disponibilidade.textContent = 'Disponivel'
}

console.log("Valor numérico:", valorNumerico);
console.log("Texto atualizado com porcentagem:", porcentagem);

