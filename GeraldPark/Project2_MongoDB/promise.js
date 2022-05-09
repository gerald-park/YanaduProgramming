const addSum = (a,b)=>{
    return new Promise((resolve, reject)=>{
        setTimeout(()=>{
            if(typeof a !=='number' || typeof b !== 'number') {
                reject('a,b must be numbers')
            };
            var sum = a+b;
            console.log({sum})
            resolve(sum);
        }, 1000);
    });
}

//Promise
/*
addSum(10,20)
    .then(sum1 => addSum(sum1,1))
    .then(sum1 => addSum(sum1,1))
    .then(sum1 => addSum(sum1,1))
    .then(sum1 => addSum(sum1,1))
    .then(sum1 => addSum(sum1,1))
    .then(sum => console.log({ sum }))
    .catch((error) => console.log({ error }))

*/
//await 
const totalSum = async () => {
    try{
        let sum1 = await addSum(10,10);
        let sum2 = await addSum(sum1,10);
        let sum3 = await addSum(sum2,10);
        let sum4 = await addSum(sum3,10);
        let sum5 = await addSum(sum4,10);
        console.log({ sum1, sum2, sum3, sum4, sum5 });    
    }catch(err) {
        if(err) console.log({err})
    }
    
}
totalSum();