const addSum = (a, b, callback) => {
    setTimeout(() => {
        if(typeof a !== 'number' || typeof b !== 'number'){
            return callback('a, b must be number');
        }
        var sum = a+b;
        console.log({sum});
        callback(undefined, sum);
    }, 1000);
}

let callback = 
addSum(10, 30, (error, sum) => {
    if(error) return console.log({error});
    addSum(sum,30, (error, sum) => {
        if(error) return console.log({error});
        addSum(sum,30, (error, sum) => {
            if(error) return console.log({error});
            addSum(sum,30, (error, sum) => {
                if(error) return console.log({error});
            });
        });
    });
});