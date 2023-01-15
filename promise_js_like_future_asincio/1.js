console.log('work')

let promise = new Promise(function (resolve, reject){
    // resolve(100)
    setTimeout(()=>resolve('otvet ot servera'), 3000)
    // reject('Oshibka')
})

console.log(promise)

let perem = ''
let data = fetch('https://jsonplaceholder.typicode.com/users/1')

data.then((dima)=>dima.json())
    .then((user)=>{
        console.log(user.name, 'log promise')
        perem=user.name
        throw new Error('Zhopa')
    }).catch((osh)=>console.log(osh))

console.log(perem)
