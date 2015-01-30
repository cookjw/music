// attach the .equals method to Array's prototype to call it on any array
// (credit: http://stackoverflow.com/questions/7837456/comparing-two-arrays-in-javascript )
// Array.prototype.equals = function (array) {
    // // if the other array is a falsy value, return
    // if (!array)
        // return false;

    // // compare lengths - can save a lot of time 
    // if (this.length != array.length)
        // return false;

    // for (var i = 0, l=this.length; i < l; i++) {
        // // Check if we have nested arrays
        // if (this[i] instanceof Array && array[i] instanceof Array) {
            // // recurse into the nested arrays
            // if (!this[i].equals(array[i]))
                // return false;       
        // }           
        // else if (this[i] != array[i]) { 
            // // Warning - two different object instances will never be equal: {x:20} != {x:20}
            // return false;   
        // }           
    // }       
    // return true;
// }  

// "Prototyping" (monkeypatching the built-in class) didn't work, because it made it think every array
// had an "equals" attribute to be inspected every time the array was looped through; otherwise the
// logic of the function below is the same.

function equals (firstArray, secondArray) {
    if (!secondArray){
        return false;
        }
        
    if (firstArray.length != secondArray.length) {
        return false;
    }
    var l = firstArray.length;
    for (var i = 0;  i < l; i++) {
        if (firstArray[i] instanceof Array && secondArray[i] instanceof Array) {
            if (!equals(firstArray[i], secondarray[i])){
                return false;
            }
        }
        else if (firstArray[i] != secondArray[i]) {
                return false
            }
        }        
    return true;
}

function arrayContains(array, value) {
    for (var index in array){
        item = array[index];
        if (item === value) {
            return true;
        } else if (item instanceof Array){
            if (equals(item,value)){
                return true;
        }    
        }
    }
    return false;
}



function normalMod(number, modulus){
    if(number >= 0){
        return number % modulus;
    } else {
        while (number < 0) {
            number = number + modulus;
        }
        return number % modulus;
    }   
}

function copy(list){
    var newList = []
    for (index in list){        
        newList.push(list[index]);
    }
    return newList;
}

function removeDuplicates(list){
    var newList = [];      
    for (index in list){ 
        var item = list[index];        
        if (!(arrayContains(newList, list[index]))){            
            newList.push(list[index]);        
        }
    }
    return newList;
}



function rotate(pcSet, number){
    return pcSet.slice(number).concat(pcSet.slice(0, number)) ;
}

function distance(pcSet){
    return normalMod(pcSet[pcSet.length-1] - pcSet[0], 12) ;
}

function tiebreaker(candidateList, cardinality){

    var n = 2;
    var list = candidateList;

    while (list.length > 1){
        var distanceArray = [];
        for (var index in list){
            pcSet = list[index];
            distanceArray.push(distance(pcSet.slice(0, n)));
        }
        dAMin = Math.min.apply(null, distanceArray);
        var candidates = [];
        for (index in list){
            candidate = list[index];
            if (distance(candidate.slice(0,n)) === dAMin){
                candidates.push(candidate);
            }
        }
        list = removeDuplicates(candidates);
        n+=1        
        if (n > cardinality){
            throw "the variable n has gotten larger than it was supposed to." ;
        }
    }
    return list[0];
}

function findNormalForm(pcSet){
    var pcSet = removeDuplicates(pcSet).sort(function(a, b){return a-b});
    var rotations = [];    
    for (var i=0; i < pcSet.length; i++){
        rotations.push(rotate(pcSet, i));
    } 
    var distances = [];
    for (var index in rotations){
        var pcSet = rotations[index];
        distances.push(distance(pcSet));
    }    
    var minimumDistance = Math.min.apply(null, distances);
    var rotationArray = [];
    for (var index in rotations){
        var rotation = rotations[index];
        if (distance(rotation) === minimumDistance){
            rotationArray.push(rotation) ;
        };
    };
    var minimumDistanceList = removeDuplicates(rotationArray);    
    if (minimumDistanceList.length === 1) {
        var normalForm = minimumDistanceList[0] ;
    } else {
        var normalForm = tiebreaker(minimumDistanceList, pcSet.length) ;
    }
    var normalFormFromZero = [];
    for (var index in normalForm){
        var x = normalForm[index];
        normalFormFromZero.push(normalMod(x - normalForm[0], 12));
    }
    return normalFormFromZero;
}

function findPrimeForm(pcSet){
    var pcSet = findNormalForm(pcSet);
    inverses = [];
    for (var index in pcSet){
        var x = pcSet[index];
        inverses.push(normalMod(0 - x, 12));
    }
    
    var inversion = findNormalForm(inverses);    
    var candidates = [pcSet, inversion];
    var canDistances = [distance(pcSet), distance(inversion)];
    var minimumDistanceList = [];
    for (var index in candidates){
        var candidate = candidates[index];
        if(distance(candidate)=== Math.min.apply(null, canDistances)){
            minimumDistanceList.push(candidate);
        }
    }
    var minimumDistanceList = removeDuplicates(minimumDistanceList);    
    primeForm = tiebreaker(minimumDistanceList, pcSet.length);
    return primeForm;
    
}

function prepare(input){ 
    var inputArray = input.split(",");
    var pcSet = [];
    for (index=0; index < inputArray.length; index++){
        pcSet[index] = Number(inputArray[index]);
    }
    return pcSet;
}

function getResult(){    
    this.output.value = findPrimeForm(prepare(
        this.input.value
        ));
}



