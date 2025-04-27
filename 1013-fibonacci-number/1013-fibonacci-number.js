/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    let map=new Map()
    if(n<=1)return n
    
    if(map.has(n)){
        return map.get(n)
    }
    let result=fib(n-1)+fib(n-2)
    map.set(n,result)
    return result
};