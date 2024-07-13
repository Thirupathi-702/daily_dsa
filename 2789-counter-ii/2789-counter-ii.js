/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let r=init;
    
    function increment(){
        return ++r;
    }
    function reset(){
        return r=init;
    }
    function decrement(){
        return --r;
    }
    return {increment,reset,decrement}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */