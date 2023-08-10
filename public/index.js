async function carregarAnimais() {
    const response = await axios.get('http://localhost:8000/animais')
    const animais = response.data
    const lista = document.getElementById('lista-animais')
    lista.innerHTML = ''

    animais.map(animal => {
        const item = document.createElement('li')
        item.innerText = animal.nome

        lista.appendChild(item)
    })
}

async function manipularFormulário() {
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')

    form_animal.onsubmit = async (event) => {
        event.preventDefault()
        const nome_animal = input_nome.value

        axios.post('http://localhost:8000/animais', {
            nome: nome_animal,
            idade: 2,
            sexo: "Femea",
            cor: "Marrom"
        })
        carregarAnimais()
        alert('Animal cadastrado com sucesso!')
    }

}


function app() {
    console.log('App iniciada')
    carregarAnimais()
    manipularFormulário()
}

app()