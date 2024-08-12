/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let y=[]
    for(let i=0;i<arr.length;i++){
        if (fn(arr[i],i)){
            y.push(arr[i])
        }
    }
    return y
    
};