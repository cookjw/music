
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
        if ($.inArray(list[index], newList) === -1){
            newList.push(list[index]);        
        }
    }
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
        if (n > cardinality){
            throw "the variable n has gotten larger than it was supposed to." ;
        }
    }
    return list[0];
}

function findNormalForm(pcSet){
    var pcSet = removeDuplicates(pcSet).sort();
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

// function businessLogic(pcSet){
    // return rotate(pcSet, 1);
// }

function getResult(){
    this.output.value = findPrimeForm(prepare(
        this.input.value
        ));
}