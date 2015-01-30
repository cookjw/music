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
        console.log("I'm going to push item # ".concat(index.toString()));
        newList.push(list[index]);
    }
    return newList;
}

function removeDuplicates(list){
    var newList = [];
    console.log("removeDuplicates is now being applied to the list:");
    console.log(list.toString());
    for (index in list){
        // console.log($.inArray(1,[1,2,3]) === -1);
        // console.log("array contains item I'm looking at:");
        // console.log(arrayContains(newList, list[index]));
        // console.log("list[index]");
        // console.log(list[index].toString());
        // console.log("newList");
        // console.log(newList.toString());
        var item = list[index];
        console.log("I'm checking whether ".concat(item.toString()).concat( "is duplicated in the list"));
        if (!(arrayContains(newList, list[index]))){
            console.log("I didn't find ".concat(list[index].toString()).concat(" in ").concat(newList.toString()));
            newList.push(list[index]);        
        }
    }
    console.log("the resulting duplicate-free list is now being returned:");
    console.log(newList.toString());
    return newList;
}

// function copy(content){
    // var j = document.getElementById("output");
    // j.value = content;    
// }

function rotate(pcSet, number){
    return pcSet.slice(number).concat(pcSet.slice(0, number)) ;
}

function distance(pcSet){
    return normalMod(pcSet[pcSet.length-1] - pcSet[0], 12) ;
}

function tiebreaker(candidateList, cardinality){
    // console.log("candidateList: ");
    // console.log(candidateList);
    // console.log(candidateList[0]);
    // return candidateList[0];
    var n = 2;
    var list = candidateList;
    // console.log("list: ");
    // console.log(list);
    // console.log(list.length);
    while (list.length > 1){
        // console.log("distanceArray");
        // console.log(blah);
        var distanceArray = [];
        // console.log(distanceArray === []);
        // console.log(distanceArray === [4,2]);
        // console.log("distanceArray:");        
        // console.log(distanceArray.toString());

        for (var index in list){
            // console.log(distance(pcSet.slice(0, n)))
                       
            // console.log("index: ");
            // console.log(index);
            pcSet = list[index];
            // console.log("pcSet: ");
            // console.log(pcSet);
            // console.log("pcSet slice: ");
            // console.log(pcSet.slice(0, n));
            // console.log("distance(pcSet slice)");
            // console.log(distance(pcSet.slice(0, n)));
            // // console.log("distanceArray:");
            // // console.log(distanceArray.toString());
            distanceArray.push(distance(pcSet.slice(0, n)));
            // // console.log(distanceArray.toString());
            // console.log("distanceArray:");
            // console.log(distanceArray.toString());
            // console.log(index);
        }
        dAMin = Math.min.apply(null, distanceArray);
        // console.log(dAMin);
        var candidates = [];
        for (index in list){
            candidate = list[index];
            // console.log(distance(candidate.slice(0,n))===dAMin);
            // console.log(candidate.slice(0,n));
            // console.log(distance(candidate.slice(0,n)));
            // console.log(dAMin);
            if (distance(candidate.slice(0,n)) === dAMin){
                candidates.push(candidate);
                // console.log(candidate.toString());
                // console.log(candidates.toString());
            }
        }
        // console.log(candidates.toString());
        list = removeDuplicates(candidates);
        // console.log(list.toString());
        // console.log(candidates.toString());
        n+=1
        console.log(n.toString());
        if (n > cardinality){
            throw "the variable n has gotten larger than it was supposed to." ;
        }
    }
    return list[0];
}

function findNormalForm(pcSet){
    var pcSet = removeDuplicates(pcSet).sort(function(a, b){return a-b});
    console.log(pcSet.toString());
    var rotations = [];    
    for (var i=0; i < pcSet.length; i++){
        rotations.push(rotate(pcSet, i));
    } 
    console.log(rotations.toString());
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
    console.log(minimumDistanceList.toString());
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
    console.log(inverses.toString());
    var inversion = findNormalForm(inverses);
    console.log(inversion.toString());
    var candidates = [pcSet, inversion];
    console.log("candidates:");
    console.log(candidates.toString());
    var canDistances = [distance(pcSet), distance(inversion)];
    var minimumDistanceList = [];
    for (var index in candidates){
        var candidate = candidates[index];
        if(distance(candidate)=== Math.min.apply(null, canDistances)){
            minimumDistanceList.push(candidate);
        }
    }
    var minimumDistanceList = removeDuplicates(minimumDistanceList);
    console.log(minimumDistanceList.toString());
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
    console.log("OK! Let's get started");
    this.output.value = findPrimeForm(prepare(
        this.input.value
        ));
}



