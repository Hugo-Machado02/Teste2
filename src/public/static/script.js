let texto = `O Homem-Aranha, também conhecido como Peter Parker, é um dos super-heróis mais icônicos da Marvel Comics, criado por Stan Lee e Steve Ditko. Ele apareceu pela primeira vez na revista "Amazing Fantasy" #15 em 1962. Peter Parker é um jovem órfão criado por seus tios, May e Ben Parker, em Queens, Nova York. Após ser mordido por uma aranha radioativa, Peter adquire habilidades sobre-humanas, como força e agilidade aumentadas, capacidade de aderir a paredes e um "sentido aranha" que o alerta sobre perigos iminentes.

Ele decide usar seus poderes para o bem após a trágica morte de seu tio Ben, que o inspira com o lema: "Com grandes poderes vêm grandes responsabilidades." Além de combater o crime como Homem-Aranha, Peter enfrenta os desafios da vida cotidiana, como manter sua identidade secreta, equilibrar sua vida escolar e profissional, e cuidar de sua tia May.

Trabalhando como fotógrafo para o "Daily Bugle", onde o editor J. Jonah Jameson frequentemente difama o Homem-Aranha, Peter lida com uma série de vilões icônicos, incluindo o Duende Verde, Doutor Octopus, Venom, e o Homem-Areia. Ao longo dos anos, ele forma alianças com outros super-heróis, como os Vingadores e o Quarteto Fantástico. A popularidade do Homem-Aranha transcende os quadrinhos, resultando em várias adaptações para televisão, cinema, e videogames, tornando-o um símbolo duradouro de coragem, responsabilidade e determinação.
`;

var opcao = [
    { value: 'ARE1467492'},
    { value: 'ARE1467493'},
    { value: 'RE1461810'},
    { value: 'RE1463299'}
];

function addSelect(){
    var select = document.getElementById('SelecionaProjeto');
    
    for (let i = 0; i < opcao.length; i++){
        var novaOpcao = document.createElement('option');
        novaOpcao.value = opcao[i].value;
        novaOpcao.text = opcao[i].value;
        select.appendChild(novaOpcao);
    }
}

//envia os dados e recebe o retorno com o resumo
function getResumo(){
    let resultResumo = document.getElementById("SelecionaProjeto").value;

    if(resultResumo != ""){
        fetch('/resumo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(resultResumo)
        })
        .then(response => response.json())
        .then(data => {
            retornaResumo(resultResumo + " - " + data.valueReturn);
        })
        .catch((error) => {
            alert('Erro:', error);
        });
    }
    else{
        retornaResumo("Erro! Por favor, selecione um processo");
    }
}


//retorna o valor para o HTML dentro do Textarea
function retornaResumo(val){
    document.getElementById("resultResumo").value = val;
    ajustarAlturaTextarea();
}

//realiza o ajuste do textarea conforme o numero de linhas
function ajustarAlturaTextarea() {
    var textarea = document.getElementById("resultResumo");
    textarea.style.height = "";
    textarea.style.height = textarea.scrollHeight*1.01 + "px";
    // let labelResumo = document.getElementById("LabelResumo")
    // labelResumo.style.display = 'none';
}
