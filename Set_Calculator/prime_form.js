


function removeDuplicates(list){
    var new_list = [];
    for (item in new_list){
        if ($.inArray(item, new_list) === -1){
            new_list.push(item);        
        }
    }
    return new_list;
}

// function copy(content){
    // var j = document.getElementById("output");
    // j.value = content;    
// }

function rotate(pcSet, number){
    return pcSet.slice(number).concat(pcSet.slice(0, number))
}

function prepare(input){ 
    inputArray = input.split(",")
    pcSet = [];
    for (index=0; index < inputArray.length; index++){
        pcSet[index] = Number(inputArray[index]);
    }
    return pcSet;
}

function businessLogic(pcSet){
    return rotate(pcSet, 1);
}

function getResult(){
    this.output.value = businessLogic(prepare(
        this.input.value
        ));
}