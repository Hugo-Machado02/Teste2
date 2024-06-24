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
        retornaResumo("Gerando Resumo! Por favor aguarde...");
        ajustarAlturaTextarea();
        fetch('/resumo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(resultResumo)
        })
        .then(response => response.json())
        .then(data => {
            retornaResumo(data.valueReturn);
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
